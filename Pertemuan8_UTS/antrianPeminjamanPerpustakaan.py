pengunjung_hari_ini = [
{"id": "M001", "nama": "Rina", "usia": 20, "kategori": "Fiksi",
"kembali": False},
{"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains",
"kembali": True},
{"id": "M003", "nama": "Siti", "usia": 19, "kategori": "Fiksi",
"kembali": False},
{"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum",
"kembali": True},
{"id": "M005", "nama": "Yuni", "usia": 18, "kategori": "Sains",
"kembali": False},
{"id": "M006", "nama": "Bagas", "usia": 22, "kategori": "Hukum",
"kembali": False},
]


'''
saol 1 List dan Dictionary
Buat dua fungsi berikut:
  1. tampilkan_pengunjung() — Tampilkan semua data pengunjung dalam format tabel.
  2. filter_belum_kembali() — Kembalikan list berisi nama-nama pengunjung yang belum mengembalikan buku, lalu tampilkan total jumlah mereka.
Ketentuan tambahan:
  • Urutkan hasil filter_belum_kembali() berdasarkan nama secara alfabetis A-Z sebelum ditampilkan. Gunakan metode sorting pada list.
  • Gunakan list comprehension untuk mengambil data pengunjung yang belum mengembalikan buku.

  Contoh Output:
===== DATA PENGUNJUNG PERPUSTAKAAN =====
No | ID | Nama | Usia | Kategori | Status Kembali
---+------+--------+------+----------+---------------
1 | M001 | Rina | 20 | Fiksi | Belum Kembali
2 | M002 | Hendra | 23 | Sains | Sudah Kembali
3 | M003 | Siti | 19 | Fiksi | Belum Kembali
4 | M004 | Taufik | 21 | Hukum | Sudah Kembali
5 | M005 | Yuni | 18 | Sains | Belum Kembali
6 | M006 | Bagas | 22 | Hukum | Belum Kembali
===== PENGUNJUNG BELUM KEMBALI =====
1. Bagas
2. Rina
3. Siti
4. Yuni
Total belum kembali: 4 pengunjung
'''
def tampilkan_pengunjung(pengunjung):
    print("===== DATA PENGUNJUNG PERPUSTAKAAN =====")
    print("No | ID | Nama | Usia | Kategori | Status Kembali")
    print("---+------+--------+------+----------+---------------")
    for index, data in enumerate(pengunjung, start=1):
        status = "Belum Kembali" if not data['kembali'] else "Sudah Kembali"
        print(f"{index} | {data['id']} | {data['nama']} | {data['usia']} | {data['kategori']} | {status}")

def filter_belum_kembali(pengunjung):
    belum_kembali = [data['nama'] for data in pengunjung if not data['kembali']]
    belum_kembali.sort()
    return belum_kembali
tampilkan_pengunjung(pengunjung_hari_ini)
belum_kembali_list = filter_belum_kembali(pengunjung_hari_ini)
print("===== PENGUNJUNG BELUM KEMBALI =====")
for index, nama in enumerate(belum_kembali_list, start=1):
    print(f"{index}. {nama}")
print(f"Total belum kembali: {len(belum_kembali_list)} pengunjung")





'''
Soal 2 - Tuple dan Set
Buat dua fungsi berikut:
  1. info_perpustakaan() — Kembalikan informasi tetap perpustakaan menggunakan tuple lalu tampilkan isinya.
  2. rekap_kategori() — Gunakan set untuk mendapatkan kategori buku unik, lalu hitung jumlah pengunjung per kategori menggunakan dictionary.
Ketentuan tambahan:
  • Dari hasil rekap, tampilkan kategori buku dengan jumlah pengunjung terbanyak.
  • Jika ada lebih dari satu kategori dengan jumlah yang sama, tampilkan semuanya.

Contoh Output:
Info Perpustakaan:
Nama : Perpustakaan Kampus Terpadu
Alamat : Jl. Pendidikan No. 5, Pekanbaru
Telp : 0761-54321
Kategori Buku Unik: {'Fiksi', 'Sains', 'Hukum'}
Jumlah kategori: 3
Rekap per kategori:
Fiksi : 2 pengunjung
Sains : 2 pengunjung
Hukum : 2 pengunjung
Kategori terbanyak: Fiksi, Sains, Hukum (2 pengunjung)
'''
def info_perpustakaan():
    info = (
        "Perpustakaan Kampus Terpadu",
        "Jl. Pendidikan No. 5, Pekanbaru",
        "0761-54321"
    )
    return info

def rekap_kategori(pengunjung):
    kategori_unik = set(pengunjung['kategori'] for pengunjung in pengunjung)
    rekap = {}
    for kategori in kategori_unik:
        jumlah_pengunjung = sum(1 for pengunjung in pengunjung if pengunjung['kategori'] == kategori)
        rekap[kategori] = jumlah_pengunjung
    return rekap

info_perpustakaan = info_perpustakaan()
rekap_kategori = rekap_kategori(pengunjung_hari_ini)
print("Info Perpustakaan:")
print(f"Nama : {info_perpustakaan[0]}")
print(f"Alamat : {info_perpustakaan[1]}")
print(f"Telp : {info_perpustakaan[2]}")
print("Kategori Buku Unik:", rekap_kategori)
print("Jumlah kategori:", len(rekap_kategori))
print("Rekap per kategori:")
for kategori, jumlah_pengunjung in rekap_kategori.items():
    print(f"{kategori} : {jumlah_pengunjung} pengunjung")
