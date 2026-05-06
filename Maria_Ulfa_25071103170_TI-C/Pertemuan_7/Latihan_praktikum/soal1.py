
def pisahkan_plat(plat_list):
    ganjil = []
    genap = []

    for plat in plat_list:
        bagian = plat.split()      #memisahkan string
        angka = bagian[1]         
        digit_terakhir = int(angka[-1])  

        if digit_terakhir % 2 == 0:
            genap.append(plat)
        else:
            ganjil.append(plat)

    return ganjil, genap


data =  ["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"]

ganjil, genap = pisahkan_plat(data)

print("Plat Ganjil:", ganjil)
print("Plat Genap:", genap)


