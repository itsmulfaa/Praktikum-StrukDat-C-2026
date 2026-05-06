class Node:
    def __init__(self, plat):
        self.plat = plat
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    #tambah kendaraan biasa di akhir
    def tambah(self, plat):
        new = Node(plat)

        if self.head == None:
            self.head = new
        else:
            n = self.head
            while n.next:
                n = n.next
            n.next = new

    #sisipkan kendaraan VIP setelah plat tertentu
    def sisipkan_vip(self, plat_baru, plat_target):
        n = self.head

        while n:
            if n.plat == plat_target:
                new = Node(plat_baru)
                new.next = n.next
                n.next = new
                break
            n = n.next

    #menampilkan antrean
    def tampilkan_antrean(self):
        n = self.head
        while n:
            print(n.plat, end=" -> ")
            n = n.next
        print("None")


valet = LinkedList()

valet.tambah("B 1234 ABC")
valet.tambah("D 8888 XYZ")
valet.tambah("A 111 TUV")

print("Antrean awal:")
valet.tampilkan_antrean()

valet.sisipkan_vip("VIP 999", "D 8888 XYZ")

print("Antrean setelah VIP masuk:")
valet.tampilkan_antrean()