kategori_terbanyak = max(rekap_kategori, key=rekap_kategori.get)
print(f"Kategori terbanyak: {kategori_terbanyak}, {rekap_kategori[kategori_terbanyak]} pengunjung")





'''
Soal 3 - OOP
Buat class Pengunjung dan class turunannya PengunjungPrioritas dengan ketentuan berikut:
  Class Pengunjung:
    - Atribut private: __id, __nama, __kategori
    - Getter untuk setiap atribut
    - Method tampilkan_info()
    - Method static hitung_pengunjung() -> mengembalikan total objek Pengunjung
    yang sudah dibuat (gunakan class variable sebagai counter)

  Class PengunjungPrioritas (turunan Pengunjung):
    - Tambahkan atribut: prioritas ("Mendesak" / "Biasa")
    - Override tampilkan_info() untuk menyertakan info prioritas
    - Jika prioritas = "Mendesak", tampilkan pesan peringatan: "** Layani segera! **"

    Contoh Output:
    ID : M001
    Nama : Rina
    Kategori : Fiksi
    ID : M007
    Nama : Gilang
    Kategori : Referensi
    Prioritas : Mendesak
    ** Layani segera! **
    Total pengunjung terdaftar: 2
'''
class Pengunjung:
    def __init__(self, id, nama, kategori):
        self.__id = id
        self.__nama = nama
        self.__kategori = kategori
        Pengunjung._hitung_pengunjung = 0
        Pengunjung._hitung_pengunjung += 1

    def get_id(self):
        return self.__id

    def get_nama(self):
        return self.__nama

    def get_kategori(self):
        return self.__kategori

    def tampilkan_info(self):
        print(f"ID : {self.__id}")
        print(f"Nama : {self.__nama}")
        print(f"Kategori : {self.__kategori}")

    @staticmethod
    def hitung_pengunjung():
        return Pengunjung._hitung_pengunjung

class PengunjungPrioritas(Pengunjung):
    def __init__(self, id, nama, kategori, prioritas):
        super().__init__(id, nama, kategori)
        self.prioritas = prioritas
        Pengunjung._hitung_pengunjung += 1

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Prioritas : {self.prioritas}")
        if self.prioritas == "Mendesak":
            print("** Layani segera! **")

pengunjung1 = Pengunjung("M001", "Rina", "Fiksi")
pengunjung2 = PengunjungPrioritas("M007", "Gilang", "Referensi", "Mendesak")

pengunjung1.tampilkan_info()
pengunjung2.tampilkan_info()

print(f"Total pengunjung terdaftar: {Pengunjung.hitung_pengunjung()}")





'''
Soal 4 - Single Linked List: Antrian Peminjaman
Perpustakaan menggunakan Single Linked List untuk mengatur antrian layanan petugas.
Pengunjung yang datang lebih awal akan dilayani lebih dulu (FIFO).

Buat class Node dan class AntrianPeminjaman dengan method berikut:
Class Node:
  - data : dictionary {"id", "nama", "kategori"}
  - next : pointer ke node berikutnya
Class AntrianPeminjaman:
  - head : node pertama
  - tambah(data) -> tambah pengunjung di akhir antrian
  - tampilkan() -> tampilkan seluruh antrian beserta posisinya
  - panggil_berikutnya() -> hapus dan tampilkan pengunjung paling depan
  - cari(nama) -> cari pengunjung berdasarkan nama, tampilkan posisinya
  - hapus_berdasarkan_id(id) -> hapus pengunjung berdasarkan ID di mana saja posisinya dalam antrian
  - hitung() -> kembalikan jumlah pengunjung dalam antrian

Ketentuan tambahan:
Method hapus_berdasarkan_id() harus menangani 3 kasus:
  ○ Pengunjung ada di posisi pertama (head)
  ○ Pengunjung ada di tengah atau akhir
  ○ ID tidak ditemukan dalam antrian

Contoh Input:
antrian = AntrianPeminjaman()
antrian.tambah({"id": "M001", "nama": "Rina", "kategori": "Fiksi"})
antrian.tambah({"id": "M002", "nama": "Hendra", "kategori": "Sains"})
antrian.tambah({"id": "M003", "nama": "Siti", "kategori": "Fiksi"})
antrian.tambah({"id": "M004", "nama": "Taufik", "kategori": "Hukum"})
antrian.tampilkan()
antrian.panggil_berikutnya()
antrian.tampilkan()
antrian.hapus_berdasarkan_id("M003")
antrian.tampilkan()
antrian.cari("Taufik")
print("Total antrian:", antrian.hitung())

Contoh Output:
===== ANTRIAN PEMINJAMAN =====
[1] M001 - Rina | Fiksi
[2] M002 - Hendra | Sains
[3] M003 - Siti | Fiksi
[4] M004 - Taufik | Hukum
Total antrian: 4
Memanggil pengunjung berikutnya...
Silakan masuk: Rina (M001) - Fiksi
===== ANTRIAN PEMINJAMAN =====
[1] M002 - Hendra | Sains
[2] M003 - Siti | Fiksi
[3] M004 - Taufik | Hukum
Total antrian: 3
Menghapus pengunjung dengan ID M003...
Siti (M003) berhasil dihapus dari antrian.
===== ANTRIAN PEMINJAMAN =====
[1] M002 - Hendra | Sains
[2] M004 - Taufik | Hukum
Total antrian: 2
Mencari 'Taufik'...
Ditemukan: M004 - Taufik | Hukum (posisi ke-2)
Total antrian: 2
'''

