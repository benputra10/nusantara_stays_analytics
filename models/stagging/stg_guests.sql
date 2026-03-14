SELECT
    guest_id,
    -- merapikan nama: huruf pertama besar sisanya kecil
    CONCAT(UPPER(SUBSTRING(guest_name, 1, 1)), LOWER(SUBSTRING(guest_name, 2))) AS nama_tamu,
    -- mengganti null email
    COALESCE(email, 'TIDAK ADA EMAIL') as email_kontak,
    city as kota_asal
FROM nusantara_stays.raw_guests