Harga_barang = int(input("Masukan harga barang: "))
Jumlah_barang = int(input("Masukan jumlah barang: "))

def hitung_total_belanja(harga_barang):
    total = sum(harga_barang)
    
    if total >= 100000:
        diskon = 0.10 * total
    else:
        diskon = 0

    pajak = 0.11 * (total - diskon)
    total_bayar = total - diskon + pajak

    return total, diskon, pajak, total_bayar


# Contoh data


total, diskon, pajak, bayar = hitung_total_belanja(barang)

print("Total Belanja :", total)
print("Diskon        :", diskon)
print("Pajak         :", pajak)
print("Total Bayar   :", bayar)
