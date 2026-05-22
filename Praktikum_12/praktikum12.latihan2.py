# Nama  : Ahmad Maulana Abimanyu
# NIM   : J0403251017
# Kelas : A2
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 2: Implementasi Dijkstra
# ==========================================================

import heapq
from turtle import distance

# Weighted graph dengan bobot positif
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat,
        # maka proses dilewati
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

hasil = dijkstra(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Berapa jarak terpendek dari A ke B?
#    Jawab: 4
#    Penjelasan: Dijkstra menemukan jalur langsung A -> B dengan bobot 4.
#    Tidak ada jalur lain menuju B yang lebih kecil dari 4.

# 2. Berapa jarak terpendek dari A ke C?
#    Jawab: 2
#    Penjelasan: Jalur langsung A -> C dengan bobot 2.
#    C adalah node terdekat dari A.

# 3. Berapa jarak terpendek dari A ke D?
#    Jawab: 3
#    Penjelasan: Melalui jalur A -> C -> D = 2 + 1 = 3.
#    Bukan melalui A -> B -> D = 4 + 5 = 9.

# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B?
#    Jawab: Karena total bobot melalui C = 2 + 1 = 3, sedangkan
#    melalui B = 4 + 5 = 9. Meskipun jumlah edge sama (2 edge),
#    bobot setiap edge berbeda. Edge A->C (bobot 2) dan C->D (bobot 1)
#    jauh lebih kecil dibanding A->B (bobot 4) dan B->D (bobot 5).

# 5. Apa fungsi priority_queue dalam algoritma Dijkstra?
#    Jawab: Priority queue (min-heap) berfungsi untuk SELALU MEMILIH NODE
#    DENGAN JARAK TERKECIL yang belum diproses. Dengan struktur ini,
#    Dijkstra menjamin setiap node diproses berdasarkan urutan jarak
#    dari node awal. Ini adalah inti dari pendekatan greedy Dijkstra:
#    node yang jaraknya sudah paling kecil diproses lebih dulu,
#    sehingga ketika suatu node diambil dari queue, jaraknya sudah final
#    dan tidak perlu diubah lagi.

# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?
#    Jawab: Dijkstra menggunakan pendekatan greedy - sekali node diproses
#    dan jaraknya ditetapkan sebagai minimum, algoritma tidak akan
#    memperbarui jarak tersebut lagi. Asumsi ini hanya valid jika semua
#    bobot positif. Jika ada bobot negatif, bisa jadi ada jalur yang
#    melewati edge negatif menghasilkan jarak lebih kecil SETELAH node
#    sudah dikunci. Akibatnya, hasil shortest path menjadi tidak akurat.
#    Contoh: jika C -> D = -10, Dijkstra mungkin sudah mengunci jarak D
#    sebelum mempertimbangkan edge negatif tersebut.
