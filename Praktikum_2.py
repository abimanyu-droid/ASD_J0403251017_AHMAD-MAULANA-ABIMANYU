# =====================================================
# Pertemuan 11 - TPL1109 Algoritma dan Struktur Data
# Praktikum 2 - Membuat Adjacency List
# Nama  : Ahmad Maulana Abimanyu
# NIM   : J0403251017
# =====================================================

def createGraph(V, edges):

    adj = [[] for _ in range(V)]

    # Menambahkan edge ke adjacency list
    for it in edges:
        u = it[0]
        v = it[1]

        adj[u].append(v)

        # karena graph undirected
        adj[v].append(u)

    return adj


if __name__ == "__main__":

    # Jumlah node
    V = 4

    # Graph:
    # A --- B
    # |     |
    # C --- D
    #
    # A = 0
    # B = 1
    # C = 2
    # D = 3

    # List edge
    edges = [
        [0, 1],
        [0, 2],
        [1, 3],
        [2, 3]
    ]

    # Membuat graph
    adj = createGraph(V, edges)

    print("Adjacency List Representation:")

    for i in range(V):

        # Menampilkan node
        print(f"{i}:", end=" ")

        for j in adj[i]:

            # Menampilkan node tetangga
            print(j, end=" ")

        print()