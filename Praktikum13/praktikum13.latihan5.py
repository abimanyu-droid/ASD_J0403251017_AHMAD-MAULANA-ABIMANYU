# Nama  : Ahmad Maulana Abimanyu
# NIM   : J0403251017
# Kelas : TPLA2
# Praktikum 13 - Graph III: Spanning Tree

# ===========================================================
# Latihan 5 - Tugas Mandiri: MST Kasus Baru
# Kasus 1: Jaringan Jalan Antar Kota
# ===========================================================
# Kasus: Pemerintah ingin membangun jaringan jalan yang
# menghubungkan kota-kota berikut dengan total panjang jalan
# minimum (angka menunjukkan jarak/biaya pembangunan dalam
# satuan tertentu):
#
#   Bogor   - Jakarta = 5
#   Bogor   - Depok   = 2
#   Depok   - Jakarta = 3
#   Jakarta - Bandung = 6
#   Depok   - Bandung = 4
#
# Algoritma yang digunakan: KRUSKAL
# Alasan: graph ini sparse (5 edge, 4 node), Kruskal bekerja
# efisien dengan mengurutkan edge terlebih dahulu.

import heapq

# ===========================================================
# Representasi Weighted Graph - Adjacency Dictionary
# (untuk visualisasi graph dan keperluan traversal)
# ===========================================================
graph_adjacency = {
    'Bogor'   : {'Jakarta': 5, 'Depok': 2},
    'Depok'   : {'Bogor': 2, 'Jakarta': 3, 'Bandung': 4},
    'Jakarta' : {'Bogor': 5, 'Depok': 3, 'Bandung': 6},
    'Bandung' : {'Jakarta': 6, 'Depok': 4},
}

# Representasi edge list untuk Kruskal
# Format: (bobot, kota1, kota2)
edges = [
    (5, 'Bogor',   'Jakarta'),  # jarak/biaya Bogor-Jakarta
    (2, 'Bogor',   'Depok'),    # jarak/biaya Bogor-Depok
    (3, 'Depok',   'Jakarta'),  # jarak/biaya Depok-Jakarta
    (6, 'Jakarta', 'Bandung'),  # jarak/biaya Jakarta-Bandung
    (4, 'Depok',   'Bandung'),  # jarak/biaya Depok-Bandung
]

# ===========================================================
# Tampilkan peta koneksi jalan yang tersedia
# ===========================================================
print("=" * 55)
print("PETA JARINGAN JALAN ANTAR KOTA")
print("=" * 55)
print("Semua rute yang mungkin dibangun:")
# Tampilkan dalam urutan terurut berdasarkan bobot
for bobot, k1, k2 in sorted(edges):
    print(f"  {k1:<10} -- {k2:<10}  : {bobot} satuan")

# ===========================================================
# Implementasi Algoritma Kruskal
# ===========================================================

# Langkah 1: Urutkan semua edge dari bobot terkecil
edges.sort()

mst = []          # ruas jalan yang dipilih untuk dibangun
total_bobot = 0   # total panjang/biaya jalan yang dibangun
connected = set() # kota-kota yang sudah terhubung

print("\n" + "=" * 55)
print("Proses Pemilihan Rute (Algoritma Kruskal):")
print("=" * 55)

# Langkah 2-6: Iterasi edge dari terkecil, cegah cycle
for bobot, k1, k2 in edges:
    # Pilih edge jika minimal satu kota belum terhubung
    if k1 not in connected or k2 not in connected:
        mst.append((k1, k2, bobot))
        total_bobot += bobot
        connected.add(k1)
        connected.add(k2)
        status = "DIPILIH ✓"
    else:
        # Kedua kota sudah terhubung -> memilih edge ini
        # akan membentuk cycle (jalur melingkar)
        status = "DILEWATI ✗ (siklus)"

    print(f"  {k1:<10} -- {k2:<10} ({bobot}) -> {status}")

# ===========================================================
# Output Hasil MST - Jaringan Jalan Minimum
# ===========================================================
print("\n" + "=" * 55)
print("HASIL JARINGAN JALAN MINIMUM (MST):")
print("=" * 55)
print("Ruas jalan yang direkomendasikan untuk dibangun:")
for rute in mst:
    print(f"  {rute[0]:<10} <--> {rute[1]:<10}  : {rute[2]} satuan")

print(f"\nTotal bobot MST (panjang/biaya total) = {total_bobot} satuan")
print(f"Jumlah ruas jalan yang dibangun       = {len(mst)} ruas")
print(f"Jumlah kota yang terhubung            = {len(connected)} kota")

# Verifikasi: untuk N kota, MST harus punya N-1 edge
n_kota = len(graph_adjacency)
print(f"\nVerifikasi: {n_kota} kota -> MST seharusnya {n_kota - 1} edge")
print(f"Hasil     : {len(mst)} edge -> {'VALID ✓' if len(mst) == n_kota - 1 else 'INVALID ✗'}")

# ===========================================================
# Jawaban Analisis:
# ===========================================================
# 1. Kasus apa yang dipilih?
#    Kasus 1: Jaringan Jalan Antar Kota. Pemerintah ingin
#    menghubungkan 4 kota (Bogor, Depok, Jakarta, Bandung)
#    dengan total panjang/biaya jalan yang paling minimum.
#
# 2. Algoritma apa yang digunakan?
#    Algoritma Kruskal. Dipilih karena graph ini bersifat sparse
#    (hanya 5 edge untuk 4 node, rasio edge/node rendah).
#    Kruskal efisien untuk sparse graph karena cukup mengurutkan
#    edge yang jumlahnya sedikit.
#
# 3. Edge mana saja yang dipilih dalam MST?
#    - Bogor   -- Depok    : 2 satuan  (terkecil, dipilih pertama)
#    - Depok   -- Jakarta  : 3 satuan  (menghubungkan Jakarta)
#    - Depok   -- Bandung  : 4 satuan  (menghubungkan Bandung)
#    Ketiga edge ini membentuk MST dengan semua 4 kota terhubung.
#
# 4. Berapa total bobot MST?
#    Total bobot = 2 + 3 + 4 = 9 satuan
#    Ini adalah total minimum yang memungkinkan semua kota
#    terhubung. Tidak ada kombinasi 3 ruas jalan lain yang
#    bisa menghubungkan 4 kota dengan total lebih kecil dari 9.
#
# 5. Mengapa edge tertentu tidak dipilih?
#    - Bogor-Jakarta (5): Saat diproses, Bogor sudah terhubung
#      lewat Bogor-Depok dan Jakarta sudah terhubung lewat
#      Depok-Jakarta. Memilih edge ini membentuk cycle
#      Bogor-Depok-Jakarta-Bogor.
#    - Jakarta-Bandung (6): Saat diproses, Jakarta sudah
#      terhubung dan Bandung sudah terhubung lewat Depok-Bandung.
#      Memilih edge ini membentuk cycle Jakarta-Depok-Bandung-Jakarta.
#    Prinsip MST: setiap kota hanya perlu "dijangkau" satu kali.
#    Koneksi berlebih hanya membuang biaya tanpa manfaat tambahan.
