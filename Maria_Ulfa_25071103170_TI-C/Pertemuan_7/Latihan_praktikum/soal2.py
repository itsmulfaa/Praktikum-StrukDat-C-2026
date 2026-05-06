class Node:
    def __init__(self, plat):
        self.plat = plat
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # menambah kendaraan di akhir (tail)
    def tambahKendaraan(self, plat):
        new = Node(plat)

        if self.head == None:
            self.head = new
        else:
            n = self.head
            while n.next:
                n = n.next
            n.next = new

    # menghapus kendaraan tertentu
    def hapusKendaraan(self, plat):
        n = self.head
        prev = None

        while n:
            if n.plat == plat:
                if prev == None:
                    self.head = n.next
                else:
                    prev.next = n.next
                break
            prev = n
            n = n.next

    # menampilkan antrean
    def tampil(self):
        n = self.head
        while n:
            print(n.plat, end=" -> ")
            n = n.next
        print("Null")


parkir = LinkedList()

parkir.tambahKendaraan("B1234")
parkir.tambahKendaraan("D8888")
parkir.tambahKendaraan("A111")
parkir.tambahKendaraan("B2022")

print("Antrean awal:")
parkir.tampil()

parkir.hapusKendaraan("A111")

print("Antrean setelah kendaraan mogok dihapus:")
parkir.tampil()