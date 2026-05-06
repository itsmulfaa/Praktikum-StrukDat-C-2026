# Stack menggunakan List
stack = []

def is_empty():
    return len(stack) == 0

def push(url):
    stack.append(url)

def pop():
    if is_empty():
        return "Riwayat kosong"
    else:
        return stack.pop()

def peek():
    if is_empty():
        return None
    else:
        return stack[-1]

def size():
    return len(stack)

# Program utama
push("google")
push("youtube")
push("github")

print("Isi riwayat:", stack)
print("Halaman aktif:", peek())
print("Jumlah riwayat:", size())

print("Back ke:", pop())
print("Halaman aktif sekarang:", peek())