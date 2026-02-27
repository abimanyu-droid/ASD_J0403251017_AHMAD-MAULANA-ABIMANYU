# ========================================================== 
# Contoh Rekursi 3: Menjumlahkan Elemen List
# ==========================================================

# Definisi fungsi dengan parameter 'data' (list) dan 'index' yang dimulai dari 0
def jumlah_list(data, index=0): 
    
    # Blok Base Case: Kondisi berhenti jika index sudah di luar jangkauan list
    # Jika index sama dengan panjang list, kembalikan 0 sebagai nilai netral penjumlahan
    # Base case: jika index sudah mencapai panjang list 
    if index == len(data): 
        return 0 
    
    # Blok Recursive Case: Menambahkan elemen saat ini dengan hasil fungsi berikutnya
    # Baris ini mengambil data[index] lalu memanggil kembali fungsi untuk index + 1
    # Proses ini terus berlanjut sampai semua elemen list "terkunjungi"
    # Recursive case: elemen sekarang + jumlah elemen setelahnya 
    return data[index] + jumlah_list(data, index + 1) 

# Blok Eksekusi: Memanggil fungsi dengan list angka [2, 4, 6, 8]
# Logika akumulasinya: 2 + (4 + (6 + (8 + 0))) = 20
print(jumlah_list([2, 4, 6, 8])) # Output: 20