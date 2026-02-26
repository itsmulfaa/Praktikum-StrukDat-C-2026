#Membuat class
class Mobil:
    # PROPERTI KELAS (Class Variable)
    # Properti ini dimiliki oleh class
    # dan dibagi ke semua objek
    jumlah_roda = 4

    # CONSTRUCTOR
    def __init__(self, merk, warna):

        # PROPERTI INSTANCE
        # Properti ini khusus untuk setiap objek
        self.merk = merk
        self.warna = warna  


#Membuat object
mobil1 = Mobil("Toyota", "Merah")
mobil2 = Mobil("Honda", "Hitam")


#Mengakses properti instance
print(mobil1.merk)
print(mobil1.warna)

print("------------------")

print(mobil2.merk)
print(mobil2.warna)


#Mengakses properti class
print("------------------")
print(mobil1.jumlah_roda)
print(mobil2.jumlah_roda)

# Walaupun objek berbeda,
# jumlah_roda tetap sama karena milik class


#Memodifikasi properti instance
mobil1.warna = "Biru"

print("------------------")
print("Setelah warna mobil1 diubah:")
print(mobil1.warna)
print(mobil2.warna)


#Memodifikasi properti class
Mobil.jumlah_roda = 6

print("------------------")
print("Setelah jumlah_roda diubah:")
print(mobil1.jumlah_roda)
print(mobil2.jumlah_roda)

# Karena ini properti kelas,
# semua objek ikut berubah

