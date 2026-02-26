#Set tidak bisa diakses pakai index
# Jadi kita harus pakai perulangan atau pengecekan nilai

#Mengakses set dengan for loop
sets = {"apple", "banana", "cherry"}
print("Isi set:")
for x in sets:
    print(x)

#Mengecek apakah item ada di dalam set
if "banana" in sets:
    print("banana ada di dalam set")

#Mengecek jika item TIDAK ada
if "mango" not in sets:
    print("mango tidak ada di dalam set")

#Mengubah set ke list agar bisa diakses dengan index (opsional)
list_set = list(sets)
print("Elemen pertama setelah diubah ke list:", list_set[0])



