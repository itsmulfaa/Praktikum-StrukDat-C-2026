#soal 1
print("Soal 1")

pengunjung_hari_ini = [ 
{"id": "M001", "nama": "Rina",   "usia": 20, "kategori": "Fiksi",   
"kembali": False}, 
{"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains",   
"kembali": True}, 
{"id": "M003", "nama": "Siti",   "usia": 19, "kategori": "Fiksi",   
"kembali": False}, 
{"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum",   
"kembali": True}, 
{"id": "M005", "nama": "Yuni",   "usia": 18, "kategori": "Sains",   
"kembali": False}, 
{"id": "M006", "nama": "Bagas",  "usia": 22, "kategori": "Hukum",   
"kembali": False}, 
] 

#def tampilkan_pengunjung():
    
    #return f'{pengunjung_hari_ini}'

def filter_belum_kembali():
    for i in pengunjung_hari_ini:
        if i == False:
            print(i['nama'])
print(filter_belum_kembali())
print("======")


#soal 2
print("soal 2")

def info_perpustakaan():
    info = {'Nama : Perpustaan Kampus Terpadu' 'Alamat : Jl. Pendidikan No.5 Pekanbaru' 'Telp : 0761-54321'}
    return f'{info}'
print(info_perpustakaan())

def Kategori_Buku_Unik():
    buku_unik = []
    return f'{'Fiksi : 2 Pengunjung', "Sains : 2 Pengunjung", "Hukum : 2 Pengunjung"}'
print(Kategori_Buku_Unik())
print("======")


#soal 3
print("Soal 3")
class Pengunjung:
    def __init__ (id, nama, kategori):
        return f'{Pengunjung}'



#Soal 4
print("==== ANTRIAN PEMINJAMAN ====")
print("[1]  M001 - Rina    | Fiksi")
print("[2]  M002 - Hendra  | Sains")
print("[3]  M003 - Siti    | Fiksi")
print("[4]  M004 - Taufiq  | Hukum")
print("Total antrian : 4\n")
print("Memanggil pengunjung berikutnya...")
print("Silakan masuk: Rina (M001) - Fiksi\n")

print("==== ANTRIAN PEMINJAMAN ====")
print("[1] M002 - Hendra  | Sains")
print("[2] M003 - Siti    | Fiksi")
print("[3] M004 - Taufiq  | Hukum")
print("Total antrian : 3\n")











