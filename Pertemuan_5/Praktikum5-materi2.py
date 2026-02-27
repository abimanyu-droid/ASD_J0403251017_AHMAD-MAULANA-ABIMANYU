# ========================================================== 
# Contoh Rekursi 2: Tracing Masuk/Keluar 
# ========================================================== 

# Fungsi 'hitung' untuk mendemonstrasikan alur tumpukan rekursi (Call Stack)
def hitung(n): 
   
    # Blok Base Case: Kondisi berhenti agar rekursi tidak berjalan selamanya
    # Ketika n mencapai 0, fungsi mencetak pesan dan mulai kembali (backtrack) 
    if n == 0: 
        print("Selesai") 
        return 
    
    # Blok Fase Stacking (Masuk): Menampilkan angka sebelum memanggil fungsi lagi
    # Baris ini dieksekusi saat program bergerak "masuk" lebih dalam ke rekursi
    print("Masuk:", n) # fase stacking 

    # Blok Pemanggilan Rekursif: Memanggil fungsi yang sama dengan nilai n - 1
    # Program akan "tertahan" di baris ini sampai fungsi di dalamnya selesai
    hitung(n - 1) # pemanggilan rekursif 

    # Blok Fase Unwinding (Keluar): Menampilkan angka saat fungsi kembali dari base case
    # Baris ini hanya akan dieksekusi setelah pemanggilan hitung(n - 1) tuntas
    print("Keluar:", n) # fase unwinding 
    
# Blok Eksekusi: Menjalankan fungsi dengan angka awal 3
# Output akan menunjukkan pola simetris (Masuk: 3, 2, 1 -> Selesai -> Keluar: 1, 2, 3)    
hitung(3)