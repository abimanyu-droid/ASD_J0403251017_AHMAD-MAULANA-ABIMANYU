# Nama  : Ahmad Maulana Abimanyu
# NIM   : J0403251017
# Kelas : TPLA2
# Praktikum 13 - Graph III: Spanning Tree

# ===========================================================
# Praktikum13.materi2.py - Bagian 6.4
# Implementasi Algoritma Prim
# ===========================================================

import heapq  # modul bawaan Python untuk membuat min-heap (antrian prioritas)
               # heapq selalu menjaga elemen terkecil ada di posisi paling depan

# Representasi graph sebagai dictionary berlapis
# graph[node] = {tetangga: bobot} -> menunjukkan semua koneksi dari satu node
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},  # A terhubung ke B(bobot 4), C(bobot 2), D(bobot 5)
    'B': {'A': 4, 'D': 3},           # B terhubung ke A(bobot 4), D(bobot 3)
    'C': {'A': 2, 'D': 1},           # C terhubung ke A(bobot 2), D(bobot 1)
    'D': {'A': 5, 'B': 3, 'C': 1}   # D terhubung ke A(bobot 5), B(bobot 3), C(bobot 1)
}

def prim(graph, start):

    visited = set([start])  # tandai node awal sebagai sudah dikunjungi

    edges = []  # list yang akan dipakai sebagai min-heap (antrian prioritas)

    # Masukkan semua edge dari node awal ke dalam heap
    # Format yang dimasukkan: (bobot, node_asal, node_tujuan)
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))  # heappush = masukkan ke heap

    mst = []          # list untuk menyimpan edge-edge hasil MST
    total_weight = 0  # akumulasi total bobot MST

    # Terus proses selama masih ada kandidat edge di heap
    while edges:

        # heappop = ambil dan hapus elemen terkecil dari heap
        # hasilnya adalah edge dengan bobot paling kecil saat ini
        weight, u, v = heapq.heappop(edges)

        # Periksa apakah node tujuan (v) belum dikunjungi
        # Jika sudah dikunjungi, skip -> mengambilnya akan membentuk cycle
        if v not in visited:

            visited.add(v)              # tandai node v sudah masuk MST
            mst.append((u, v, weight))  # simpan edge ini ke hasil MST
            total_weight += weight      # tambahkan bobot ke total

            # Setelah node v bergabung, cari tetangga-tetangga v
            # yang belum dikunjungi dan masukkan edge-nya ke heap
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))  # masukkan kandidat edge baru

    return mst, total_weight  # kembalikan hasil MST dan total bobotnya


# Jalankan Prim mulai dari node 'A'
mst, total = prim(graph, 'A')

# Tampilkan semua edge yang terpilih dalam MST
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

# Tampilkan total bobot seluruh edge MST
print("Total bobot =", total)
