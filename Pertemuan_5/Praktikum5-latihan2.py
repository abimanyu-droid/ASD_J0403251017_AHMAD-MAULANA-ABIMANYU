# ========================================================== 
# Latihan 2: Tracing Rekursi 
# ==========================================================

# Definisi fungsi untuk melacak alur eksekusi rekursi
def countdown(n): 
    
    # Blok Base Case: Syarat berhenti saat n mencapai 0
    # Jika terpenuhi, fungsi akan berhenti turun dan mulai "naik" kembali
    if n == 0: 
        print("Selesai") 
        return 
    
    # Blok Pre-Recursive (Fase Masuk/Stacking): 
    # Mencetak angka sebelum fungsi memanggil dirinya sendiri (bergerak ke dalam)
    print("Masuk:", n) 
    
    # Blok Pemanggilan Rekursif: Menunda sisa perintah di bawahnya
    # Program akan "diam" di baris ini dan membuka instance fungsi baru untuk n - 1
    countdown(n - 1) 
    
    # Blok Post-Recursive (Fase Keluar/Unwinding):
    # Mencetak angka setelah fungsi di atasnya selesai (bergerak keluar/kembali)
    print("Keluar:", n) 
    
# Blok Eksekusi: Memanggil fungsi dengan nilai awal 3    
countdown(3)

# Alasan utamanya adalah prinsip LIFO (Last In, First Out) pada Call Stack. 
# Bayangkan sebuah tumpukan piring: piring terakhir yang kamu letakkan di atas 
# adalah yang pertama harus kamu ambil agar bisa mencapai piring di bawahnya.