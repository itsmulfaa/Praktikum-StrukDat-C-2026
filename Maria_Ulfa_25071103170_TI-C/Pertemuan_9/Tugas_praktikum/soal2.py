#Hapus Kendaraan dari Tengah - Update Dua Arah

''''
Gunakan struktur Double Linked List dari soal 1.
Buat fungsi hapus_kendaraan(plat) yang mencari node berdasarkan plat, lalu
menghapusnya dengan memperbarui pointer next dan prev dari node tetangganya.
Tampilkan list sebelum dan sesudah penghapusan menggunakan tampilkan_maju().
'''

#Membuat class Node
class Node:
    def __init__(self, plat):
        self.plat = plat
        self.next = None
        self.prev = None

#Membuat class DoubleLinkedList
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    #Menambah kendaraan ke akhir list
    def tambah_kendaraan(self, plat):
        new_node = Node(plat)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    #Menampilkan dari depan ke belakang
    def tampilkan_maju(self):
        current = self.head
        while current is not None:
            print(current.plat)
            current = current.next

    #Fungsi menghapus kendaraan berdasarkan plat
    def hapus_kendaraan(self, plat):
        current = self.head

        #Mencari node yang akan dihapus
        while current is not None:
            if current.plat == plat:

                #Kasus 1: Node adalah HEAD
                if current.prev is None:
                    self.head = current.next
                    if self.head is not None:
                        self.head.prev = None

                #Kasus 2: Node adalah TAIL
                elif current.next is None:
                    self.tail = current.prev
                    self.tail.next = None

                #Kasus 3: Node di TENGAH
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                print("Kendaraan", plat, "berhasil dihapus.")
                return

            current = current.next

        print("Kendaraan tidak ditemukan.")


#Program utama
parkir = DoubleLinkedList()

parkir.tambah_kendaraan("B 1111 AA")
parkir.tambah_kendaraan("D 2222 BB")
parkir.tambah_kendaraan("A 3333 CC")
parkir.tambah_kendaraan("B 4444 DD")

print("Sebelum:")
parkir.tampilkan_maju()

parkir.hapus_kendaraan("A 3333 CC")

print("Sesudah:")
parkir.tampilkan_maju()