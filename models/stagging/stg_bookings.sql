SELECT 
    booking_id,
    guest_id,
    room_code,
    CAST(booking_date AS DATE) AS tanggal_booking,
    status AS status_booking,
    CAST(amount AS DECIMAL(10, 2)) AS nominal_transaksi
FROM nusantara_stays.raw_bookings