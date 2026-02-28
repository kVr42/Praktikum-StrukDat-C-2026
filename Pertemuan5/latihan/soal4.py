'''
4. Diberikan data produk dalam bentuk list of dictionaries:
gudang_pc = [
 {"item": "Monitor", "harga": 1500000, "stok": 5},
 {"item": "Keyboard", "harga": 400000, "stok": 12},
 {"item": "Mouse", "harga": 250000, "stok": 20}
]
a. Tambahkan satu key baru bernama "kategori" dengan nilai "Aksesoris" untuk produk 
Keyboard.
b. Tambahkan satu item baru: "Headset" dengan harga 350000 dan stok 8.
c. Hitung Total Nilai Aset (Harga x Stok) untuk setiap item. Tampilkan output dengan 
format:
Item: [Nama] | Total Aset: Rp [Hasil Perkalian]
'''
gudang_pc = [
 {"item": "Monitor", "harga": 1500000, "stok": 5},
 {"item": "Keyboard", "harga": 400000, "stok": 12},
 {"item": "Mouse", "harga": 250000, "stok": 20}
]
# a. Tambahkan satu key baru bernama "kategori" dengan nilai "Aksesoris" untuk produk Keyboard.
gudang_pc[1]["kategori"] = "Aksesoris"
print(gudang_pc)

# b. Tambahkan satu item baru: "Headset" dengan harga 350000 dan stok 8.
gudang_pc.append({"item": "Headset", "harga": 350000, "stok": 8})
print("Barang baru telah ditambahkan cuy:", gudang_pc[-1])

# c. Hitung Total Nilai Aset (Harga x Stok) untuk setiap item. Tampilkan output dengan format: Item: [Nama] | Total Aset: Rp [Hasil Perkalian]
for item in gudang_pc:
    total_aset = item["harga"] * item["stok"]
    print(f"Item: {item['item']} | Total Aset: Rp {total_aset}")