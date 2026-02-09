# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama : Ahmad Maulana Abimanyu
# NIM : J0403251017
# Kelas : A2
# ==========================================================

# -------------------------------
# Konstanta nama file
# -------------------------------
from ast import main


from ast import main


nama_file = "stok_barang.txt"

# -------------------------------
# Fungsi: Membaca data dari file
# -------------------------------

def baca_stok(nama_file):
    stok_dict = {}
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
        # Lewati baris kosong
            if baris == "":
                continue
            data_barang = baris.split(",")   

            kode, nama, stok = data_barang
            try:
                stok_int = int(stok)
            except ValueError:
                continue
            stok_dict[kode] = {"nama": nama, "stok": stok_int}
    return stok_dict

buka_data = baca_stok(nama_file)

# -------------------------------
# Fungsi: Menampilkan semua data
# -------------------------------
def tampilkan_semua(stok_dict):
    print("\n=== Daftar Barang ===")
    print(f"{'Kode' : <8} | {'Nama' : <30} | {'Stok' : >7}")
    print("-"*51)
    for kode in sorted(stok_dict.keys()):
        nama = stok_dict[kode]["nama"]
        stok = stok_dict[kode]["stok"]
        print(f"{kode : <8} | {nama : <30} | {stok : >7}")

    if len(stok_dict) == 0:
        print("Tidak ada data barang tersedia.")

# -------------------------------
# Fungsi: Cari barang berdasarkan kode
# -------------------------------
def cari_barang(stok_dict):
    kode_cari = input("\nMasukkan kode barang yang ingin dicari: ").strip()
    if kode_cari in stok_dict:
        nama = stok_dict[kode_cari]["nama"]
        stok = stok_dict[kode_cari]["stok"]
        print(f"\n===Barang ditemukan===\nKode: {kode_cari}, \nNama: {nama}, \nStok: {stok}")
    else:
        print("Barang dengan kode tersebut tidak ditemukan.")

# -------------------------------
# Fungsi: Tambah barang baru
# -------------------------------
def tambah_barang(stok_dict):
    while True:
        kode = input("\nMasukkan kode barang baru: ").strip()
        if kode in stok_dict:
            print("\nKode barang sudah ada. Gunakan fungsi update stok untuk menambah stok.")
        else:
            break
    nama = input("Masukkan nama barang: ").strip()
    while True:
        try:
            stok = int(input("Masukkan stok awal barang: ").strip())
            break
        except ValueError:
            print("Stok harus berupa angka. Silakan coba lagi.")
    stok_dict[kode] = {"nama": nama, "stok": stok}
    print("\nBarang baru berhasil ditambahkan.")

# -------------------------------
# Fungsi: Update stok barang
# -------------------------------
def update_stok(stok_dict):
    kode = input("\nMasukkan kode barang yang stoknya ingin diupdate: ").strip()
    

    if kode in stok_dict:
        while True:
            try:
                print(f"Nama barang: {stok_dict[kode]['nama']}\n Stok: {stok_dict[kode]['stok']}")
                print("\n=== Update Stok Barang ===\n1. Tambah Stok\n2. Kurangi Stok")
                update_stok = int(input("Pilih opsi: ").strip())
                while True:
                    tambahan_stok = int(input("\nMasukkan jumlah stok yang akan ditambahkan/kurangi: ").strip())
                    if update_stok == 2:
                        tambahan_stok = -tambahan_stok
                    if stok_dict[kode]["stok"] + tambahan_stok < 0:
                        print("Stok tidak bisa negatif. Silakan coba lagi.")
                        continue
                    else:
                        stok_dict[kode]["stok"] += tambahan_stok
                        print("Stok barang berhasil diperbarui.")
                        print(f"Stok baru: {stok_dict[kode]['stok']}")
                        return
            except ValueError:
                print("Jumlah stok harus berupa angka. Silakan coba lagi.")
        
    else:
        print("Barang dengan kode tersebut tidak ditemukan.")

# -------------------------------
# Fungsi: Menyimpan data ke file
# -------------------------------
def simpan_stok(nama_file, stok_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for kode in stok_dict:
            nama = stok_dict[kode]["nama"]
            stok = stok_dict[kode]["stok"]
            file.write(f"{kode},{nama},{stok}\n")
        print("\nData berhasil disimpan.")
# -------------------------------
# Program Utama
# -------------------------------
def main():
 # Membaca data dari file saat program mulai
 stok_barang = baca_stok(nama_file)
 while True:
    print("\n=== MENU STOK KANTIN ===")
    print("1. Tampilkan semua barang")
    print("2. Cari barang berdasarkan kode")
    print("3. Tambah barang baru")
    print("4. Update stok barang")
    print("5. Simpan ke file")
    print("0. Keluar")
    pilihan = input("Pilih menu: ").strip()
    if pilihan == "1":
        tampilkan_semua(stok_barang)
    elif pilihan == "2":
        cari_barang(stok_barang)
    elif pilihan == "3":
        tambah_barang(stok_barang)
    elif pilihan == "4":
        update_stok(stok_barang)
    elif pilihan == "5":
        simpan_stok(nama_file, stok_barang)
    elif pilihan == "0":
        print("\nProgram selesai.")
        break

# Menjalankan program utama
if __name__ == "__main__":
    main()