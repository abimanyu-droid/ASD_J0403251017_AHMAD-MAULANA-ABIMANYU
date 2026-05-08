# ============================================================
# Pertemuan 11 - TPL1109 Algoritma dan Struktur Data
# Praktikum 4  - Studi Kasus Dunia Nyata : Peta Kota
# Nama         : Ahmad Maulana Abimanyu
# NIM          : J0403251017
# Dosen        : Dr. Shelvie Nidya Neyman, S.Kom, M.Si
# ============================================================

# Studi Kasus  : Peta Kota Wilayah Jawa Barat
# Node (Vertex): Kota / Kabupaten
# Edge         : Jalan penghubung antar kota
# Jenis Graph  : Undirected (jalan bisa dilalui dua arah)

# ── Data ────────────────────────────────────────────────────
nodes = ["Bogor", "Depok", "Jakarta", "Bekasi", "Karawang", "Bandung", "Sukabumi"]

edges = [
    ("Bogor",   "Depok"),
    ("Bogor",   "Sukabumi"),
    ("Bogor",   "Bandung"),
    ("Depok",   "Jakarta"),
    ("Depok",   "Bekasi"),
    ("Jakarta", "Bekasi"),
    ("Bekasi",  "Karawang"),
]

# ── Fungsi ───────────────────────────────────────────────────
def buat_adjacency_list(nodes, edges):
    adj = {node: [] for node in nodes}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    return adj

def buat_adjacency_matrix(nodes, edges):
    n     = len(nodes)
    idx   = {node: i for i, node in enumerate(nodes)}
    mat   = [[0] * n for _ in range(n)]
    for u, v in edges:
        i, j       = idx[u], idx[v]
        mat[i][j]  = 1
        mat[j][i]  = 1
    return mat

# ── Bangun struktur data ─────────────────────────────────────
adj_list   = buat_adjacency_list(nodes, edges)
adj_matrix = buat_adjacency_matrix(nodes, edges)

SEP = "=" * 58

# ── 1. Adjacency List ────────────────────────────────────────
print(SEP)
print("  1. ADJACENCY LIST")
print(SEP)
for kota, tetangga in adj_list.items():
    koneksi = ", ".join(tetangga) if tetangga else "-"
    print(f"  {kota:<12} -->  {koneksi}")

# ── 2. Adjacency Matrix ──────────────────────────────────────
print()
print(SEP)
print("  2. ADJACENCY MATRIX")
print(SEP)

COL = 10                              # lebar tiap kolom (header + nilai)
ROW = 12                              # lebar kolom label baris

# Header kolom
header_cells = [n[:8].center(COL) for n in nodes]
print("  " + " " * ROW + "".join(header_cells))
print("  " + "-" * (ROW + COL * len(nodes)))

# Baris matrix
for i, row in enumerate(adj_matrix):
    values = "".join(str(v).center(COL) for v in row)
    print(f"  {nodes[i]:<{ROW}}{values}")

# ── 3. Nama Node ─────────────────────────────────────────────
print()
print(SEP)
print("  3. DAFTAR NAMA NODE (KOTA)")
print(SEP)
for i, node in enumerate(nodes):
    print(f"  Node {i}  :  {node}")

# ── 4. Hubungan Antar Node ───────────────────────────────────
print()
print(SEP)
print("  4. HUBUNGAN ANTAR NODE (EDGE)")
print(SEP)
for no, (u, v) in enumerate(edges, start=1):
    print(f"  Edge {no}  :  {u}  <------>  {v}")
print()
print(f"  Total node  :  {len(nodes)} kota")
print(f"  Total edge  :  {len(edges)} jalan penghubung")
print(SEP)
