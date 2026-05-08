# =====================================================
# Pertemuan 11 - TPL1109 Algoritma dan Struktur Data
# Praktikum 1 - Membuat Adjacency Matrix
# Nama  : Ahmad Maulana Abimanyu
# NIM   : J0403251017
# =====================================================

def createGraph(V, edges):
    mat = [[0 for _ in range(V)] for _ in range(V)]

    # Menambahkan edge ke adjacency matrix
    for it in edges:
        u = it[0]
        v = it[1]

        mat[u][v] = 1
        mat[v][u] = 1   # karena graph undirected

    return mat


if __name__ == "__main__":

    # Jumlah node
    V = 4

    # Daftar edge
    # Graph:
    # 0 --- 1
    # |    /
    # 2 --- 3

    edges = [
        [0, 1],
        [0, 2],
        [1, 3],
        [2, 3]
    ]

    # Membuat graph
    mat = createGraph(V, edges)

    # Menampilkan adjacency matrix
    print("Adjacency Matrix Representation:")

    for i in range(V):
        for j in range(V):
            print(mat[i][j], end=" ")
        print()

    # Penjelasan setiap baris
    print("\nPenjelasan Setiap Baris:")
    print("Baris 0 : Node 0 terhubung dengan node 1 dan 2")
    print("Baris 1 : Node 1 terhubung dengan node 0 dan 3")
    print("Baris 2 : Node 2 terhubung dengan node 0 dan 3")
    print("Baris 3 : Node 3 terhubung dengan node 1 dan 2")