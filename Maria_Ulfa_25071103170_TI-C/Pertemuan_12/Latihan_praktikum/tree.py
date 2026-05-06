# Binary Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Binary_Tree:
    def __init__(self):
        self.root = None
        pass

    #Membuat Node
    def insert_manual(self):
        self.root = Node('A')
        self.root.left = Node('B')
        self.root.right = Node('C')
        self.root.left.left = Node('D')
        self.root.left.right = Node('E')
        self.root.right.right = Node('F')

    #traversal pre-order (Root, kiri, kanan)
    def traverse_preorder(root):
        if root:
            print(root.data, end=" ")
            traverse_preorder(root.left)
            traverse_preorder(root.right)

    #traverse in-order (Kiri, root, kanan)
    def traverse_inorder(root):
        if root:
            traverse_inorder(root.left)
            print(root.data, end=" ")
            traverse_inorder(root.right)

    #traverse post-order (kiri, kanan, root)
    def traverse_postorder(root):
        if root:
            traverse_postorder(root.left)
            traverse_postorder(root.right)
            print(root.data, end=" ")

    #Leaf Node
    def get_leaf_Node(root):
        if root:
            if root.left is None and root.right is None:                
                print(root.data, end=" ")
            get_leaf_Node(root.left)
            get_leaf_Node(root.right)

#====================
#PROGRAM UTAMA
#====================

if __name__ =="__main__":
    print("SISTEM AUDIT DISTRIBUSI \"CEPAT SAMPAI\"")
    print("="*40)

    print("[INFO] Membangun Struktur Gudang...")
    root = insert_manual(self)
    print("[INFO] Struktur berhasil dibuat.\n")

    print("HASIL AUDIT: ")

    print("1. Pre-Order :", end='')
    traverse_preorder(root)

    print("\n2. In-Order: ", end='')
    traverse_inorder(root)

    print("\n3. Post-Order: ", end='')
    traverse_postorder(root)

    print("\n\n[DATA] Gudang Ujung (Leaf Node): ", end='')
    get_leaf_Node(root)

    print("\n" + "="*40)
    print("Audit Selesai!")



      
    