class BangunDatar:
    def __init__(self, nama):
        self.nama = nama

class Persegi(BangunDatar):
    def __init__(self, nama, sisi):
        super().__init__(nama)
        self.sisi = sisi

    def luas(self):
        return self.sisi ** 2

class Segitiga(BangunDatar):
    def __init__(self, nama, alas, tinggi):
        super().__init__(nama)
        self.alas = alas
        self.tinggi = tinggi

    def luas(self):
        return 0.5 * self.alas * self.tinggi

list_bangun_datar = []

def tampilkan_list_data():
    print('List Data:')
    for idx, bangun_datar in enumerate(list_bangun_datar):
        if isinstance(bangun_datar, Persegi):
            print(f"Nama: {bangun_datar.nama}")
            print(f"Sisi: {bangun_datar.sisi} cm")
            print(f"Luas: {bangun_datar.luas()} cm2")
        elif isinstance(bangun_datar, Segitiga):
            print(f"Nama: {bangun_datar.nama}")
            print(f"Alas: {bangun_datar.alas} cm")
            print(f"Tinggi: {bangun_datar.tinggi} cm")
            print(f"Luas: {bangun_datar.luas()} cm2")

def main():
    while True:
        print("\nMenu:")
        print("1. Masukan Data")
        print("2. Tampilkan List Data")
        print("3. Hapus Data")
        print("4. Keluar")
        pilih_menu = int(input("Masukkan Pilihan Menu: "))

        if pilih_menu == 1:
            nama = input("Masukkan Nama Bangun Datar: ")
            tipe = input("Masukkan Tipe Bangun Datar (Persegi / Segitiga): ")
            if tipe == "Persegi":
                sisi = float(input("Masukkan Sisi: "))
                bangun_datar = Persegi(nama, sisi)
                list_bangun_datar.append(bangun_datar)
            elif tipe == "Segitiga":
                alas = float(input("Masukkan Alas: "))
                tinggi = float(input("Masukkan Tinggi: "))
                bangun_datar = Segitiga(nama, alas, tinggi)
                list_bangun_datar.append(bangun_datar)
            else:
                print("Tipe Bangun datar yang anda masukkan tidak valid")
        elif pilih_menu == 2:
            index = int(input("Masukkan indeks yang akan ditampilkan: "))
            if 0 <= index < len(list_bangun_datar):
                bangun_datar = list_bangun_datar[index]
                if isinstance(bangun_datar, Persegi):
                    print(f"Indeks: {index}")
                    print(f"Nama: {bangun_datar.nama}")
                    print(f"Sisi: {bangun_datar.sisi} cm")
                    print(f"Luas: {bangun_datar.luas()} cm2")
                elif isinstance(bangun_datar, Segitiga):
                    print(f"Indeks: {index}")
                    print(f"Nama: {bangun_datar.nama}")
                    print(f"Alas: {bangun_datar.alas} cm")
                    print(f"Tinggi: {bangun_datar.tinggi} cm")
                    print(f"Luas: {bangun_datar.luas()} cm2")
            else:
                print("Indeks Tidak valid")
        elif pilih_menu == 3:
            tampilkan_list_data()
            index = int(input("Masukkan indeks yang akan dihapus: "))
            if 0 <= index < len(list_bangun_datar):
                del list_bangun_datar[index]
                print("Data Berhasil Dihapus")
            else:
                print("Indeks Tidak valid")
        elif pilih_menu == 4:
            print("Keluar Dari Program")
            break
        else:
            print("Menu tidak valid")

if __name__ == "__main__":
    main()
