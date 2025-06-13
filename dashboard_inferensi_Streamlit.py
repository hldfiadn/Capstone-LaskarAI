import streamlit as st
import numpy as np
import tensorflow as tf
import os
import requests

st.set_page_config(page_title="Prediksi Penyakit", layout="centered")
st.title("Prediksi Penyakit (Heart Disease, Stroke, Diabetes)")

MODEL_URL = "https://raw.githubusercontent.com/hldfiadn/Capstone-LaskarAI/main/mnn5.keras"
MODEL_PATH = "mnn5.keras"

if not os.path.exists(MODEL_PATH):
    with st.spinner("Mengunduh model..."):
        r = requests.get(MODEL_URL)
        with open(MODEL_PATH, "wb") as f:
            f.write(r.content)

def binary_object(label):
    return st.selectbox(label, [0, 1], format_func=lambda x: "Ya" if x==1 else "Tidak")

def map_age_to_category(age):
    if 18 <= age <= 24: return 1
    elif 25 <= age <= 29: return 2
    elif 30 <= age <= 34: return 3
    elif 35 <= age <= 39: return 4
    elif 40 <= age <= 44: return 5
    elif 45 <= age <= 49: return 6
    elif 50 <= age <= 54: return 7
    elif 55 <= age <= 59: return 8
    elif 60 <= age <= 64: return 9
    elif 65 <= age <= 69: return 10
    elif 70 <= age <= 74: return 11
    elif 75 <= age <= 79: return 12
    elif 80 <= age <= 99: return 13
    else: return 0

# Input
hypertension      = binary_object("Hipertensi")
highchol          = binary_object("Kolestrol tinggi")
cholcheck         = binary_object("Pemeriksaan kolesterol dalam 5 tahun Tterakhir")
bmi               = st.number_input("Boddy Mass Index (BMI)", min_value=10, max_value=100, value=25)
smokingstatus     = binary_object("Perokok aktif")
physactivity      = binary_object("Melakukan aktivitas fisik dalam 30 hari terakhir")
fruits            = binary_object("Mengonsumsi buah setiap hari")
veggies           = binary_object("Mengonsumsi sayur setiap hari")
hvyalcoholconsump = binary_object("Mengonsumsi lebih dari 7 alkohol dalam seminggu")
anyhealthcare     = binary_object("Mempunyai asuransi kesehatan")
nodocbccost       = binary_object("Membayar untuk berobat ke dokter")
menthlth          = st.number_input("Hari buruk mental dalam sebulan, 0–30", min_value=0, max_value=30, value=0)
physhlth          = st.number_input("Hari buruk fisik dalam sebulan, 0–30", min_value=0, max_value=30, value=0)
diffwalk          = binary_object("Kesulitan berjalan atau menaiki tangga")


# GENDER: 0 Perempuan, 1 Laki-laki
gender = st.selectbox("Gender", options=[0, 1], format_func=lambda x: "Perempuan" if x==0 else "Laki-laki")

age_raw          = st.number_input("Usia", min_value=18, max_value=99, value=40)
age_cat          = map_age_to_category(age_raw)

GENHLTH_LABELS = {
    "Sangat Baik": 1,
    "Baik": 2,
    "Cukup Baik": 3,
    "Buruk": 4,
    "Sangat Buruk": 5
}
genhlth_label = st.selectbox("Status Kesehatan Umum", list(GENHLTH_LABELS.keys()))
genhlth = GENHLTH_LABELS[genhlth_label]


EDUCATION_LABELS = {
    "Tidak Pernah Sekolah/Hanya TK": 1,
    "SD": 2,
    "SMP": 3,
    "SMA": 4,
    "Kuliah (1-3 thn)": 5,
    "Lulus Kuliah": 6
}
education_label = st.selectbox("Tingkat Pendidikan", list(EDUCATION_LABELS.keys()))
education = EDUCATION_LABELS[education_label]


