def registrasi_gadget(merk, tipe, harga, sn):
    if harga <= 1000000:
        print("error : Harga harus di atas 1000000")
        return None

    if len(sn) < 5:
        print("error : sn harus berisi minimal 5 karakter")
        return None

    return {
        "merk": merk,
        "tipe": tipe,
        "harga": harga,
        "sn": sn,
        "status": "Tersedia"
    }

#program utama
inventaris = []

for i in range(3):
    merk = input("Masukkan merk gadget: ")
    tipe = input("Masukkan tipe gadget:")
    harga = input("Masukkan merk gadget:")
    sn = input("Masukkan Serial Number gadget:")

    gadget = registrasi_gadget(merk, tipe, harga, sn)

    if gadget is not None:
        inventaris.append(gadget)

#Menampilkan hasil inventaris
print("Daftar Inventaris Gadget :")
for item in inventaris:
    print(item)


   




