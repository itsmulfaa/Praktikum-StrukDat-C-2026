#Membuat class
class Mahasiswa:
    # Constructor
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    
    #Methods untuk menampilkan data
    def tampilkan_data(self):
            # self digunakan untuk mengakses
            # properti milik objek
        print("Nama  :", self.nama)
        print("Nilai :", self.nilai)


    #Methods untuk mengubah data
    def ubah_nilai(self, nilai_baru):
            # Mengubah properti instance
            self.nilai = nilai_baru
            print("Nilai berhasil diubah!")


#Membuat object
mhs1 = Mahasiswa("Maria", 90)
mhs2 = Mahasiswa("Atiqa", 80)


#Memanggil methods
mhs1.tampilkan_data()
print("------------------")
mhs2.tampilkan_data()


#Menggunakan methods untuk mengubah data
print("------------------")
mhs1.ubah_nilai(95)

print("------------------")
mhs1.tampilkan_data()