# ========================================================== 
# Nama    : Ahmad Maulana Abimanyu
# NIM     : J0403251017
# Kelas   : A2
# ==========================================================
# Latihan 3: Mencari Nilai Maksimum 
# ========================================================== 

# Definisi fungsi dengan parameter list 'data' dan penanda posisi 'index' 
def cari_maks(data, index=0): 
    
    # Blok Base Case: Berhenti saat index mencapai elemen terakhir list
    # Elemen terakhir dianggap sebagai nilai maksimum sementara untuk dibandingkan
    # Base case 
    if index == len(data) - 1: 
        return data[index] 
    
    # Blok Recursive Case: Mencari nilai maksimum di sisa list (sebelah kanan)
    # Fungsi terus memanggil dirinya sendiri sampai mencapai elemen terakhir
    # Recursive case 
    maks_sisa = cari_maks(data, index + 1) 
    
    # Blok Perbandingan: Membandingkan elemen saat ini dengan hasil rekursi
    # Jika angka saat ini lebih besar dari pemenang sisa list, kembalikan angka saat ini
    if data[index] > maks_sisa: 
        return data[index] 
    else: 
        # Jika tidak, teruskan nilai maksimum yang sudah ditemukan sebelumnya
        return maks_sisa 

# Blok Eksekusi: Mencari angka terbesar dalam list [3, 7, 2, 9, 5]    
angka = [3, 7, 2, 9, 5] 
print("Nilai maksimum:", cari_maks(angka))

# ALUR PROGRAM:
# Program bekerja dengan cara menelusuri list hingga ke ujung akhir sebelum melakukan 
# perbandingan apa pun. Pada setiap langkah, fungsi "bertanya" ke elemen di sebelahnya, 
# "Siapa yang paling besar di antara kalian semua?". Pertanyaan ini diteruskan sampai ke 
# elemen terakhir. Setelah elemen terakhir menjawab, proses perbandingan dilakukan saat 
# fungsi kembali naik (fase unwinding).

# base case:
# Base case pada program ini adalah if index == len(data) - 1. Kondisi ini terjadi ketika 
# fungsi sampai pada elemen terakhir dalam list. Pada titik ini, tidak ada lagi elemen di 
# sebelah kanan untuk dibandingkan, sehingga fungsi mulai mengembalikan nilai untuk dibandingkan 
# dengan elemen sebelumnya.

# Recursive call:
# Recursive call terjadi pada baris maks_sisa = cari_maks(data, index + 1). Di sini, fungsi memecah 
# masalah besar (mencari maksimum dari 5 angka) menjadi masalah yang lebih kecil 
# (mencari maksimum dari 4 angka, lalu 3 angka, dan seterusnya). Variabel maks_sisa bertindak sebagai 
# penyimpan hasil "pertandingan" dari elemen-elemen yang berada di indeks lebih tinggi.