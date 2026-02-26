class BankAccount:
    def __init__(self, nama, nomor, saldo):
        self.nama = nama
        self.nomor = nomor
        self.saldo = saldo

    def tampil_info(self):
        return "Nama: {nama}, Nomor: {nomor}, Saldo: {saldo}"

    def ubah_nomor(self, nomor_baru):
        self.nomor_baru = nomor_baru

    def tampil_akhir(self):
        return f"Nama: {self.nama}, Nomor: {self.nomor}, Saldo: {self.saldo}, Nomor_baru: {self.nomor_baru}"
      
p1 = BankAccount("Rani", "01", "500000")
print(p1.tampil_info())
p1.ubah_nomor("04")
print(p1.tampil_akhir())




    






