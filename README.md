# Proyek Prediksi Penyakit Kronis

Proyek ini bertujuan untuk membangun model prediksi untuk beberapa penyakit kronis berdasarkan dataset yang diberikan. Model yang digunakan adalah Multi-output Neural Network (MNN) yang dibangun menggunakan TensorFlow.

## Daftar Isi

* [Pengantar](#pengantar)
* [Dataset](#dataset)
* [Struktur Proyek](#struktur-proyek)
* [Instalasi](#instalasi)
* [Cara Menjalankan](#cara-menjalankan)
* [Hasil dan Analisis](#hasil-dan-analisis)
* [Lisensi](#lisensi)
* [Kontributor](#kontributor)

## Pengantar

Penyakit kronis merupakan masalah kesehatan global yang memerlukan deteksi dini dan manajemen yang efektif. Proyek ini berfokus pada pengembangan model pembelajaran mesin yang dapat memprediksi risiko penyakit kronis tertentu (misalnya, diabetes, penyakit jantung, dan stroke) berdasarkan fitur-fitur kesehatan yang relevan.

## Dataset

Dataset yang digunakan dalam proyek ini diharapkan berisi fitur-fitur yang relevan untuk prediksi penyakit kronis, seperti data demografi, riwayat kesehatan, dll.

* **Nama File Dataset:** `heart_disease_health_indicators_BRFSS2015.csv`)
* **Format:** CSV
* **Kolom Target:** (Misalnya: `Diabetes`, `Penyakit Jantung`, `Stroke`)

## Struktur Proyek

├── Prediksi_Penyakit_Kronis.ipynb

├── requirements.txt

└── README.md

└── dashboard_inferensi_Streamlit.py

└── mnn5.keras

└── heart_disease_health_indicators_BRFSS2015.csv


* `Prediksi_Penyakit_Kronis.ipynb`: Notebook Jupyter yang berisi semua kode untuk pra-pemrosesan data, pembangunan model, pelatihan, evaluasi, dan visualisasi.
* `requirements.txt`: Daftar semua dependensi Python yang diperlukan untuk menjalankan proyek ini.
* `README.md`: Berkas penjelasan proyek ini.

## Instalasi

Untuk menjalankan notebook ini, Anda perlu menginstal dependensi Python yang tercantum dalam `requirements.txt`.

1.  **Kloning repositori (jika ini adalah repositori Git):**
    ```bash
    git clone <URL_REPO_ANDA>
    cd <NAMA_FOLDER_REPO>
    ```

2.  **Buat lingkungan virtual (direkomendasikan):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    # venv\Scripts\activate  # Windows
    ```

3.  **Instal dependensi:**
    ```bash
    pip install -r requirements.txt
    ```

## Cara Menjalankan

1.  **Pastikan Anda telah menginstal semua dependensi** seperti yang dijelaskan di bagian [Instalasi](#instalasi).
2.  **Pastikan file dataset** (jika ada, misalnya `data_penyakit_kronis.csv`) berada di lokasi yang benar seperti yang diharapkan oleh notebook, atau unggah jika Anda menjalankannya di lingkungan seperti Google Colab.
3.  **Buka notebook Jupyter:**
    ```bash
    jupyter notebook Prediksi_Penyakit_Kronis.ipynb
    ```
4.  **Jalankan setiap sel** di dalam notebook secara berurutan. Notebook akan melakukan hal-hal berikut:
    * Memuat dan membersihkan data.
    * Melakukan pra-pemrosesan fitur (normalisasi/standardisasi).
    * Membangun dan melatih model ANN untuk setiap kolom target penyakit.
    * Mengevaluasi kinerja model menggunakan metrik seperti Akurasi, Presisi, Recall, F1-Score, dan ROC AUC.
    * Memvisualisasikan Kurva ROC.

## Hasil dan Analisis

Notebook akan menampilkan hasil evaluasi model untuk setiap penyakit kronis yang diprediksi. Ini akan mencakup:

* **Matriks Konfusi:** Untuk memahami kinerja klasifikasi.
* **Laporan Klasifikasi:** Menampilkan Presisi, Recall, F1-Score, dan Support untuk setiap kelas.
* **Kurva ROC dan AUC:** Menggambarkan kemampuan diskriminasi model.

Anda akan melihat output akurasi dan metrik lainnya untuk set pelatihan dan pengujian.


## Kontributor

1. A001XBM122 – Dewi Kunthi Siswati Suryo – IPB University
2. A001XBM196 – Halida Fiadnin – IPB University
3. A001XBM223 – Illinia Malika Putri – IPB University
4. A001YBM349 – Muhammad Rizky Fajar – IPB University

