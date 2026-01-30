#=========================================================
#Praktikum 1 : Konsep ADT dan FILE Handling
#Pelatihan Dasar 1 : Membaca seluruh isi file data
#=========================================================


#membuka file dalam satu string
print("====Membuka file dalam satu string====")
with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    isi_file = file.read()
print(isi_file)

#Mengetahui tipe data file
print("Tipe Data :",type(isi_file))

#membuka data per baris
print("Membuka file per baris")
jumlah_baris = 0
with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris
        print("Baris ke-", jumlah_baris)
        print("Isinya :", baris)