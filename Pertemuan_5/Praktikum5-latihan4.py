# ========================================================== 
# Nama    : Ahmad Maulana Abimanyu
# NIM     : J0403251017
# Kelas   : A2
# ==========================================================
# Latihan 4: Kombinasi Huruf 
# ========================================================== 

# Definisi fungsi kombinasi dengan n sebagai panjang target dan hasil sebagai string sementara
def kombinasi(n, hasil=""): 
    
    # Blok Base Case: Jika panjang string 'hasil' sudah sama dengan n
    # Program mencetak kombinasi yang terbentuk lalu kembali (backtrack) ke persimpangan sebelumnya
    if len(hasil) == n: 
        print(hasil) 
        return 
    
    # Blok Choose + Explore (Pilihan A): 
    # Menambahkan karakter 'A' ke hasil dan masuk lebih dalam ke rekursi
    kombinasi(n, hasil + "A") 

    # Blok Choose + Explore (Pilihan B): 
    # Menambahkan karakter 'B' ke hasil setelah eksplorasi pilihan A selesai
    kombinasi(n, hasil + "B") 

# Blok Eksekusi: Membuat kombinasi dengan panjang 2
# Output yang dihasilkan: AA, AB, BA, BB    
kombinasi(2)

# Jumlah total kombinasi yang dihasilkan ditentukan oleh jumlah pilihan karakter 
# pada setiap langkah dan kedalaman rekursinya (nilai $n$).

# 1. Rumus Matematika
# Secara matematis, ini adalah masalah Permutasi dengan Pengulangan. Jika kita 
# memiliki $k$ pilihan karakter (dalam hal ini 2, yaitu 'A' dan 'B') dan kita ingin 
# membentuk string sepanjang $n$, maka total kombinasinya adalah:
# $$Total = k^n$$

# 2. Analisis Kasus n = 2
# Kita memiliki 2 pilihan (A atau B).
# Kita melakukan 2 tingkatan pemilihan ($n = 2$).
# Maka: $2^2 = 4$ kombinasi (AA, AB, BA, BB).

# 3. Analisis Kasus n = 3
# Jika fungsi dipanggil dengan kombinasi(3), maka pohon keputusan akan bertambah satu tingkat lagi:
# Maka: $2^3 = 8$ kombinasi (AAA, AAB, ABA, ABB, BAA, BAB, BBA, BBB).

# Kesimpulan:
# Setiap kali nilai $n$ bertambah satu, jumlah output akan berlipat ganda karena setiap kombinasi 
# sebelumnya akan bercabang menjadi dua pilihan baru ('A' dan 'B'). Hal ini menunjukkan bahwa algoritma 
# ini memiliki kompleksitas eksponensial, yang berarti waktu eksekusinya akan meningkat sangat cepat seiring 
# bertambahnya $n$.