#=============================================
# Nama  : Ahmad Maulana Abimanyu
# NIM   : J0403251017
# kelas : A2
#=============================================

#=============================================
# Implementasi Dasar : Node pada Linked List
#=============================================

class Node:
    #konstruktor adalah fungsi yang dijalankan secara otomatis ketika dipanggil / diinstansiasi
    def __init__(self,data):
        self.data = data #menyimpan nilai / data pada list
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)

#1) membuat node dengan instantiasi class node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#2) mendefinisikan head dan menghubungkan node : A -> B -> C -> None
head = nodeA #head menunjuk ke nodeA
nodeA.next = nodeB #setelah node A ke node B
nodeB.next = nodeC #setelah node B ke node C

#4) Traversal : menelusuri node dari head sampai ke none
current = head
while current is not None:
    print(current.data) #menampilkan data pada node saat ini
    current = current.next #pointer pindah ke node berikutnya 


