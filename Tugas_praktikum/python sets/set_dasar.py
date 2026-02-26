#Membuat set
sets = {"apple", "banana", "cherry"}
print(sets)

# Catatan:
# Set tidak berurutan, jadi urutan output bisa berubah-ubah

#Set tidak mengizinkan duplikasi
set2 = {"apple", "banana", "cherry", "apple"}
print(set2)   #apple yang kedua akan diabaikan

#True dianggap sama dengan 1
set3 = {"apple", True, 1, 2}
print(set3)

#False dianggap sama dengan 0
set4 = {"apple", False, 0, "banana"}
print(set4)

#Mengetahui panjang set
print(len(sets))

#Set bisa berisi berbagai tipe data
set5 = {"abc", 34, True, 40, "male"}
print(set5)

#Mengecek tipe data
print(type(sets))

#Membuat set dengan constructor
set6 = set(("apple", "banana", "cherry"))
print(set6)

