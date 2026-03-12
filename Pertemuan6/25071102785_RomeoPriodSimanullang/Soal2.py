'''
Soal 2. Filter Gadget Berdasarkan Range Harga

Deskripsi:
Pelanggan sering mencari gadget berdasarkan budget tertentu. Buatlah fitur filter harga.

Ketentuan Program:
Gunakan data katalog berikut (dapat ditulis langsung di kode):
    stok_gadget = [
      {'merk': 'Samsung', 'tipe': 'S23', 'harga': 12000000},
      {'merk': 'Oppo', 'tipe': 'Reno 10', 'harga': 6000000},
      {'merk': 'Xiaomi', 'tipe': 'Mi 13', 'harga': 10000000},
      {'merk': 'Iphone', 'tipe': '15 Pro', 'harga': 20000000},
      ]
1. Buat fungsi filter_harga(data, min_harga, max_harga) yang mengembalikan list gadget yang harganya masuk dalam rentang tersebut.
2. Jika tidak ada yang sesuai, kembalikan list kosong.
3. Di program utama, minta user input batas bawah dan batas atas harga, lalu 
tampilkan hasilnya. Jika kosong, tampilkan "Tidak ada gadget dalam rentang harga tersebut."
''' 
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