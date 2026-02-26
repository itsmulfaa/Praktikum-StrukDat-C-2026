#Sort alfabet secara ascending
a = ["jeruk", "mangga", "kiwi", "nanas", "pisang"]
a.sort()
print(a)

#Sort angka secara ascending
b = [100, 50, 65, 82, 23]
b.sort()
print(b)

#Sort descending (terbalik)
c = ["jeruk", "mangga", "kiwi", "nanas", "pisang"]
c.sort(reverse=True)
print(c)

d = [100, 50, 65, 82, 23]
d.sort(reverse=True)
print(d)

#Custom sort dengan fungsi sendiri
def dekat_50(n):
    return abs(n - 50)

e = [100, 50, 65, 82, 23]
e.sort(key=dekat_50)
print(e)

#Sort case sensitive
f = ["pisang", "Jeruk", "Kiwi", "ceri"]
f.sort()
print(f)

#Sort tidak sensitif huruf besar kecil
g = ["pisang", "Jeruk", "Kiwi", "ceri"]
g.sort(key=str.lower)
print(g)

#Membalik urutan list dengan reverse()
h = ["pisang", "Jeruk", "Kiwi", "ceri"]
h.reverse()
print(h)

