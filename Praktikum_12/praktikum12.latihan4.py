# Nama  : Ahmad Maulana Abimanyu
# NIM   : J0403251017
# Kelas : A2
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================

import heapq

# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

hasil = dijkstra(graph, 'Gerbang')

print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")


# ==========================================================
# Jawaban Analisis:
# ==========================================================

# Hasil yang diharapkan dari program:
# Gerbang       = 0 menit
# Perpustakaan  = 6 menit  (Gerbang -> Perpustakaan langsung)
# Kantin        = 2 menit  (Gerbang -> Kantin langsung)
# Lab           = 6 menit  (Gerbang -> Kantin -> Lab = 2+4)
# Aula          = 7 menit  (Gerbang -> Kantin -> Lab -> Aula = 2+4+1)

# 1. Lokasi mana yang paling dekat dari Gerbang?
#    Jawab: KANTIN, dengan waktu tempuh 2 menit.
#    Ini adalah jalur langsung Gerbang -> Kantin dengan bobot 2.

# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
#    Jawab: 7 menit, melalui jalur Gerbang -> Kantin -> Lab -> Aula
#    Rincian: 2 + 4 + 1 = 7 menit.
#    Bukan jalur langsung Gerbang -> Kantin -> Aula = 2 + 7 = 9 menit.
#    Dan bukan Gerbang -> Perpustakaan -> Lab -> Aula = 6 + 3 + 1 = 10 menit.

# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
#    Jawab: TIDAK SELALU.
#    Contoh pada kasus ini: Gerbang ke Aula bisa ditempuh secara langsung
#    melalui Kantin -> Aula = 2 + 7 = 9 menit. Namun jalur yang melewati
#    Lab terlebih dulu justru lebih cepat: Kantin -> Lab -> Aula = 2+4+1 = 7 menit.
#    Hal ini membuktikan bahwa jalur dengan lebih banyak singgahan (lebih banyak
#    edge) bisa menghasilkan total waktu yang lebih singkat, tergantung bobot
#    masing-masing edge. Shortest path berfokus pada total bobot minimum,
#    bukan pada jumlah minimal node yang dilewati.

# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
#    Jawab: Karena semua bobot (waktu tempuh) pada graph kampus ini POSITIF.
#    Tidak mungkin waktu tempuh bernilai negatif di dunia nyata.
#    Dijkstra dirancang khusus dan bekerja optimal pada graph berbobot positif.
#    Selain itu, Dijkstra lebih EFISIEN dibanding Bellman-Ford untuk kasus
#    seperti ini, karena menggunakan priority queue sehingga kompleksitasnya
#    O((V+E) log V) - jauh lebih cepat dari Bellman-Ford O(V*E).
#    Pada aplikasi nyata seperti navigasi kampus, kecepatan komputasi penting
#    agar hasil ditemukan secara real-time.
