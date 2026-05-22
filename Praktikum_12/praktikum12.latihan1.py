# Nama  : Ahmad Maulana Abimanyu
# NIM   : J0403251017
# Kelas : A2
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur
# ==========================================================

# Representasi weighted graph menggunakan dictionary bersarang
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Menghitung dua kemungkinan jalur dari A ke D
jalur_1 = graph['A']['B'] + graph['B']['D'] # A -> B -> D
jalur_2 = graph['A']['C'] + graph['C']['D'] # A -> C -> D

print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)

if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")

# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Berapa total bobot jalur A -> B -> D?
#    Jawab: Total bobot jalur A -> B -> D = 4 + 5 = 9
#    Rincian: A ke B bobotnya 4, kemudian B ke D bobotnya 5.

# 2. Berapa total bobot jalur A -> C -> D?
#    Jawab: Total bobot jalur A -> C -> D = 2 + 1 = 3
#    Rincian: A ke C bobotnya 2, kemudian C ke D bobotnya 1.

# 3. Jalur mana yang dipilih sebagai jalur terpendek?
#    Jawab: Jalur terpendek adalah A -> C -> D dengan total bobot 3.
#    Karena 3 < 9, maka jalur A -> C -> D lebih optimal dipilih.

# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?
#    Jawab: Karena pada weighted graph, setiap edge memiliki bobot yang berbeda-beda.
#    Shortest path berfokus pada TOTAL BOBOT MINIMUM, bukan jumlah edge.
#    Pada contoh ini, kedua jalur sama-sama memiliki 2 edge, namun total bobotnya
#    berbeda jauh (9 vs 3). Bahkan jika suatu jalur memiliki lebih banyak edge
#    tetapi total bobotnya lebih kecil, jalur tersebut tetap dipilih sebagai
#    jalur terpendek. Contoh: jalur 3 edge dengan total bobot 4 lebih baik
#    daripada jalur 2 edge dengan total bobot 9.
