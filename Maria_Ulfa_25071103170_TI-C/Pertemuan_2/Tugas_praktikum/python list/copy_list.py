# catatan:
# tidak bisa menyalin list hanya dengan b = a
# karena itu hanya membuat referensi, bukan salinan baru

#Copy menggunakan method copy()
a = ["apel", "pisang", "ceri"]
b = a.copy()
print(b)

#Copy menggunakan fungsi list()
c = ["apel", "pisang", "ceri"]
d = list(c)
print(d)

#Copy menggunakan slice operator
e = ["apel", "pisang", "ceri"]
f = e[:]
print(f)