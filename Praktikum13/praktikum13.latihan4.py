# Nama  : Ahmad Maulana Abimanyu
# NIM   : J0403251017
# Kelas : TPLA2
# Praktikum 13 - Graph III: Spanning Tree

# ===========================================================
# Latihan 4 - Studi Kasus: Jaringan Kabel Antar Gedung
# ===========================================================
# Sebuah kampus ingin membangun jaringan kabel internet antar
# gedung dengan biaya minimum. MST digunakan untuk menemukan
# kombinasi koneksi kabel yang menghubungkan semua gedung
# dengan total biaya pemasangan paling murah.
#
# Data hubungan dan biaya kabel antar gedung:
#   GedungA - GedungB = 4 (juta rupiah)
#   GedungA - GedungC = 2
#   GedungB - GedungD = 3
#   GedungC - GedungD = 1
#   GedungA - GedungD = 5
#
# Algoritma yang digunakan: KRUSKAL
# Alasan: jumlah edge sedikit (sparse graph), Kruskal lebih
# mudah diimplementasikan dengan mengurutkan edge terlebih dahulu.

import heapq

# ===========================================================
# Representasi Weighted Graph
# ===========================================================
# Format edge: (bobot/biaya, gedung1, gedung2)
edges = [
    (4, 'GedungA', 'GedungB'),  # biaya pasang kabel A-B = 4 juta
    (2, 'GedungA', 'GedungC'),  # biaya pasang kabel A-C = 2 juta
    (3, 'GedungB', 'GedungD'),  # biaya pasang kabel B-D = 3 juta
    (1, 'GedungC', 'GedungD'),  # biaya pasang kabel C-D = 1 juta
    (5, 'GedungA', 'GedungD'),  # biaya pasang kabel A-D = 5 juta
]

# Tampilkan semua opsi koneksi yang tersedia
print("=" * 55)
print("DATA JARINGAN KABEL KAMPUS")
print("=" * 55)
print("Semua kemungkinan koneksi kabel:")
for biaya, g1, g2 in edges:
    print(f"  {g1} -- {g2}  : Rp {biaya} juta")

# ===========================================================
# Implementasi Algoritma Kruskal
# ===========================================================

# Langkah 1: Urutkan semua edge berdasarkan biaya terkecil
edges.sort()

mst = []          # jalur kabel yang dipilih untuk jaringan
total_biaya = 0   # total biaya minimum pemasangan kabel
connected = set() # gedung-gedung yang sudah masuk jaringan

print("\n" + "=" * 55)
print("Proses Pemilihan Kabel (Algoritma Kruskal):")
print("=" * 55)

# Langkah 2-6: Pilih edge dari bobot terkecil, hindari cycle
for biaya, g1, g2 in edges:
    # Edge dipilih jika minimal satu gedungnya belum terhubung
    # (mencegah terbentuknya cycle pada jaringan)
    if g1 not in connected or g2 not in connected:
        mst.append((g1, g2, biaya))
        total_biaya += biaya
        connected.add(g1)
        connected.add(g2)
        print(f"  ✓ Pasang kabel {g1} -- {g2}  (Rp {biaya} juta) -> DIPILIH")
    else:
        print(f"  ✗ Lewati       {g1} -- {g2}  (Rp {biaya} juta) -> akan membentuk siklus")

# ===========================================================
# Output Hasil MST
# ===========================================================
print("\n" + "=" * 55)
print("HASIL JARINGAN KABEL MINIMUM (MST):")
print("=" * 55)
print("Kabel yang harus dipasang:")
for koneksi in mst:
    print(f"  {koneksi[0]} <--> {koneksi[1]}  : Rp {koneksi[2]} juta")

print(f"\nTotal biaya pemasangan minimum = Rp {total_biaya} juta")
print(f"Jumlah kabel yang dipasang      = {len(mst)} kabel")
print(f"Jumlah gedung yang terhubung    = {len(connected)} gedung")

# ===========================================================
# Jawaban Analisis:
# ===========================================================
# 1. Algoritma apa yang digunakan?
#    Algoritma Kruskal digunakan. Algoritma ini bekerja dengan
#    mengurutkan semua edge berdasarkan bobot terkecil, lalu
#    memilih edge satu per satu dari yang termurah selama tidak
#    membentuk cycle. Pilihan ini cocok karena jumlah edge
#    relatif sedikit (sparse graph - hanya 5 edge untuk 4 gedung).
#
# 2. Edge mana saja yang dipilih?
#    - GedungC -- GedungD  : Rp 1 juta  (termurah, dipilih pertama)
#    - GedungA -- GedungC  : Rp 2 juta  (aman, tidak membentuk cycle)
#    - GedungB -- GedungD  : Rp 3 juta  (aman, menghubungkan GedungB)
#    Edge GedungA-GedungB (4) dan GedungA-GedungD (5) tidak dipilih
#    karena saat diproses, kedua ujung edge sudah terhubung.
#
# 3. Berapa total biaya minimum?
#    Total biaya = 1 + 2 + 3 = Rp 6 juta
#    Ini adalah biaya terendah yang mungkin untuk menghubungkan
#    seluruh 4 gedung tanpa redundansi jalur.
#
# 4. Mengapa MST cocok digunakan pada kasus ini?
#    Kasus jaringan kabel kampus adalah contoh klasik penggunaan MST.
#    Tujuannya adalah menghubungkan SEMUA gedung (seluruh node)
#    tanpa loop/redundansi (tanpa cycle), dengan biaya MINIMUM.
#    MST secara matematis memberikan solusi optimal untuk masalah
#    ini - tidak ada cara lain menghubungkan 4 gedung dengan biaya
#    lebih rendah dari Rp 6 juta menggunakan data yang ada.
