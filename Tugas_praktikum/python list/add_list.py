#menambah item dengan append()
a = ["apel", "pisang", "ceri"]
a.append("jeruk")
print(a)

#menambah list dengan extend()
c = ["apel", "pisang", "ceri"]
d = ["mangga", "nanas", "pepaya"]

c.extend(d)
print(c)

#extend dengan iterable lain (tuple)
e = ["apel", "pisang", "ceri"]
f = ("kiwi", "jeruk")

e.extend(f)
print(e)