#Membuat kelas
# Class adalah blueprint / cetakan
class Mahasiswa:
    
    # Properti kelas (class variable)
    kampus = "Universitas Riau"


#Membuat object
# Object dibuat dengan memanggil nama class
mhs1 = Mahasiswa()
mhs2 = Mahasiswa()

# mhs1 dan mhs2 adalah OBJECT
# Mereka dibuat dari class Mahasiswa


#Mengakses properti class
print(mhs1.kampus)
print(mhs2.kampus)

# Keduanya menampilkan nilai yang sama
# karena properti tersebut milik class


#Membuat object berada
print(mhs1)
print(mhs2)

# Walaupun dibuat dari class yang sama,
# keduanya tetap object yang berbeda
