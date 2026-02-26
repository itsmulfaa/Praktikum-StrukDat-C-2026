# PYTHON OOP (OBJECT ORIENTED PROGRAMMING)
# OOP adalah cara menulis program menggunakan
# CLASS (cetakan) dan OBJECT (hasil cetakan)

#Membuat class
# Class adalah blueprint / template
class Mobil:
    pass
    # "pass" digunakan jika class masih kosong
    # Agar Python tidak error


#Membuat object dari class
# Object dibuat dengan memanggil nama class
mobil1 = Mobil()
mobil2 = Mobil()

# mobil1 dan mobil2 adalah OBJECT
# Mereka dibuat dari class Mobil


#Menampilkan object
print(mobil1)
print(mobil2)
# Output akan menampilkan alamat memori object

#Menambahkan data ke class (Properti)
class Motor:
    jenis = "Sport"   # ini disebut properti kelas

#Membuat object dari class Motor
motor1 = Motor()
motor2 = Motor()

# Mengakses properti melalui object
print(motor1.jenis)
print(motor2.jenis)

# Kedua object memiliki nilai yang sama
# karena berasal dari class yang sama

   