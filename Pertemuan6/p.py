#2
stok_gadget = [
    {'merk': 'Samsung', 'tipe': 'S23', 'harga': 12000000},
    {'merk': 'Oppo', 'tipe': 'Reno 10', 'harga': 6000000},
    {'merk': 'Xiaomi', 'tipe': 'Mi 13', 'harga': 10000000},
    {'merk': 'Iphone', 'tipe': '15 Pro', 'harga': 20000000},
]

def filter_harga(data, min_harga, max_harga):
    filtered_data = []
    for gadget in data:
        if min_harga <= gadget['harga'] <= max_harga:
            filtered_data.append(gadget)
    return filtered_data

min_harga = float(input("Masukkan batas bawah harga: "))
max_harga = float(input("Masukkan batas atas harga: "))

filtered_gadgets = filter_harga(stok_gadget, min_harga, max_harga)

if filtered_gadgets:
    for gadget in filtered_gadgets:
        print("Merk:", gadget['merk'])
        print("Tipe:", gadget['tipe'])
        print("Harga:", gadget['harga'])
        print()
else:
    print("Tidak ada gadget dalam rentang harga tersebut.")


#3
katalog = [
    {'merk': 'Samsung', 'tipe': 'S23', 'sn': 'SAM01', 'stok': 2},
    {'merk': 'Oppo', 'tipe': 'Reno 10', 'sn': 'OPP01', 'stok': 5}
]

daftar_merk = set()

def update_stok(katalog, sn_target, jumlah_tambah):
    for gadget in katalog:
        if gadget['sn'] == sn_target:
            if 'stok' not in gadget:
                gadget['stok'] = 0
            gadget['stok'] += jumlah_tambah
            daftar_merk.add(gadget['merk'])
            return

update_stok(katalog, 'SAM01', 3)
update_stok(katalog, 'OPP01', 2)
update_stok(katalog, 'VIVO', 1)

print(daftar_merk)


#4
skema_komisi = (
    (100000000, 10), # Penjualan >= 100jt -> Komisi 10%
    (50000000, 5), # Penjualan >= 50jt -> Komisi 5%
    (20000000, 2), # Penjualan >= 20jt -> Komisi 2%
    (0, 0) # Di bawah 20jt -> Tidak ada komisi
)

def hitung_komisi(total_penjualan, skema, index=0):
    if total_penjualan >= skema[index][0]:
        return skema[index][1]
    elif index < len(skema) - 1:
        return hitung_komisi(total_penjualan, skema, index + 1)
    else:
        return 0

nama_sales = input("Nama Sales: ")
total_penjualan = int(input("Total Penjualan: "))

persen_komisi = hitung_komisi(total_penjualan, skema_komisi)
nominal_komisi = total_penjualan * persen_komisi / 100

print(f"Nama Sales: {nama_sales}")
print(f"Total Penjualan: {total_penjualan}")
print(f"Persen Komisi: {persen_komisi}%")
print(f"Nominal Komisi: {nominal_komisi}")



#5
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