# =====================================================
# Pertemuan 11 - TPL1109 Algoritma dan Struktur Data
# Praktikum 3 - Konversi Matrix ke List
# Nama  : Ahmad Maulana Abimanyu
# NIM   : J0403251017
# =====================================================

def matrixToList(matrix):

    V = len(matrix)

    # Membuat adjacency list kosong
    adj = [[] for _ in range(V)]

    # Konversi matrix ke adjacency list
    for i in range(V):
        for j in range(V):

            if matrix[i][j] == 1:
                adj[i].append(j)

    return adj


if __name__ == "__main__":

    # Adjacency Matrix
    matrix = [
        [0,1,1,0],
        [1,0,1,0],
        [1,1,0,1],
        [0,0,1,0]
    ]

    # Konversi matrix ke adjacency list
    adj = matrixToList(matrix)

    print("Adjacency List Representation:")

    for i in range(len(adj)):

        # Menampilkan node
        print(f"{i}:", end=" ")

        for j in adj[i]:

            # Menampilkan node tetangga
            print(j, end=" ")

        print()