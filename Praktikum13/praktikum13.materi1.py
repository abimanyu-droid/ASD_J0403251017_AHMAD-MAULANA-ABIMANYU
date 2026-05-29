# Nama  : Ahmad Maulana Abimanyu
# NIM   : J0403251017
# Kelas : TPLA2
# Praktikum 13 - Graph III: Spanning Tree

# ===========================================================
# Praktikum13.materi1.py - Bagian 6.3
# Implementasi Sederhana Algoritma Kruskal
# ===========================================================

# Daftar edge: (bobot, node1, node2)
# Setiap tuple berisi: bobot edge, node asal, node tujuan
edges = [
    (1, 'C', 'D'),   # edge C-D dengan bobot 1 (paling kecil)
    (2, 'A', 'C'),   # edge A-C dengan bobot 2
    (3, 'B', 'D'),   # edge B-D dengan bobot 3
    (4, 'A', 'B'),   # edge A-B dengan bobot 4
    (5, 'A', 'D'),   # edge A-D dengan bobot 5 (paling besar)
]

# Mengurutkan edge berdasarkan bobot terkecil ke terbesar
# Kruskal selalu mulai dari edge yang paling murah/ringan
edges.sort()

mst = []          # list kosong untuk menyimpan edge-edge yang masuk MST
total_weight = 0  # variabel untuk menghitung total bobot MST

# Set kosong untuk mencatat node mana saja yang sudah terhubung
# Set dipakai karena pencarian lebih cepat dibanding list
connected = set()

# Proses setiap edge dari yang bobotnya paling kecil
for weight, u, v in edges:

    # Cek apakah edge ini aman diambil (tidak membentuk cycle)
    # Aman jika minimal salah satu node-nya belum ada di 'connected'
    # Jika keduanya sudah ada, berarti sudah terhubung -> skip
    if u not in connected or v not in connected:

        mst.append((u, v, weight))   # tambahkan edge ini ke MST
        total_weight += weight       # tambahkan bobotnya ke total

        connected.add(u)  # tandai node u sudah masuk MST
        connected.add(v)  # tandai node v sudah masuk MST

# Tampilkan semua edge yang terpilih dalam MST
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

# Tampilkan total bobot seluruh edge MST
print("Total bobot =", total_weight)
