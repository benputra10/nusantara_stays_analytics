# 🏨 Nusantara Stays: End-to-End Hotel Revenue Analytics Pipeline

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![dbt](https://img.shields.io/badge/dbt-FF694B?style=for-the-badge&logo=dbt&logoColor=white)
![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=Tableau&logoColor=white)

## 📌 Executive Summary
Proyek ini adalah simulasi dunia nyata dari arsitektur analitik perhotelan. Saya merancang *data pipeline* menyeluruh yang dimulai dari pembuatan (*generation*) data mentah menggunakan Python, pemrosesan dan pengujian data berskala menggunakan **dbt (data build tool)** di atas *database* MySQL, hingga perancangan *Executive Dashboard* interaktif di Tableau.

## 🛠️ The Architecture & Workflow
Proyek ini memecahkan masalah umum di industri (data kotor, anomali status pemesanan, dan inefisiensi komputasi) melalui 4 tahapan *Engineering*:

1. **Data Ingestion (Python & MySQL `LOCAL INFILE`)**
   * Mensimulasikan data kotor dari *Property Management System* (PMS) menggunakan modul Python `pandas`.
   * Memanfaatkan `LOAD DATA LOCAL INFILE` di MySQL untuk memasukkan ribuan baris data mentah (`raw_guests`, `raw_bookings`) secara instan ke skema *Development*.
2. **Data Transformation (dbt Staging & Seeds)**
   * **Staging:** Membersihkan inkonsistensi tipografi (Title Casing nama tamu) dan menangani *NULL values* menggunakan fungsi *native* SQL.
   * **Seeds:** Menginjeksi kamus statis (`room_mapping.csv`) ke dalam *database* untuk menerjemahkan kode operasional menjadi nama produk yang ramah bisnis (misal: "DLX" menjadi "Deluxe Room") tanpa perlu *update* ke sistem *Backend*.
3. **Business Logic & Optimization (dbt Marts)**
   * Membangun tabel fakta tunggal (`fct_revenue`).
   * **Surrogate Keys:** Menggunakan `MD5(CONCAT())` untuk membuat ID Pendapatan yang kebal terhadap duplikasi.
   * **Business Filter:** Menerapkan logika hanya memproses tamu berstatus `'Checked Out'` untuk mencegah omzet fiktif dari pembatalan.
   * **Incremental Materialization:** Memprogram dbt agar hanya memproses baris data terbaru, menghemat beban komputasi *server* secara drastis.
4. **Quality Control (dbt Tests)**
   * Menerapkan validasi ketat di `schema.yml` (`not_null`, `unique`, dan `accepted_values`) untuk memblokir data cacat masuk ke lapisan visualisasi.

## 📊 The Executive Dashboard
**🔗 [Live Tableau Dashboard: Nusantara Stays Scorecard]( https://public.tableau.com/app/profile/rizki.ardani/viz/viz1stays/Dashboard1?publish=yes )**

*Dashboard* ini dirancang dengan prinsip visualisasi data eksekutif, menyajikan BANs (*Big Ass Numbers*) untuk metrik finansial utama, tren musiman, komparasi performa tipe kamar, dan peta demografi asal pengunjung sebagai landasan strategi pemasaran tertarget.

## 📂 Repository Structure
* `generate_data.py`: Skrip generator data kotor.
* `raw_guests.csv` & `raw_bookings.csv`: Bahan baku *ingestion*.
* `nusantara_stays/`: Direktori inti proyek dbt (Models, Seeds, YML configurations)
