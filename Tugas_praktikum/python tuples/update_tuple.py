#tuple bersifat unchangeable (tidak bisa diubah langsung)
a = ("apel", "pisang", "ceri")
print(a)

#Mengubah tuple dengan cara diubah ke list dulu
b = list(a)     #ubah jadi list
b[1] = "mangga"   #ubah datanya
a = tuple(b)      #kembalikan jadi tuple

print(a)

#Menambah item ke tuple
c = ("apel", "pisang", "ceri")

d = list(c)
d.append("jeruk")
c = tuple(d)

print(c)

#Menghapus item dari tuple
e = ("apel", "pisang", "ceri")

f = list(e)
f.remove("pisang")
e = tuple(f)

print(e)

#Menggabungkan dua tuple
g = ("apel", "pisang")
h = ("mangga", "jeruk")

i = g + h
print(i)

