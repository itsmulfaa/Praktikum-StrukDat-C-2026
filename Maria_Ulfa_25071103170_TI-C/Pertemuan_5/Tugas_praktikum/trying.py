def cek_kelulusan(nama, nilai):
    if nilai >= 75:
        print("Nama :", nama)
        print("Status : Lulus")
    else:
        print("Nama :", nama)
        print("Status : Tidak Lulus")

# Pemanggilan
cek_kelulusan("Maria", 80)