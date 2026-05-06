# =========================
# Class Node
# =========================
class Node:
    def __init__(self, nama, keluhan, nomor):
        self.nama = nama
        self.keluhan = keluhan
        self.nomor = nomor
        self.next = None


# =========================
# Class Queue
# =========================
class QueueLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
        self.next_number = 1  # nomor antrian berikutnya

    def is_empty(self):
        return self.head is None

    def enqueue(self, nama, keluhan):
        node = Node(nama.upper(), keluhan, self.next_number)

        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        print(f"[DAFTAR] {node.nama.title()} terdaftar dengan keluhan: {keluhan} (No. Antrian: {node.nomor})")

        self._size += 1
        self.next_number += 1

    def dequeue(self):
        if self.is_empty():
            return

        removed = self.head
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        print(f"[PANGGIL] Dokter memanggil: {removed.nama} (keluhan: {removed.keluhan})")

        self._size -= 1

    def peek(self):
        if not self.is_empty():
            print(f"[PEEK] Pasien berikutnya: {self.head.nama} -> {self.head.keluhan}")

    def size(self):
        return self._size

    def display(self):
        print("[ANTRIAN SAAT INI]")
        current = self.head
        nomor = 1

        while current:
            print(f"{nomor}. {current.nama} -> {current.keluhan}")
            current = current.next
            nomor += 1

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0
        print("[CLEAR] Sesi poliklinik selesai. Antrian dikosongkan.")


# =========================
# SIMULASI 
# =========================

print("====================================")
print("SISTEM ANTRIAN POLI UMUM")
print("RS Sehat Bersama")
print("====================================\n")

queue = QueueLinkedList()

# Cek kosong
if queue.is_empty():
    print("[CEK] Apakah antrian kosong? -> YA, antrian masih kosong.")

# Daftar pasien
queue.enqueue("Budi", "demam tinggi")
queue.enqueue("Ani", "batuk pilek")
queue.enqueue("Citra", "sakit kepala")

# Jumlah pasien
print(f"[INFO] Jumlah pasien menunggu: {queue.size()} orang")

# Peek
queue.peek()

# Panggil pasien
queue.dequeue()

# Tambah pasien lagi
queue.enqueue("Dodi", "nyeri perut")

# Tampilkan antrian
queue.display()

# Panggil pasien lagi
queue.dequeue()

# Info jumlah
print(f"[INFO] Jumlah pasien masih menunggu: {queue.size()} orang")

# Clear
queue.clear()

# Cek kosong lagi
if queue.is_empty():
    print("[CEK] Apakah antrian kosong? -> YA, antrian sudah kosong.")

print("\n====================================")
print("Simulasi Selesai!")
print("====================================")