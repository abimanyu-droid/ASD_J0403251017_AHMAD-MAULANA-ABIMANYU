# ========================================================== 
# Nama    : Ahmad Maulana Abimanyu
# NIM     : J0403251017
# Kelas   : A2
# ==========================================================
# Contoh Backtracking 1: Kombinasi Biner (n) 
# ==========================================================

# Definisi fungsi biner dengan parameter n (target panjang) dan hasil (string sementara)
def biner(n, hasil=""): 
    
    # Blok Base Case: Kondisi berhenti saat panjang string sudah mencapai n
    # Jika syarat terpenuhi, cetak kombinasi yang terbentuk dan kembali (backtrack) 
    if len(hasil) == n: 
        print(hasil) 
        return
    
    # Blok Jalur Kiri (Choose + Explore): Mencoba kemungkinan angka '0'
    # Fungsi memanggil dirinya sendiri dengan menambahkan '0' ke variabel hasil
    # Choose + Explore: tambah '0' 
    biner(n, hasil + "0") 
    
    # Blok Jalur Kanan (Choose + Explore): Mencoba kemungkinan angka '1'
    # Setelah jalur '0' selesai (backtrack), program mencoba jalur angka '1'
    # Choose + Explore: tambah '1' 
    biner(n, hasil + "1") 

# Blok Eksekusi: Memulai pencarian kombinasi biner untuk panjang 3
# Akan menghasilkan 8 variasi: 000, 001, 010, 011, 100, 101, 110, 111
biner(3)