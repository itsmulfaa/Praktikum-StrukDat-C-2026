ukm_coding = {"Andi", "Budi", "Caca", "Deni"}
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"}

hanya_coding = ukm_coding - ukm_robotik
print("Mahasiswa yang hanya mendaftar ukm coding saja:", hanya_coding)

mahasiswa_unik = ukm_coding.union(ukm_robotik)
print("Mahasiswa unik yang mendaftar", mahasiswa_unik)

if "Andi" in ukm_robotik:
    print(True)


