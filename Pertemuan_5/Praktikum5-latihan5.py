# ========================================================== 
# Nama    : Ahmad Maulana Abimanyu
# NIM     : J0403251017
# Kelas   : A2
# ==========================================================
# Studi Kasus: Generator PIN 
# ==========================================================

# Definisi fungsi untuk membuat PIN dengan panjang tertentu
def buat_pin(panjang, hasil=""): 
    
    # Blok Base Case: Jika panjang PIN yang disusun sudah sesuai target
    # Cetak hasilnya dan lakukan backtrack untuk mencoba angka lain
    if len(hasil) == panjang: 
        print("PIN:", hasil) 
        return 
    
    # Blok Loop Choose + Explore: Mencoba setiap angka dari list pilihan
    # Loop ini akan mengeksekusi rekursi untuk angka "0", kemudian "1", lalu "2"
    for angka in ["0", "1", "2"]: 
        # Fungsi memanggil dirinya sendiri dengan menambahkan angka terpilih
        buat_pin(panjang, hasil + angka) 

# Blok Eksekusi: Menghasilkan PIN 3 digit (Total kombinasi: 3^3 = 27)        
buat_pin(3)

# Pada kode di atas, angka yang sama bisa muncul berulang (seperti "000" atau "112") 
# karena setiap tingkat rekursi selalu memulai perulangan dari list angka yang lengkap ["0", "1", "2"].

# Untuk mencegah angka yang sama muncul kembali dalam satu kombinasi (permutasi tanpa pengulangan), 
# kita perlu melakukan pengecekan kondisi sebelum melangkah lebih jauh (pruning sederhana).
# Cara Modifikasinya:
# Kita cukup menambahkan syarat if angka not in hasil sebelum melakukan pemanggilan rekursif.

# Penjelasan Alur Angka Unik:
# 1. Pilih: Program mencoba angka "0".
# 2. Cek: Apakah "0" sudah ada di hasil? Jika belum, lanjut.
# 3. Explore: Pindah ke digit kedua. Saat mencoba memilih "0" lagi, 
# syarat if angka not in hasil akan bernilai False, sehingga program akan melewati angka 
# tersebut dan langsung mencoba "1".
# 4. Hasil Akhir: Kombinasi seperti "001" tidak akan pernah tercetak, hanya kombinasi unik 
# seperti "012", "021", "102", dan seterusnya.

# Dengan cara ini, jumlah total kemungkinan akan berkurang dari $3^3 = 27$ menjadi $3! = 6$ 
# kemungkinan saja.