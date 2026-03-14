{{ config(
    materialized = 'incremental',
    unique_key = 'revenue_id'
)}}

WITH bookings AS (
    SELECT * FROM {{ ref('stg_bookings') }}
),

guests AS (
    SELECT * FROM {{ ref('stg_guests') }}
),

rooms AS (
    SELECT * FROM {{ ref('room_maping') }}
)

SELECT 
    -- membuat id unik gabungan menggunakan native mysql
    MD5(CONCAT_ws('-', b.booking_id, b.tanggal_booking)) AS revenue_id,
    b.booking_id,
    b.tanggal_booking,
    g.nama_tamu,
    g.kota_asal,
    r.room_name as tipe_kamar,
    r.bed_type as tipe_kasur,
    b.nominal_transaksi as pendapatan_bersih

FROM bookings b
LEFT JOIN guests g ON b.guest_id = g.guest_id
LEFT JOIN rooms r ON b.room_code = r.room_code

-- FILTER BISNIS: HANYA AMBIL PENDAPATAN DARI TAMU YANG BENERAN MENGINAP
WHERE b.status_booking = 'Checked Out'

-- LOGIKA INCREMENTAL : jika di jalankan ulang hanya ambil data tanggal terbaru
{% if is_incremental() %}
    AND b.tanggal_booking > (SELECT MAX(tanggal_booking) FROM {{ this}})
{% endif %}