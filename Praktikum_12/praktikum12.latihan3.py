# Nama  : Ahmad Maulana Abimanyu
# NIM   : J0403251017
# Kelas : A2
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):

        # Periksa semua edge
        for node in graph:
            for neighbor, weight in graph[node].items():

                # Jika jarak ke node saat ini sudah diketahui,
                # dan ditemukan jarak yang lebih kecil ke neighbor,
                # maka lakukan update jarak
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
   
    return distances

hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)


# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Berapa bobot langsung dari A ke B?
#    Jawab: 5
#    Penjelasan: Edge langsung A -> B memiliki bobot 5 sesuai definisi graph.

# 2. Berapa total bobot jalur A -> C -> B?
#    Jawab: 4 + (-2) = 2
#    Penjelasan: Dari A ke C bobotnya 4, lalu dari C ke B bobotnya -2.
#    Total = 4 + (-2) = 2. Bobot negatif pada edge C -> B membuat
#    jalur ini lebih murah meskipun melewati satu node tambahan.

# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
#    Jawab: Jalur A -> C -> B dengan total bobot 2.
#    Lebih kecil dibanding jalur langsung A -> B yang bobotnya 5.
#    Output program: A=0, B=2, C=4

# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
#    Jawab: Bellman-Ford TIDAK mengunci jarak seperti Dijkstra.
#    Algoritma ini melakukan relaksasi BERULANG pada semua edge sebanyak
#    (V-1) kali. Setiap iterasi memberi kesempatan memperbarui jarak
#    ke semua node, termasuk yang dipengaruhi oleh bobot negatif.
#    Karena semua edge diperiksa berulang kali, efek dari bobot negatif
#    akan terus dipropagasikan hingga nilai minimum ditemukan.
#    Bellman-Ford juga bisa mendeteksi negative cycle (siklus bobot negatif).

# 5. Apa yang dimaksud dengan proses relaksasi edge?
#    Jawab: Relaksasi edge adalah proses MEMERIKSA DAN MEMPERBARUI jarak
#    ke suatu node jika ditemukan jalur yang lebih pendek.
#    Caranya: jika distances[node] + bobot_edge < distances[tetangga],
#    maka distances[tetangga] diperbarui dengan nilai lebih kecil tersebut.
#    Proses ini disebut "relaksasi" karena kita "melonggarkan" estimasi
#    jarak yang sebelumnya mungkin terlalu besar, menuju nilai yang lebih
#    akurat dan kecil. Dilakukan berulang hingga semua jarak optimal.

# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
#    Jawab:
#    - Bobot negatif : Dijkstra TIDAK bisa, Bellman-Ford BISA
#    - Kecepatan     : Dijkstra lebih CEPAT O((V+E)logV),
#                      Bellman-Ford lebih LAMBAT O(V*E)
#    - Pendekatan    : Dijkstra menggunakan GREEDY (pilih node terkecil),
#                      Bellman-Ford menggunakan RELAKSASI BERULANG semua edge
#    - Struktur data : Dijkstra butuh priority queue,
#                      Bellman-Ford cukup dengan loop biasa
#    - Deteksi neg.  : Bellman-Ford bisa deteksi negative cycle,
#                      Dijkstra tidak bisa
