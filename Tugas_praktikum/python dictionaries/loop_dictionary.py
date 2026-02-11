data = {
    "nama": "Rani",
    "umur": 19,
    "jurusan": "Sistem Informasi",
    "kota": "Surabaya"
}

print("Isi dictionary:")
print(data)

#Loop untuk menampilkan semua key
print("\nMenampilkan semua key:")

for kunci in data:
    print(kunci)


#Loop untuk menampilkan semua value
print("\nMenampilkan semua value:")

for nilai in data.values():
    print(nilai)


#Loop untuk menampilkan key dan value
print("\nMenampilkan key dan value:")

for kunci, nilai in data.items():
    print(kunci, ":", nilai)


#Contoh penggunaan loop dengan logika
print("\nMenampilkan data bertipe string saja:")

for kunci, nilai in data.items():
    if type(nilai) == str:
        print(kunci, "->", nilai)

