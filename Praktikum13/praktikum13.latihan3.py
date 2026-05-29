# Nama  : Ahmad Maulana Abimanyu
# NIM   : J0403251017
# Kelas : TPLA2
# Praktikum 13 - Graph III: Spanning Tree

# ===========================================================
# Latihan 3 - Implementasi Algoritma Prim
# ===========================================================


# heapq digunakan sebagai min-heap (priority queue)
# agar selalu mengambil edge dengan bobot terkecil secara efisien

import heapq

# Representasi graph sebagai adjacency dictionary
# Format: graph[node] = {tetangga: bobot, ...}
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},  # A terhubung ke B(4), C(2), D(5)
    'B': {'A': 4, 'D': 3},           # B terhubung ke A(4), D(3)
    'C': {'A': 2, 'D': 1},           # C terhubung ke A(2), D(1)
    'D': {'A': 5, 'B': 3, 'C': 1}   # D terhubung ke A(5), B(3), C(1)
}

def prim(graph, start):
    """
    Fungsi Prim untuk mencari Minimum Spanning Tree.
    Parameter:
        graph : adjacency dict berisi bobot tiap edge
        start : node awal untuk memulai pembangunan MST
    Return:
        mst          : list of tuple (u, v, weight) edge yang terpilih
        total_weight : total bobot MST
    """

    # Set untuk menyimpan node yang sudah masuk MST
    visited = set([start])

    # Priority queue (min-heap) untuk menyimpan kandidat edge
    # Format: (bobot, node_asal, node_tujuan)
    edges = []

    # Masukkan semua edge dari node awal ke priority queue
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []          # edge-edge yang terpilih
    total_weight = 0  # total bobot MST

    print("=" * 50)
    print(f"Mulai dari node: {start}")
    print("Proses Pembangunan MST (Algoritma Prim):")
    print("=" * 50)

    # Terus ambil edge terkecil selama masih ada kandidat
    while edges:
        # Ambil edge dengan bobot terkecil dari heap
        weight, u, v = heapq.heappop(edges)

        # Jika node tujuan belum dikunjungi, tambahkan ke MST
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
            print(f"  Pilih edge ({u}-{v}, bobot={weight}) | Node aktif: {sorted(visited)}")

            # Masukkan semua edge dari node baru ke priority queue
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
        else:
            print(f"  Skip edge ({u}-{v}, bobot={weight}) -> node {v} sudah dikunjungi")

    return mst, total_weight


# Jalankan algoritma Prim mulai dari node 'A'
mst, total = prim(graph, 'A')

# Tampilkan hasil akhir MST
print("\n" + "=" * 50)
print("Minimum Spanning Tree (hasil Prim):")
print("=" * 50)
for edge in mst:
    print(f"  {edge[0]} -- {edge[1]}  (bobot: {edge[2]})")

print(f"\nTotal bobot MST = {total}")
print(f"Jumlah edge MST = {len(mst)}")

# ===========================================================
# Jawaban Analisis:
# ===========================================================
# 1. Node awal apa yang digunakan?
#    Node 'A' digunakan sebagai titik awal. Algoritma Prim dapat
#    dimulai dari node mana saja dan akan menghasilkan MST dengan
#    total bobot yang sama (meskipun urutan pemilihan edge bisa
#    berbeda tergantung node awal).
#
# 2. Edge mana yang dipilih pertama kali?
#    Edge A-C dengan bobot 2 dipilih pertama karena dari node A,
#    edge ke C memiliki bobot terkecil (A-C=2 < A-B=4 < A-D=5).
#
# 3. Bagaimana Prim menentukan edge berikutnya?
#    Prim menggunakan min-heap (priority queue). Setiap kali sebuah
#    node baru bergabung ke MST, semua edge dari node itu ke node
#    yang belum dikunjungi dimasukkan ke heap. Kemudian edge dengan
#    bobot terkecil dari heap diambil sebagai kandidat berikutnya.
#    Ini memastikan kita selalu memperluas MST dengan edge termurah
#    yang tersedia dari node-node yang sudah masuk MST.
#
# 4. Berapa total bobot MST yang dihasilkan?
#    Total bobot = 2 + 1 + 3 = 6
#    (edge A-C=2, C-D=1, D-B=3)
#
# 5. Apa perbedaan pendekatan Prim dan Kruskal?
#    - Kruskal: memilih edge terkecil secara GLOBAL dari seluruh
#      graph, tidak peduli posisi. Cocok untuk sparse graph.
#    - Prim: memilih edge terkecil yang menghubungkan node di dalam
#      MST dengan node di luar MST (LOCAL dari frontier). Dimulai
#      dari satu node dan "membesar" ke tetangga. Cocok untuk
#      dense graph karena tidak perlu mengurutkan semua edge.
#    - Keduanya menghasilkan MST dengan total bobot yang sama (6),
#      namun urutan pemilihan edge berbeda.
