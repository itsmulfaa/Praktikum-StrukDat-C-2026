#Parkir Dua Arah - Penelusuran Maju & Mundur

'''
Buat struktur Node dan DoubleLinkedList dengan pointer next dan prev.
Buat fungsi tambah_kendaraan(plat) untuk menambah kendaraan ke akhir list.
Buat fungsi tampilkan_maju() untuk mencetak semua kendaraan dari head ke tail.
Buat fungsi tampilkan_mundur() untuk mencetak semua kendaraan dari tail ke head.
'''

#Membuat class Node
class Node:
    def __init__(self, plat):
        self.plat = plat      # Menyimpan data plat kendaraan
        self.next = None      # Pointer ke node berikutnya
        self.prev = None      # Pointer ke node sebelumnya


#Membuat class DoubleLinkedList
class DoubleLinkedList:
    def __init__(self):
        self.head = None  # Node pertama
        self.tail = None  # Node terakhir

    #Fungsi untuk menambah kendaraan ke akhir list
    def tambah_kendaraan(self, plat):
        new_node = Node(plat)  # Membuat node baru

        #Jika list kosong
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            #Hubungkan node baru dengan node terakhir
            new_node.prev = self.tail
            self.tail.next = new_node

            #Pindahkan tail ke node baru
            self.tail = new_node

    #Menampilkan data dari depan ke belakang
    def tampilkan_maju(self):
        print("[Maju]")
        current = self.head  # Mulai dari head

        while current is not None:
            print(current.plat)
            current = current.next  # Pindah ke node berikutnya

    #Menampilkan data dari belakang ke depan
    def tampilkan_mundur(self):
        print("[Mundur]")
        current = self.tail  #Mulai dari tail

        while current is not None:
            print(current.plat)
            current = current.prev  #Pindah ke node sebelumnya


#Program utama
parkir = DoubleLinkedList()

parkir.tambah_kendaraan("B 1234 ABC")
parkir.tambah_kendaraan("D 5678 XYZ")
parkir.tambah_kendaraan("A 9999 TUV")

parkir.tampilkan_maju()
parkir.tampilkan_mundur()

