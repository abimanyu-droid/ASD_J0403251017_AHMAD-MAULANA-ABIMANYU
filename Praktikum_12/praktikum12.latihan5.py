# Nama  : Ahmad Maulana Abimanyu
# NIM   : J0403251017
# Kelas : A2
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 5: Studi Kasus Shortest Path Antar Kota
# Algoritma: Dijkstra
# ==========================================================

import heapq  # Modul untuk priority queue (min-heap)

# -----------------------------------------------------------
# 1. Representasi graph berbobot menggunakan dictionary
# -----------------------------------------------------------
# Setiap key adalah nama kota (node), value adalah dictionary
# berisi kota tujuan dan bobotnya (jarak dalam satuan tertentu)
graph = {
    'Bogor'   : {'Jakarta': 5, 'Depok': 2},  # Bogor terhubung ke Jakarta & Depok
    'Depok'   : {'Jakarta': 2, 'Bandung': 6}, # Depok terhubung ke Jakarta & Bandung
    'Jakarta' : {'Bandung': 7},               # Jakarta terhubung ke Bandung
    'Bandung' : {}                            # Bandung adalah kota tujuan akhir
}

# -----------------------------------------------------------
# 2. Fungsi Dijkstra
# -----------------------------------------------------------
def dijkstra(graph, start):
    """
    Mencari jarak terpendek dari kota 'start' ke semua kota lain.

    Cara kerja:
    - Inisialisasi jarak semua node = tak hingga, kecuali start = 0
    - Gunakan priority queue untuk selalu memproses node terdekat
    - Perbarui jarak tetangga jika ditemukan jalur lebih pendek
    - Ulangi hingga semua node diproses

    Parameter:
        graph : dict - weighted graph berisi hubungan antar kota
        start : str  - kota awal pencarian

    Return:
        distances : dict - jarak terpendek dari start ke tiap kota
    """

    # Inisialisasi semua jarak sebagai tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari kota awal ke dirinya sendiri = 0
    distances[start] = 0

    # Priority queue dimulai dari kota awal dengan jarak 0
    # Format: (jarak, nama_kota)
    priority_queue = [(0, start)]

    while priority_queue:
        # Ambil kota dengan jarak terkecil dari priority queue
        current_distance, current_node = heapq.heappop(priority_queue)

        # Lewati jika jarak ini sudah tidak relevan (sudah ada yang lebih kecil)
        if current_distance > distances[current_node]:
            continue

        # Periksa semua kota tetangga yang terhubung
        for neighbor, weight in graph[current_node].items():
            # Hitung jarak baru ke tetangga melalui kota saat ini
            distance = current_distance + weight

            # Jika jarak baru lebih kecil, perbarui dan masukkan ke queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# -----------------------------------------------------------
# 3. Penentuan node awal
# -----------------------------------------------------------
node_awal = 'Bogor'  # Pencarian dimulai dari kota Bogor

# -----------------------------------------------------------
# 4. Jalankan Dijkstra dan tampilkan output
# -----------------------------------------------------------
hasil = dijkstra(graph, node_awal)

print(f"Jarak terpendek dari {node_awal}:")
for kota, jarak in hasil.items():
    print(f"{node_awal} -> {kota} = {jarak}")


# ==========================================================
# Jawaban Analisis:
# ==========================================================

# Output yang dihasilkan program:
# Jarak terpendek dari Bogor:
# Bogor -> Bogor   = 0
# Bogor -> Depok   = 2
# Bogor -> Jakarta = 4
# Bogor -> Bandung = 8

# 1. Node awal yang digunakan apa?
#    Jawab: Node awal adalah BOGOR.
#    Dijkstra dimulai dari Bogor dengan jarak 0, semua kota lain = tak hingga.

# 2. Node mana yang memiliki jarak paling kecil dari node awal?
#    Jawab: DEPOK, dengan jarak 2.
#    Jalur: Bogor -> Depok langsung = 2.
#    Ini adalah kota terdekat dari Bogor dalam graph ini.

# 3. Node mana yang memiliki jarak paling besar dari node awal?
#    Jawab: BANDUNG, dengan jarak 8.
#    Jalur terpendek: Bogor -> Depok -> Bandung = 2 + 6 = 8.
#    Bukan Bogor -> Jakarta -> Bandung = 5 + 7 = 12.
#    Bukan Bogor -> Depok -> Jakarta -> Bandung = 2 + 2 + 7 = 11.

# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat:
#
#    Langkah 1 - Inisialisasi:
#    distances = {Bogor: 0, Depok: inf, Jakarta: inf, Bandung: inf}
#    priority_queue = [(0, 'Bogor')]
#
#    Langkah 2 - Proses Bogor (jarak 0):
#    - Tetangga Jakarta: 0 + 5 = 5 < inf -> update Jakarta = 5
#    - Tetangga Depok  : 0 + 2 = 2 < inf -> update Depok = 2
#    distances = {Bogor: 0, Depok: 2, Jakarta: 5, Bandung: inf}
#    priority_queue = [(2, 'Depok'), (5, 'Jakarta')]
#
#    Langkah 3 - Proses Depok (jarak 2, terkecil di queue):
#    - Tetangga Jakarta : 2 + 2 = 4 < 5 -> update Jakarta = 4
#    - Tetangga Bandung : 2 + 6 = 8 < inf -> update Bandung = 8
#    distances = {Bogor: 0, Depok: 2, Jakarta: 4, Bandung: 8}
#    priority_queue = [(4, 'Jakarta'), (5, 'Jakarta'(lama)), (8, 'Bandung')]
#
#    Langkah 4 - Proses Jakarta (jarak 4, terkecil di queue):
#    - Tetangga Bandung : 4 + 7 = 11 > 8 -> tidak diupdate
#    distances tetap: {Bogor: 0, Depok: 2, Jakarta: 4, Bandung: 8}
#
#    Langkah 5 - Proses Jakarta lama (jarak 5): dilewati karena 5 > distances[Jakarta]=4
#
#    Langkah 6 - Proses Bandung (jarak 8):
#    - Tidak ada tetangga -> selesai
#
#    HASIL AKHIR: Bogor=0, Depok=2, Jakarta=4, Bandung=8
