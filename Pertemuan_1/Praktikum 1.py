#=========================================================
#Praktikum 1 : Konsep ADT dan FILE Handling
#Pelatihan Dasar 1 : Membaca seluruh isi file data
#=========================================================


#membuka file semua
print("====Membuka file dalam satu string====")
with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    isi_file = file.read() #mengambil data dan menyimpan semua data dalam 1 variabel
print(isi_file)

#Mengetahui tipe data file
print("Tipe Data :",type(isi_file))

print("")
print("=======================")
print("")

#-----------------------------------
# Praktikum 1 : Konsep ADT dan File Handling 
# Lat Dasar 2 : Membaca Pasing Data
#-----------------------------------

#membuka data per baris
print("====Membuka file per baris====")
jumlah_baris = 0
with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip() #menghilangkan karakter spesial seperti \n pada akhir baris
        print("Baris ke-", jumlah_baris)
        print("Isinya :", baris)

#parsing data baris menadi data satuan dan menampilkannya dalam bentuk kolom2 data
print("====Parsing data per baris====")
with open("data_mahasiswa.txt","r",encoding=("utf-8")) as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter baris baru
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan dan simpan ke variabel
        print("|NIM :", nim, "|nama :", nama, "|Nilai :", nilai) #menampilkan satuan data satuan dan simpan ke variabel

print("")
print("=======================")
print("")

#-----------------------------------
# Praktikum 1 : Konsep ADT dan File Handling 
# Lat Dasar 3 : Membaca data dan menyimpan nya ke data list
#-----------------------------------

data_list = []#inisialisasi list kosong untuk menampung data mahasiswa

with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter baris baru
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan dan simpan ke variabel
        data_list.append([nim,nama,int(nilai)]) #memasukkan data ke list
print("====Menampilkan data dalam list====")
print(data_list)
print("Contoh record ke 1", data_list[0]) #menampilkan record pertama
print("Contoh record ke 1", data_list[1]) #menampilkan record kedua
print("jumlah record :", len(data_list)) #menampilkan jumlah record dalam list

print("")
print("=======================")
print("")

#=========================================================
#Praktikum 1 : Konsep ADT dan FILE Handling
#Pelatihan Dasar 4 : Membaca data dan menyimpannya ke struktur data dictionary
#=========================================================

data_dict = {} #inisialisasi dictionary kosong untuk menampung data mahasiswa
with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter baris baru
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan dan simpan ke variabel
        #simpan data dalam dictionary (key, value)
        data_dict[nim] = {
            "nama": nama,
            "nilai": int(nilai)
        }
print("====Menampilkan data  dictionary====")
print(data_dict)