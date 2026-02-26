data = {
    "nama": "Siti",
    "umur": 19
}

print("Data awal:")
print(data)

#Menambah item baru dengan key langsung
print("\nMenambah data jurusan:")

data["jurusan"] = "Teknik Informatika"
print(data)


#Menambah lebih dari satu item
print("\nMenambah beberapa data:")

data["kota"] = "Gresik"
data["angkatan"] = 2024

print(data)


#Menambah item menggunakan update()
print("\nMenambah dengan metode update():")

data.update({"hobi": "membaca"})

print(data)


#Contoh penambahan dengan input logika sederhana
print("\nTambah status berdasarkan umur:")

if data["umur"] >= 18:
    data["status"] = "dewasa"

print(data)