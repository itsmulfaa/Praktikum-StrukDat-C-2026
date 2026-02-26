#Membuat class
class Mahasiswa:
    
    # Constructor
    def __init__(self, nama, umur):
        
        # self adalah objek yang sedang dibuat
        
        self.nama = nama   # menyimpan ke dalam objek
        self.umur = umur   # menyimpan ke dalam objek
    
    
    # Method
    def tampilkan_data(self):
        
        # Mengakses data milik objek menggunakan self
        print("Nama :", self.nama)
        print("Umur :", self.umur)


#Membuat object
mhs1 = Mahasiswa("Maria", 19)
mhs2 = Mahasiswa("Atiqa", 20)


#Memanggil method
mhs1.tampilkan_data()
print("------------------")
mhs2.tampilkan_data()
