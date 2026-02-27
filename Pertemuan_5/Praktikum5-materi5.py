# ========================================================== 
# Contoh Backtracking 2: Kombinasi Biner dengan Batas '1' (Pruning) 
# ========================================================== 

# Definisi fungsi dengan tambahan parameter 'batas' dan penghitung 'jumlah_1'
def biner_batas(n, batas, hasil="", jumlah_1=0): 
    
    # Blok Pruning (Pemangkasan): Mengevaluasi syarat sebelum melangkah lebih jauh
    # Jika jumlah angka '1' sudah melebihi batas, fungsi langsung berhenti (return)
    # Jalur ini dianggap "mati" dan tidak akan dieksplorasi hingga ke base case
    # Pruning: jika jumlah_1 sudah melewati batas, berhenti 
    if jumlah_1 > batas: 
        return 
    
    # Blok Base Case: Kondisi berhenti saat kombinasi biner sudah mencapai panjang n
    # Karena ada pruning di atas, hasil yang sampai ke sini pasti memenuhi syarat batas
    # Base case 
    if len(hasil) == n: 
        print(hasil) 
        return 
    
    # Blok Pilih '0' (Choose + Explore): Menambahkan angka '0' ke dalam kombinasi
    # Parameter jumlah_1 tidak bertambah karena kita memilih angka '0'
    # Pilih '0' 
    biner_batas(n, batas, hasil + "0", jumlah_1)

    # Blok Pilih '1' (Choose + Explore): Menambahkan angka '1' ke dalam kombinasi
    # Parameter jumlah_1 bertambah 1 untuk dilacak pada pemanggilan berikutnya
    # Pilih '1' 
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1) 
    
# Blok Eksekusi: Mencari kombinasi biner panjang 4 dengan maksimal dua angka '1'
# Contoh output yang valid: "0011", "1010". Contoh yang dipangkas: "1110"    
biner_batas(4, 2)