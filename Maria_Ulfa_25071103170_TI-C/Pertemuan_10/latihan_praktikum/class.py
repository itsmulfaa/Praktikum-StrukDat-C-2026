class StackList:
    def __init__(self):
        self.items = [] #Menggunakan list bawaan Python

    def is_empty(self):
        return len(self.items) == 0
        pass

    def push(self, url):
        self.items.append(url)
        pass

    def pop(self):
        if self.is_empty():
            return "Riwayat kosong"
        else:
            return self.items.pop()
        pass

    def peek(self):
        if self.is_empty():
            return "Riwayat kosong"
        else:
            return self.items[-1]
        pass

    def size(self):
        return len(self.items)
        pass

stack = StackList()

stack.push("google")
stack.push("youtube")
stack.push("github")

print("Isi Riwayat: ", stack.items)
print("Halaman aktif:", stack.peek())
print("Jumlah riwayat:", stack.size())

print("Back ke:", stack.pop())
print("Halaman aktif sekarang:", stack.peek())