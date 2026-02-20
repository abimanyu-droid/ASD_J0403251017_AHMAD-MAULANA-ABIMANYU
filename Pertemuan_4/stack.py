#=============================================
# Nama  : Ahmad Maulana Abimanyu
# NIM   : J0403251017
# kelas : A2
#=============================================

#=============================================
# Implementasi Dasar : Stack 
#=============================================

from inspect import stack


class Node:
    #konstruktor adalah fungsi yang dijalankan secara otomatis ketika dipanggil / diinstansiasi
    def __init__(self,data):
        self.data = data #menyimpan nilai / data pada list
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)


#Stack ada operasi push (memasukan head baru) dan pop (menghapus head)
#A -> B -> C -> None

class stack:
    def __init__(self):
        self.top = None #top menunjuk ke node paling atas (awalnya kosong)

    def push(self,data): #memasukan data baru pada stack
        #1 membuat node baru
        nodeBaru = Node(data) #Instantiasi/memanggil konstruktor pada class Node
        
        
        #2 node baru menunjuk ke top yang lama (head lama)
        nodeBaru.next = self.top 

        #3 geser top pindah ke node baru
        self.top = nodeBaru 

    def is_empty(self):
        return self.top is None #Stack kosong jika top = None

    def pop(self): #mengambil / menghapus node paling atas (top/head)
    
        if self.is_empty():
            print("Stack kosong, tidak bisa pop")
            return None
        data_terhapus = self.top.data #soroti bagian top dan simpan di variabel (peek)
        self.top = self.top.next #geser top ke node berikutnya
        return data_terhapus 
    
    def peek(self):
        #melihat data paling atas tanpa menghapus
        if self.is_empty():
            return None
        return self.top.data

    def tampilkan(self):
        #Top -> A -> B
        current = self.top
        print("Top ->", end=" ")
        while current is not None:
            print(current.data, end=" ") 
            current = current.next 
        print("None")

#Instantiasi Class Stack
s = stack()
s.push("A")
s.push("B")  
s.push("C")
s.tampilkan()      
print ("Peek (Lihat Top): ", s.peek())
s.pop()
s.tampilkan()
print ("Peek (Lihat Top): ", s.peek())