# Nama  : Ahmad Maulana Abimanyu
# NIM   : J0403251017
# Kelas : TPLA2
# Praktikum 13 - Graph III: Spanning Tree

# ===========================================================
# Latihan 1 
# ===========================================================


# Daftar edge graph awal (semua koneksi yang ada)
# Graph memiliki 4 node: A, B, C, D
edges = [
    ('A', 'B'),  # koneksi A ke B
    ('A', 'C'),  # koneksi A ke C
    ('A', 'D'),  # koneksi A ke D (diagonal)
    ('C', 'D'),  # koneksi C ke D
    ('B', 'D'),  # koneksi B ke D
]

# Contoh spanning tree yang valid
# Spanning tree harus: menghubungkan semua node, tanpa cycle,
# dan memiliki tepat (jumlah_node - 1) = 3 edge
spanning_tree = [
    ('A', 'C'),  # pilih edge A-C
    ('C', 'D'),  # pilih edge C-D
    ('D', 'B'),  # pilih edge D-B
]

# Menampilkan semua edge pada graph awal
print("=" * 40)
print("Edge pada graph awal:")
print("=" * 40)
for edge in edges:
    print(f"  {edge[0]} -- {edge[1]}")

# Menampilkan edge pada spanning tree
print("\nContoh Spanning Tree yang valid:")
print("=" * 40)
for edge in spanning_tree:
    print(f"  {edge[0]} -- {edge[1]}")

# Menampilkan perbandingan jumlah edge
print("\nRingkasan:")
print(f"  Jumlah edge graph awal  = {len(edges)}")
print(f"  Jumlah edge spanning tree = {len(spanning_tree)}")
print(f"  Jumlah node             = 4")
print(f"  Edge spanning tree      = jumlah node - 1 = {4 - 1}")

# ===========================================================
# Jawaban Analisis:
# ===========================================================
# 1. Apa perbedaan graph awal dan spanning tree?
#    Graph awal memiliki 5 edge dan mengandung cycle (misal:
#    A-C-D-A atau A-B-D-A). Spanning tree hanya memiliki 3
#    edge, menghubungkan semua 4 node tanpa membentuk cycle
#    sama sekali. Spanning tree adalah subgraph dari graph awal.
#
# 2. Mengapa spanning tree tidak boleh memiliki cycle?
#    Cycle berarti ada jalur melingkar yang menghubungkan
#    node yang sama lebih dari satu kali. Ini menyebabkan
#    penggunaan edge berlebih, meningkatkan biaya total, dan
#    membuat koneksi tidak efisien. Tujuan spanning tree adalah
#    menghubungkan semua node dengan edge seminimal mungkin.
#
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
#    Untuk menghubungkan N node tanpa cycle, dibutuhkan tepat
#    N-1 edge. Ini adalah properti matematika dari tree:
#    setiap edge menambahkan tepat 1 node baru. Jika ada lebih
#    dari N-1 edge, pasti terbentuk cycle. Pada graph ini,
#    4 node membutuhkan tepat 3 edge pada spanning tree-nya,
#    lebih sedikit dari 5 edge yang ada di graph awal.
