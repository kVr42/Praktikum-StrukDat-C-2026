'''
Soal 5. Integrasi Sistem PyGadget Hub
Deskripsi:
Gabungkan seluruh komponen dari soal 1 hingga 4 menjadi satu aplikasi manajemen toko 
gadget yang utuh. Gunakan perulangan while dan if-elif-else untuk navigasi menu.
Ketentuan Program:
Program menampilkan menu berikut dan berjalan dalam perulangan hingga user memilih 
menu 5:
    === PyGadget Hub ===
    1. Tambah Gadget
    2. Daftar Inventaris
    3. Update Stok
    4. Cek Komisi
    5. Keluar

1. Menu 1 - Tambah Gadget: Memanggil fungsi registrasi_gadget() dan simpan hasilnya ke inventaris.
2. Menu 2 - Daftar Inventaris: Menampilkan tabel produk (Merk, Tipe, Harga, SN, Stok) menggunakan f-string.
3. Menu 3 - Update Stok: Memanggil prosedur update_stok() dan simpan ke katalog.
4. Menu 4 - Cek Komisi: Memanggil fungsi rekursif hitung_komisi().
5. Menu 5 - Keluar: Hentikan program dengan menampilkan pesan perpisahan kepada user
'''

import Soal1, Soal2, Soal3, Soal4

while True:
    print("\n=== PyGadget Hub ===")
    print("1. Tambah Gadget")
    print("2. Daftar Inventaris")
    print("3. Update Stok")
    print("4. Cek Komisi")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        Soal1.registrasi_gadget()
    elif pilihan == "2":
        Soal2.daftar_inventaris()
    elif pilihan == "3":
        Soal3.update_stok()
    elif pilihan == "4":
        Soal4.cek_komisi()
    elif pilihan == "5":
        print("Terima kasih telah menggunakan PyGadget Hub! Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
