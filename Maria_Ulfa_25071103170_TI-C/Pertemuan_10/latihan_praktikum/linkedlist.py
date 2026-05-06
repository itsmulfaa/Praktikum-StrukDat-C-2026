class Node:
    def __init__(self, url):
        self.url = url
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self.count = 0 #Variabel bantuan untuk melacak ukuran

    def is_empty(self):
        return self.count == 0

    def push(self, url):
        new_node = Node(url)
        if self.top:
            new_node.next = self.top
        self.top = new_node
        self.count += 1
        pass

    def pop(self):
        if self.is_empty():
            return 'Riwayat kosong'
        removed_url = self.top
        self.top = self.top.next
        self.count -= 1
        return removed_url
        pass

    def peek(self):
        if self.is_empty():
            return None
        return self.top.url
        pass

    def size(self):
        return self.count
        pass

    def traverseAndPrint(self):
        currentNode = self.top
        while currentNode:
            print(currentNode.url, end="->")

            currentNode = currentNode.next
        print()
    
stack = StackLinkedList()

stack.push("google")
stack.push("youtube")
stack.push("github")

print("Isi Riwayat: ", end="")
stack.traverseAndPrint()
print("Halaman aktif:", stack.peek())
print("Jumlah riwayat:", stack.size())

print("Back ke:", stack.pop())
print("Halaman aktif sekarang:", stack.peek())