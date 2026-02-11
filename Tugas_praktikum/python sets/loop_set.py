sets = {"apel", "pisang", "ceri", "mangga"}

print("Isi set:")
print(sets)

#Loop menggunakan for
print("\nMenampilkan isi set dengan for:")

for buah in sets:
    print(buah)

# Mengecek apakah item ada di dalam set
print("\nCek keanggotaan dalam set:")

if "apel" in sets:
    print("apel ada di dalam set")
else:
    print("apel tidak ada di dalam set")

#Contoh penggunaan dalam logika sederhana
print("\nFilter manual dengan loop:")

for buah in sets:
    if buah.startswith("m"):
        print(buah, "diawali huruf m")
