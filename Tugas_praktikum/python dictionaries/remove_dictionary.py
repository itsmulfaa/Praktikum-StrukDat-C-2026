data = {
    "nama": "Andi",
    "umur": 20,
    "jurusan": "Informatika",
    "kota": "Sidoarjo",
    "hobi": "futsal"
}

print("Data awal:")
print(data)

#Menghapus item dengan pop()
print("\nMenghapus key jurusan dengan pop():")

data.pop("jurusan")
print(data)


#Menghapus item terakhir dengan popitem()
print("\nMenghapus item terakhir dengan popitem():")

data.popitem()
print(data)


#Menghapus dengan del
print("\nMenghapus key umur dengan del:")

del data["umur"]
print(data)


#Mengosongkan seluruh isi dictionary
print("\nMengosongkan dictionary dengan clear():")

data.clear()
print(data)

