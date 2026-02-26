sets = {"apple", "banana", "cherry"}
print("Set awal:", sets)

#Menambah satu item dengan add()
sets.add("orange")
print("\nSet setelah add('orange'):")
print(sets)

#Menambah banyak item dengan update()
sets.update(["mango", "grapes"])
print("\nSet setelah update(['mango','grapes']):")
print(sets)

#Menambah dari iterable lain (tuple)
tropical = ("pineapple", "papaya")
sets.update(tropical)

print("\nSet setelah tambah dari tuple tropical:")
print(sets)

#Coba tambah data duplikat (tidak akan bertambah)
sets.add("apple")
print("\nSet setelah add('apple') lagi (tidak berubah karena duplikat):")
print(sets)