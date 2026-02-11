#mengakses item berdasarkan index
a = ("apel", "pisang", "ceri", "jeruk", "kiwi", "mangga")
print(a[1])   #index 1 -> pisang

#Negative indexing
print(a[-1])   #item terakhir -> mangga
print(a[-2])   #item kedua dari belakang -> kiwi

#Range of indexes
print(a[2:5])   #dari index 2 sampai 4

#Range tanpa nilai awal
print(a[:4])   #dari awal sampai index 3

#Range tanpa nilai akhir
print(a[2:])   #dari index 2 sampai akhir

#Range dengan negative indexes
print(a[-4:-1])

#Mengecek apakah item ada di tuple
if "apel" in a:
    print("Ya, apel ada di dalam tuple")

if "anggur" in a:
    print("anggur ada")
else:
    print("anggur tidak ada di tuple")
    