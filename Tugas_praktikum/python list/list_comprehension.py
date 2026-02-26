#Cara biasa tanpa list comprehension
buah = ["apel", "pisang", "ceri", "kiwi", "mangga"]
baru = []

for x in buah:
    if "a" in x:
        baru.append(x)

print(baru)

#Cara singkat dengan list comprehension
baru2 = [x for x in buah if "a" in x]
print(baru2)

#List comprehension tanpa kondisi
semua = [x for x in buah]
print(semua)

#Menggunakan range sebagai iterable
angka = [x for x in range(10)]
print(angka)

#dengan kondisi
angka2 = [x for x in range(10) if x < 5]
print(angka2)

#Memanipulasi hasil menjadi huruf besar
besar = [x.upper() for x in buah]
print(besar)

#Mengubah semua hasil menjadi teks tertentu
hello = ["halo" for x in buah]
print(hello)

#Menggunakan kondisi else di expression
ganti = [x if x != "pisang" else "jeruk" for x in buah]
print(ganti)

