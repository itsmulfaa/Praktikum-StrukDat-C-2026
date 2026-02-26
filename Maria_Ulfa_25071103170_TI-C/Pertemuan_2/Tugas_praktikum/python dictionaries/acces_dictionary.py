data = {
    "nama": "Rina",
    "umur": 19,
    "jurusan": "Sistem Informasi",
    "kota": "Surabaya"
}

print("Isi dictionary:")
print(data)

#Mengakses nilai menggunakan key langsung
print("\nAkses dengan key langsung:")

print("Nama    :", data["nama"])
print("Jurusan :", data["jurusan"])

#Mengakses menggunakan metode get()
print("\nAkses dengan metode get():")

print("Umur :", data.get("umur"))

#Menampilkan semua key
print("\nMenampilkan semua key:")

for kunci in data.keys():
    print(kunci)

#Menampilkan semua value
print("\nMenampilkan semua value:")

for nilai in data.values():
    print(nilai)

#Menampilkan key dan value sekaligus
print("\nMenampilkan key dan value:")

for kunci, nilai in data.items():
    print(kunci, ":", nilai)

#Mengecek apakah key ada di dictionary
print("\nCek keanggotaan key:")

if "nama" in data:
    print("Key nama ada di dalam dictionary")
else:
    print("Key nama tidak ada")