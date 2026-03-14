import pandas as pd
import random
from datetime import datetime, timedelta

# 1. GENERATE DATA TAMU (Kotor: Nama tidak rapi, ada NULL di email)
def generate_guests(n=50):
    first_names = ['Budi', 'siti', 'agus', 'Rina', 'dwi', 'khansa', 'ben', 'hendra']
    last_names = ['santoso', 'wijaya', 'Putri', 'Pratama', 'ardani', 'lestari']
    cities = ['Bandung', 'Jakarta', 'Surabaya', 'Medan', 'Denpasar']
    
    guests = []
    for i in range(1, n+1):
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        email = f"{name.replace(' ', '').lower()}@email.com" if random.random() > 0.2 else None # 20% NULL email
        guests.append({
            'guest_id': f'G-{i:03d}',
            'guest_name': name, # Nama sengaja berantakan huruf besarnya
            'email': email,
            'city': random.choice(cities)
        })
    return pd.DataFrame(guests)

# 2. GENERATE DATA TRANSAKSI BOOKING
def generate_bookings(guests_df, n=500):
    room_codes = ['STD', 'DLX', 'SUT']
    statuses = ['Checked Out', 'Checked Out', 'Checked Out', 'Canceled', 'No Show']
    
    bookings = []
    start_date = datetime(2025, 1, 1)
    
    for i in range(1, n+1):
        guest_id = random.choice(guests_df['guest_id'].tolist())
        room = random.choice(room_codes)
        status = random.choice(statuses)
        
        # Harga acak berdasarkan tipe kamar
        if room == 'STD': price = random.randint(300, 500) * 1000
        elif room == 'DLX': price = random.randint(600, 900) * 1000
        else: price = random.randint(1200, 2000) * 1000
        
        # Tanggal booking acak
        days_offset = random.randint(0, 300)
        b_date = start_date + timedelta(days=days_offset)
        
        bookings.append({
            'booking_id': f'BK-{i:04d}',
            'guest_id': guest_id,
            'room_code': room,
            'booking_date': b_date.strftime('%Y-%m-%d'),
            'status': status,
            'amount': price
        })
    return pd.DataFrame(bookings)

# Eksekusi dan Simpan ke CSV
print("Mulai membuat data simulasi...")
df_guests = generate_guests(100)
df_bookings = generate_bookings(df_guests, 1000)

df_guests.to_csv('raw_guests.csv', index=False)
df_bookings.to_csv('raw_bookings.csv', index=False)
print("Selesai! File raw_guests.csv dan raw_bookings.csv telah dibuat.")