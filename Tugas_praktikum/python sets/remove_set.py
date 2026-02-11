sets = {"apel", "pisang", "ceri", "mangga"}
print("Set awal:", sets)

#Menghapus item dengan remove()
sets.remove("pisang")
print("\nSet setelah remove('pisang'):")
print(sets)

#Catatan:
#remove() akan error jika item tidak ada di dalam set

#Menghapus item dengan discard()
sets.discard("durian")   #tidak error walaupun tidak ada
print("\nSet setelah discard('durian') (tidak error walau tidak ada):")
print(sets)

#Menghapus item secara acak dengan pop()
item = sets.pop()
print("\nItem yang dihapus dengan pop():", item)
print("Set setelah pop():", sets)

#Mengosongkan set dengan clear()
sets.clear()
print("\nSet setelah clear():", sets)

#Menghapus set sepenuhnya dengan del
sets = {"apel", "pisang"}
del sets
#setelah ini variabel sets sudah tidak ada lagi

