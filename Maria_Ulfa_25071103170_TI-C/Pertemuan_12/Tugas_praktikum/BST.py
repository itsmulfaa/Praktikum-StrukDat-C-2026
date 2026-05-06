#==================================
#Sistem Katalog Perpustakaan (BST)
#==================================

#Class Node
class TreeNode:
    def __init__(self, id_buku, judul):
        self.id_buku= id_buku
        self.judul = judul
        self.left = None
        self.right = None
        
#Class BST
class BST:
    def __init__(self):
        self.root = None

    #insert
    def insert(self, id_buku, judul):
        new_node = TreeNode(id_buku, judul)

        if self.root is None:
            self.root = new_node
            print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}") 
        else:
            self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, current, new_node):
        if new_node.id_buku < current.id_buku:
            if current.left is None:
                current.left = new_node
                print(f"[INSERT] Berhasil memasukkan: ID {new_node.id_buku} - {new_node.judul}")
            else:
                self._insert_recursive(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
                print(f"[INSERT] Berhasil memasukkan: ID {new_node.id_buku} - {new_node.judul}")
            else:
                self._insert_recursive(current.right, new_node)

    #Search
    def search(self, id_buku):
        return self._search_recursive(self.root, id_buku)

    def _search_recursive(self, current, id_buku):
        if current is None:
            return None
        if id_buku == current.id_buku:
            return current
        elif id_buku < current.id_buku:
            return self._search_recursive(current.left, id_buku)
        else:
            return self._search_recursive(current.right, id_buku)
    
    #In-Order Tarversal
    def inorder(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, current):
        if current is not None:
            self._inorder_recursive(current.left)
            print(f"{current.id_buku} - {current.judul}")
            self._inorder_recursive(current.right)

    #Get Min
    def get_min(self):
        current = self.root
        while current.left is not None:
            current = current.left
        return current
    
    #Get Max
    def get_max(self):
        current = self.root
        while current.right is not None:
            current = current.right
        return current
    
    #Height
    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return -1
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return max(left_height, right_height) + 1
    

#=================================
#MAIN PROGRAM
#=================================

print("SISTEM KATALOG PERPUSTAKAAN 'ILMU TERANG' ")
print("=" * 50)

bst = BST()

#Input Data
bst.insert(50, "Dasar Pemrograman")
bst.insert(30, "Struktur Data")
bst.insert(70, "Kecerdasan Buatan")
bst.insert(20, "Matematika Diskrit")
bst.insert(40, "Basis Data")
bst.insert(60, "Jaringan Komputer")
bst.insert(80, "Sistem Operasi")

#Inorder Traversal
print("\n[INFO] Koleksi Buku (In-Order Tarversal): ")
bst.inorder()

#Search
hasil = bst.search(60)
if hasil:
    print(f"\n[SEARCH] Mencari ID 60... Ditemukan! Judul: {hasil.judul}")
else:
    print("[SEARCH] Mencari ID 60... Data tidak ditemukan.")

hasil = bst.search(100)
if hasil:
    print(f"[SEARCH] Mencari ID 100... Ditemukan! Judul: {hasil.judul}")
else:
    print("[SEARCH] Mencari ID 100... Data tidak ditemukan.")

#Statistik
print("\n[STATISTIK] ID Terkecil:", bst.get_min().id_buku)
print("[STATISTIK] ID Terbesar:", bst.get_max().id_buku)

#Height
print("[INFO] Tinggi (Height) Tree:", bst.height())

print("=" * 50)
print("Simulasi Selesai")