#loop biasa menggunakan for
a = ["apel", "pisang", "ceri"]
for x in a:
    print(x)

#Loop menggunakan index dengan range dan len
for i in range(len(a)):
    print(a[i])

# Loop menggunakan while
i = 0
while i < len(a):
    print(a[i])
    i = i + 1

# Loop menggunakan list comprehension
[print(x) for x in a]