#Unpacking dasar
a = ("apel", "pisang", "ceri")

(x, y, z) = a

print(a)
print(x)
print(y)
print(z)

#Unpacking dengan tanda *
b = ("apel", "pisang", "ceri", "jeruk", "mangga")

(p, q, *r) = b

print(p)   #apel
print(q)   #pisang
print(r)   #sisanya jadi list

#Tanda * di tengah
c = ("apel", "pisang", "ceri", "jeruk", "mangga")

(i, *j, k) = c

print(i)   #apel
print(j)   #tengah
print(k)   #mangga


