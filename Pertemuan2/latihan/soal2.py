'''
2. Diberikan sebuah tuple barang:
barang = ("B001", "Laptop Gaming", 15000000)
1. Akses dan tampilkan harga barang dari tuple tersebut.
2. Cobalah untuk mengubah harga barang menjadi 14000000. Jelaskan dalam
komentar kode mengapa hal ini menyebabkan error (Gunakan comment).
3. Gunakan teknik unpacking untuk memasukkan isi tuple ke dalam tiga
variabel: kode, nama, dan harga.
'''
barang = ("B001", "Laptop Gaming", 15000000)
# 1. Akses dan tampilkan harga barang dari tuple tersebut.  
harga = barang[2]
print("Harga barang:", harga)

# 2. Cobalah untuk mengubah harga barang menjadi 14000000.
# barang[2] = 14000000
# Error terjadi karena tuple bersifat immutable, artinya isi dari tuple tidak dapat diubah setelah dibuat.

# 3. Gunakan teknik unpacking untuk memasukkan isi tuple ke dalam tiga
# variabel: kode, nama, dan harga. 
kode, nama, harga = barang
print("Kode:", kode)
print("Nama:", nama)
print("Harga:", harga)

