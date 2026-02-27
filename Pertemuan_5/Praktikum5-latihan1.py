# ========================================================== 
# Nama    : Ahmad Maulana Abimanyu
# NIM     : J0403251017
# Kelas   : A2
# ==========================================================
# Latihan 1: Rekursi Pangkat 
# ========================================================== 

# Definisi fungsi pangkat dengan parameter a (basis) dan n (eksponen/pangkat)
def pangkat(a, n): 
    
    # Blok Base Case: Kondisi berhenti paling dasar
    # Setiap bilangan yang dipangkatkan 0 hasilnya adalah 1
    # Tanpa ini, n akan terus berkurang menjadi negatif dan menyebabkan error
    # Base case 
    if n == 0: 
        return 1 
    
    # Blok Recursive Case (Recursive Call): Memecah masalah menjadi lebih kecil
    # Menghitung a^n dengan cara mengalikan a dengan hasil dari a^(n-1)
    # Fungsi memanggil dirinya sendiri dengan nilai n yang terus berkurang
    # Recursive case 
    return a * pangkat(a, n - 1) 

# Blok Eksekusi: Menghitung 2 pangkat 4 (2^4)
# Proses: 2 * (2 * (2 * (2 * 1))) = 16
print(pangkat(2, 4)) # Output: 16

# ALUR PROGRAM:
# Program ini berjalan dalam dua fase utama: 
# 1. Fase Ekspansi (Stacking): Program memecah $2^4$ menjadi $2 \times 2^3$. Namun, karena program 
# belum tahu hasil $2^3$, ia menunda perkalian tersebut dan memanggil fungsi kembali untuk menghitung 
# $2^3$. Hal ini terus berlanjut ($2 \times 2^2$, lalu $2 \times 2^1$) hingga mencapai pangkat 0. 
# Semua operasi perkalian ini "antre" di dalam memori (call stack). 
# 2. Fase Akumulasi (Unwinding): Setelah mencapai pangkat 0 dan mendapatkan angka 1, program mulai 
# menyelesaikan antrean perkalian dari bawah ke atas. Hasil 1 dikalikan 2, lalu hasilnya dikalikan 2 lagi, 
# hingga kembali ke pemanggilan awal dan menghasilkan 16.


# Base Case (Kondisi Berhenti):
# if n == 0: return 1 
# Base case adalah jangkar atau titik henti rekursi. Tanpa baris ini, fungsi akan terus memanggil dirinya sendiri 
# dengan nilai $n$ yang menjadi negatif ($-1, -2, \dots$) tanpa henti hingga program crash (stack overflow). 
# Dalam logika matematika, kita menggunakan $n = 0$ sebagai pemberhentian karena bilangan apa pun (kecuali nol) 
# yang dipangkatkan 0 hasilnya adalah 1. 


# Recursive Call (Pemanggilan Rekursif):
# return a * pangkat(a, n - 1) 
# Recursive call adalah baris di mana fungsi memanggil dirinya sendiri. Di sini terjadi proses pengecilan masalah. 
# Setiap kali dipanggil, nilai $n$ dikurangi 1 (n - 1). Ini memastikan bahwa setiap langkah membawa kita lebih dekat 
# ke base case. Fungsi "mempercayakan" perhitungan sisa pangkatnya ke pemanggilan berikutnya, lalu mengalikan 
# hasilnya dengan basis a.
