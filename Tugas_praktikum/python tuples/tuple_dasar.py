#Membuat tuple dengan tanda kurung ()
a = ("apel", "pisang", "ceri")
print(a)

#tuple bersifat ordered (urutannya tetap)
b = ("merah", "kuning", "hijau")
print(b)

#Tuple memperbolehkan nilai duplikat
c = ("apel", "pisang", "ceri", "apel", "ceri")
print(c)

#Mengetahui panjang tuple dengan len()
print(len(a))

#Membuat tuple dengan satu item harus pakai koma
d = ("apel",)
print(type(d))   #ini tuple

e = ("apel")
print(type(e))   #ini bukan tuple, tapi string

#Tuple dapat berisi berbagai tipe data
angka = (1, 5, 7, 9, 3)
boolean = (True, False, False)
campur = ("abc", 34, True, 40, "male")

print(angka)
print(boolean)
print(campur)

#Mengecek tipe data tuple
print(type(a))

#Membuat tuple dengan constructor tuple()
f = tuple(("ayam", "kucing", "ikan"))
print(f)
