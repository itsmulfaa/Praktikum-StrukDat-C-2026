#Mmebuat clss dengan _init_()
class Mahasiswa:
    
    # __init__ adalah method khusus (constructor)
    # Method ini otomatis dijalankan
    # saat objek dibuat

      def __init__(self, nama, umur):
        
        # self = objek itu sendiri
        
        # Properti instance
        # Setiap objek akan punya nilai masing-masing
        self.nama = nama
        self.umur = umur


#Membuat object
# Saat membuat objek, kita wajib mengisi parameter
mhs1 = Mahasiswa("Maria", 19)
mhs2 = Mahasiswa("Atiqa", 20)


#Menampilkan data object
print(mhs1.nama)
print(mhs1.umur)

print("------------------")

print(mhs2.nama)
print(mhs2.umur)
