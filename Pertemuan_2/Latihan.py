#=========================================================
#Praktikum 2 : Konsep ADT dan FILE Handling (STUFI KASUS)
#Latihan 2 : Membuat Fungsi Load Data
#=========================================================

#Variabel menyimpan data
nama_file = "data_mahasiswa.txt"

def baca_data(nama_file):
    data_dict = {} #Inisialisasi data dictionary
    with open (nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip() #Ambil data per baris dan hilangkan new line
            nim, nama, nilai = baris.split(",") # Ambil data per item data
            data_dict[nim] = {"nama": nama, "nilai": int(nilai)} # Masukan dalam dictionary 
    return data_dict
#buka_data = baca_data(nama_file) #Memanggil fungsi load
#print("Jumlah data terbaca", len(buka_data)) #Melihat berapa data yang di load


#=========================================================
#Praktikum 2 : Konsep ADT dan FILE Handling (STUFI KASUS)
#Latihan 2 : Membuat Fungsi Menampilkan Data
#=========================================================

def tampilkan_data(data_dict):
    #Membuat header tabel
    print("\n=== Daftar Mahasiswa ===")
    print(f"{'NIM' : <10} | {'Nama' : <12} | {'Nilai' :>5}")
    '''
    untuk tampilan yang rapu, atur lebar kolom
    {'NIM : <10} artinya nim rata kiri dengan lebar kolom 10 karakter
    {'Nama' : < 12} artinya nama rata kiri dengan lebar kolom 12 karakter
    {'Nilai' : > 5} artinya nama rata kanan dengan lebar kolom 5 karakter
    '''
    print("-"*32) #Membuat garis

    #menampilkan isi datanya
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim:<10} | {nama:<12} | {int(nilai):>5}")

#tampilkan_data(buka_data) #Memanggil fungsi untuk menampilkan data


#=========================================================
#Praktikum 2 : Konsep ADT dan FILE Handling (STUFI KASUS)
#Latihan 3 : Membuat Fungsi Mencari Data
#=========================================================

#Membuat fungsi pencarian data
def cari_data(data_dict):
    #pencarian data berdasarkan nim sebagai key dictionary 
    #membuat input nim mahasiswa yang akan dicari
    nim_cari = input("Masukan NIM mahasiswa yang ingin dicari: ").strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("===== Data Mahasiswa Ditemukan =====")
        print(f"NIM   : {nim_cari}")
        print(f"nama    : {nama}")
        print(f"Nilai   : {nilai}")
    else:
        print("Data tidak ditemukan. Pastikan NIM yang dimasukan benar")

    #Memanggil fungsi data cari
    #cari_data(buka_data)


#=========================================================
#Praktikum 2 : Konsep ADT dan FILE Handling (STUFI KASUS)
#Latihan 4 : Membuat Fungsi Update Data
#=========================================================

#Membuat fungsi update data
def ubah_data(data_dict):

    #Awali dulu dengan mencari nim / data mahasiswa yang ingin di update
    nim = input("Masukan NIM mahasiswa yang ingin diubah datanya: ").strip()

    if nim not in data_dict:
        print("NIM tidak ditemukan. Update dibatalkan")
        return
    try:
        nilai_baru =int(input("Masukan nilai baru 0-100: ").strip())
    except ValueError:
        print("Nilai harus berupa angka. Update dibatalkan")

        if nilai_baru < 0 or nilai_baru > 100:
            print("Nilai harus angka 0 sampai 100. Update dibatalkan")

    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Update berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

#memanggil fungsi ubah data
#ubah_data(buka_data)

#=========================================================
#Praktikum 2 : Konsep ADT dan FILE Handling (STUFI KASUS)
#Latihan 5 : Membuat Fungsi Menyimpan Data Pada File
#=========================================================

#membuat fungsi menyimpan data ke file
def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")

#menanggil fungsi simpan data
#simpan_data(nama_file,buka_data)
#print("\nData berhasil disimpan ke file: ", nama_file)

#=========================================================
#Praktikum 2 : Konsep ADT dan FILE Handling (STUFI KASUS)
#Latihan 6 : Membuat Menu Interaktif
#=========================================================

def main():
    #load data otomatis saat program dimulai
    buka_data = baca_data(nama_file) #

    while True:
        print("\n===MENU DATA MAHASISWA===")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Mahasiswa")
        print("3. Ubah Nilai Mahasiswa")
        print("4. Simpan Data Mahasiswa")
        print("0. Keluar Program")
        
        pilihan = input("Pilih Menu: ").strip()

        if pilihan == "1":
            tampilkan_data(buka_data) #memanggil fs 2 menampilkan data

        elif pilihan == "2":
            cari_data(buka_data) #memanggil fs 3 mencari data

        elif pilihan == "3":
            ubah_data(buka_data) #memanggil fs 4 mengubah data

        elif pilihan == "4":
            simpan_data(nama_file, buka_data) #memanggil fs 5 menyimpan data
            print("Data berhasil disimpan")

        elif pilihan == "0":
            print("Program Selesai. Terima kasih!") #mengakhiri program
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.") #validasi inputan menu

if __name__ == "__main__":
    main()