stok_barang = [15, 40, 30, 10, 25]
stok_barang[3] = 50
print(stok_barang)

stok_barang.append(5)
print(stok_barang)

stok_barang.sort(reverse = True)
print(stok_barang)

stok_barang = sum(stok_barang)
print(stok_barang)

rata_rata = stok_barang/5
nilai = "Stok Aman" if rata_rata > 20 else "Waspada"
print(nilai)