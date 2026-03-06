# ========================================================== 
# Nama    : Ahmad Maulana Abimanyu
# NIM     : J0403251017
# Kelas   : A2
# ==========================================================
# Latihan 7: Latihan Soal Pengurutan
# ==========================================================

def quickSort(data):
    quickSortHelper(data,0,len(data)-1)

def quickSortHelper(data,first,last):
    if first<last:
        splitpoint = partition(data,first,last)
        quickSortHelper(data,first,splitpoint-1)
        quickSortHelper(data,splitpoint+1,last)

def partition(data,first,last):
    pivotvalue = data[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and data[leftmark] >= pivotvalue:
            leftmark = leftmark + 1

        while data[rightmark] <= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True

        else:
            temp = data[leftmark]
            data[leftmark] = data[rightmark]
            data[rightmark] = temp

    temp = data[first]
    data[first] = data[rightmark]
    data[rightmark] = temp
    return rightmark

data = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]
quickSort(data)
print("Skor setelah diurutkan (tertinggi ke terendah):")
print(data)

lolos = data[:5]
print("\n5 Kandidat dengan nilai tertinggi:")
print(lolos)

print("\nJumlah kandidat yang lolos:", len(lolos))

