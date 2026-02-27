# ========================================================== 
# Nama    : Ahmad Maulana Abimanyu
# NIM     : J0403251017
# Kelas   : A2
# ==========================================================
# Contoh Rekursi 1: Faktorial 
# ========================================================== 

# Definisi fungsi faktorial dengan parameter n
def faktorial(n): 
    
    # Blok Base Case: Titik henti rekursi
    # Jika n mencapai 0, fungsi berhenti memanggil dirinya sendiri dan mengembalikan 1
    # Base case: berhenti ketika n = 0 
    if n == 0: 
        return 1 
    
    # Blok Recursive Case: Proses pemecahan masalah
    # Fungsi memanggil dirinya sendiri dengan argumen yang lebih kecil (n - 1)
    # Hasil perkalian akan ditumpuk hingga base case tercapai
    # Recursive case: masalah diperkecil menjadi faktorial(n-1) 
    return n * faktorial(n - 1) 

# Blok Eksekusi: Memanggil fungsi dan menampilkan hasil ke terminal
# Dalam kasus ini, 5 * 4 * 3 * 2 * 1 = 120
print(faktorial(5)) # Output: 120