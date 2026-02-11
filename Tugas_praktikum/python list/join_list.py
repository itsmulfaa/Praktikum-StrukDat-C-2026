#Menggabungkan dengan operator +
a = ["apel", "pisang", "ceri"]
b = ["mangga", "nanas", "pepaya"]

gabung = a + b
print(gabung)

#Menggabungkan dengan append menggunakan loop
c = ["apel", "pisang", "ceri"]
d = ["mangga", "nanas", "pepaya"]

for x in d:
    c.append(x)

print(c)

#Menggabungkan dengan extend()
e = ["apel", "pisang", "ceri"]
f = ["mangga", "nanas", "pepaya"]

e.extend(f)
print(e)