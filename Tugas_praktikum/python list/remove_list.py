#menghapus item berdasarkan nilai dengan remove
a = ["apel", "pisang", "ceri"]
a.remove("pisang")
print(a)

#jika ada duplikat, yang terhapus hanya yang pertama 
b = ["apel", "pisang", "ceri", "pisang", "kiwi"]
b.remove("pisang")
print(b)

#menghapus berdasarkan index dengan pop()
c = ["apel", "pisang", "ceri"]
c.pop(1)   #hapus index 1
print(c)

#pop() tanpa index menghapus data terakhir
d = ["apel", "pisang", "ceri"]
d.pop()
print(d)

#menghapus dengan del berdasarkan index
e = ["apel", "pisang", "ceri"]
del e[0]
print(e)

#menghapus seluruh list dengan del
f = ["apel", "pisang", "ceri"]
del f
#setelah ini variabel f sudah tidak ada lagi

#menghaps isi list dengan clear()
g = ["apel", "pisang", "ceri"]
g.clear()
print(g)

