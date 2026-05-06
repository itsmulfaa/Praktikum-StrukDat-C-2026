#Antrean Giliran Petugas VAlet - Rotasi Melingkar

'''
Buat struktur Node dan CircularLinkedList di mana pointer next dari node terakhir menuju kembali ke head
Buat fungsi tambah_petugas(nama) untuk menambahkan petugas ke dalam list melingkar
Buat fungsi giliran_berikutnya (n) yang mensimulasikan n kali giliran dan mencetak nama petugas yang bertugas setiap gilirannya.
'''

#Struktur Node
class Node:
    def __init__(self, nama):
        self.nama = nama
        self.next = None


#Struktur Circular Linked List
class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Menambah petugas ke list melingkar
    def tambah_petugas(self, nama):
        new_node = Node(nama)

        #Jika list kosong
        if self.head is None:
            self.head = new_node
            new_node.next = self.head  #menunjuk ke dirinya sendiri
        else:
            current = self.head

            #Mencari node terakhir
            while current.next != self.head:
                current = current.next

            #Tambah node baru di akhir
            current.next = new_node
            new_node.next = self.head

    #Simulasi giliran petugas
    def giliran_berikutnya(self, n):
        if self.head is None:
            print("Tidak ada petugas.")
            return

        current = self.head

        print("Giliran petugas:")
        for i in range(n):
            print(f"Giriran {i+1}: {current.nama}")
            current = current.next

jadwal = CircularLinkedList()

jadwal.tambah_petugas("Andi")
jadwal.tambah_petugas("Budi")
jadwal.tambah_petugas("Citra")

jadwal.giliran_berikutnya(7)

