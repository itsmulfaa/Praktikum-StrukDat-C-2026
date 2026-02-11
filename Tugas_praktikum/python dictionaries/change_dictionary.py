data = {
    "nama": "Budi",
    "umur": 18,
    "jurusan": "Informatika",
    "kota": "Malang"
}

print("Data awal:")
print(data)


#Mengubah nilai berdasarkan key
print("\nMengubah nilai umur:")

data["umur"] = 19
print(data)


#Mengubah lebih dari satu nilai
print("\nMengubah jurusan dan kota:")

data["jurusan"] = "Sistem Informasi"
data["kota"] = "Surabaya"

print(data)


#Mengubah menggunakan update()
print("\nMengubah dengan metode update():")

data.update({"nama": "Andi"})

print(data)


#Contoh perubahan dengan logika
print("\nPerubahan dengan kondisi:")

if data["umur"] < 20:
    data["status"] = "mahasiswa baru"

print(data)