# Nama  : Ahmad Maulana Abimanyu
# NIM   : J0403251017
# Kelas : TPLA2
# Praktikum 13 - Graph III: Spanning Tree

# ===========================================================
# Latihan 2 - Implementasi Sederhana Algoritma Kruskal
# ===========================================================


# Daftar edge dalam format: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),  # edge C-D dengan bobot 1
    (2, 'A', 'C'),  # edge A-C dengan bobot 2
    (3, 'B', 'D'),  # edge B-D dengan bobot 3
    (4, 'A', 'B'),  # edge A-B dengan bobot 4
    (5, 'A', 'D'),  # edge A-D dengan bobot 5
]

# Langkah 1: Urutkan edge berdasarkan bobot terkecil
# Python sort() pada tuple akan membandingkan elemen pertama (bobot)
edges.sort()

mst = []          # daftar edge yang terpilih untuk MST
total_weight = 0  # akumulasi total bobot MST

# Set untuk melacak node yang sudah masuk ke MST
# (implementasi sederhana pendeteksi cycle)
connected = set()

print("=" * 50)
print("Proses Pemilihan Edge (Algoritma Kruskal):")
print("=" * 50)

# Langkah 2-6: Iterasi setiap edge dari bobot terkecil
for weight, u, v in edges:
    # Cek apakah edge ini akan membentuk cycle sederhana:
    # Edge aman diambil jika minimal salah satu node-nya
    # belum ada di 'connected' (belum terhubung ke MST)
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)
        print(f"  Pilih edge ({u}-{v}, bobot={weight}) -> DIAMBIL")
    else:
        # Kedua node sudah terhubung -> akan membentuk cycle
        print(f"  Skip edge ({u}-{v}, bobot={weight}) -> DIABAIKAN (cycle)")

# Menampilkan hasil MST
print("\n" + "=" * 50)
print("Minimum Spanning Tree (hasil Kruskal):")
print("=" * 50)
for edge in mst:
    print(f"  {edge[0]} -- {edge[1]}  (bobot: {edge[2]})")

print(f"\nTotal bobot MST = {total_weight}")
print(f"Jumlah edge MST = {len(mst)}")

# ===========================================================
# Jawaban Analisis:
# ===========================================================
# 1. Edge mana yang dipilih pertama kali?
#    Edge C-D dengan bobot 1 dipilih pertama karena memiliki
#    bobot terkecil dari semua edge setelah diurutkan. Kruskal
#    selalu memulai dari edge berbobot paling ringan.
#
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
#    Karena tujuan MST adalah meminimalkan total bobot. Dengan
#    selalu memilih edge terkecil yang tersedia (greedy approach),
#    kita memastikan setiap penambahan edge memberikan kontribusi
#    bobot seminimal mungkin ke total akhir. Ini adalah inti
#    strategi greedy pada algoritma Kruskal.
#
# 3. Berapa total bobot MST yang dihasilkan?
#    Total bobot MST = 1 + 2 + 3 = 6
#    (edge C-D=1, A-C=2, B-D=3)
#
# 4. Mengapa edge tertentu tidak dipilih?
#    Edge A-B (bobot 4) dan A-D (bobot 5) tidak dipilih karena
#    ketika giliran mereka diproses, kedua node pada masing-masing
#    edge tersebut sudah masuk ke dalam 'connected' set. Memilih
#    edge-edge itu akan membentuk cycle pada MST yang sudah ada.
#    Sebagai contoh: jika A-B dipilih padahal A sudah terhubung
#    ke C-D melalui A-C dan B sudah terhubung via B-D, maka
#    akan terbentuk lingkaran A-C-D-B-A.