INCOME_LABELS = {
    "< Rp 1,000,000": 1,
    "Rp 1,000,000 - Rp 2,999,999": 2,
    "Rp 3,000,000 - Rp 3,999,999": 3,
    "Rp 4,000,000 - Rp 4,999,999": 4,
    "Rp 5,000,000 - Rp 6,999,999": 5,
    "Rp 7,000,000 - Rp 9,999,999": 6,
    "Rp 10,000,000 - Rp 14,999,999": 7,
    "> Rp  15,000,000": 8
}
income_label = st.selectbox("Pendapatan Bulanan", list(INCOME_LABELS.keys()))
income = INCOME_LABELS[income_label]


def one_hot(val, max_val):
    arr = [0]*max_val
    arr[val-1] = 1
    return arr

# Normalisasi
BMI_MEAN, BMI_STD = 28.964194, 6.513529
AGE_MEAN, AGE_STD = 8.254215, 2.911093
MENTHLTH_MEAN, MENTHLTH_STD = 2.930573, 7.400927
PHYSHLTH_MEAN, PHYSHLTH_STD = 4.684104, 9.364345

bmi_input       = (bmi - BMI_MEAN) / BMI_STD
age_input       = (age_cat - AGE_MEAN) / AGE_STD
menthlth_input  = (menthlth - MENTHLTH_MEAN) / MENTHLTH_STD
physhlth_input  = (physhlth - PHYSHLTH_MEAN) / PHYSHLTH_STD

input_vector = [
    hypertension, 
    highchol, 
    cholcheck, 
    bmi_input, 
    smokingstatus,
    physactivity, 
    fruits, 
    veggies, 
    hvyalcoholconsump, 
    anyhealthcare,
    nodocbccost, 
    menthlth_input, 
    physhlth_input, 
    diffwalk, 
    gender,
    age_input, 
    *one_hot(genhlth, 5), 
    *one_hot(education, 6), 
    *one_hot(income, 8)
]
input_arr = np.array([input_vector], dtype=np.float32)

@st.cache_resource
def load_keras_model():
    return tf.keras.models.load_model(MODEL_PATH)

THRESHOLDS = [0.423, 0.248, 0.318]  # Threshold optimal

if st.button("Prediksi"):
    model = load_keras_model()
    pred = model.predict(input_arr)
    pred_values = [p.item() for p in pred]
    hasil = [(1 if p > t else 0) for p, t in zip(pred_values, THRESHOLDS)]
    label_names = ["Heart Disease", "Stroke", "Diabetes"]

    st.markdown(
        "<h2 style='text-align:center; margin-top: 10px;'>Hasil Prediksi</h2><br>", 
        unsafe_allow_html=True
    )

    for i, label in enumerate(label_names):
        if hasil[i]:
            st.markdown(
                f"""
                <div style='
                    background:linear-gradient(120deg,#fff3e9 90%,#ffecd2 100%);
                    border-radius:15px;
                    padding:30px 20px 25px 20px;
                    margin-bottom:24px;
                    box-shadow:0 2px 16px 0 rgba(255,145,77,0.10);
                    border:2px solid #ff914d;
                    text-align:center;
                '>
                    <h2 style='color:#ff914d; font-size:2.2em; margin-bottom:16px; letter-spacing:1px;'>
                        {label}: <b>Positif</b>
                    </h2>
                    <span style='font-size:2.2em; color:#5a2600; font-weight:700; background:#ffeedf; border-radius:12px; padding:5px 18px;'>
                        {pred_values[i]*100:.1f}%
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div style='
                    background:linear-gradient(120deg,#f5f3fa 90%,#efeafc 100%);
                    border-radius:15px;
                    padding:30px 20px 25px 20px;
                    margin-bottom:24px;
                    box-shadow:0 2px 16px 0 rgba(123,93,219,0.07);
                    border:2px solid #7b5ddb;
                    text-align:center;
                '>
                    <h2 style='color:#7b5ddb; font-size:2.2em; margin-bottom:16px; letter-spacing:1px;'>
                        {label}: <b>Negatif</b>
                    </h2>
                    <span style='font-size:2.2em; color:#392d63; font-weight:700; background:#edeafd; border-radius:12px; padding:5px 18px;'>
                        {pred_values[i]*100:.1f}%
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )
