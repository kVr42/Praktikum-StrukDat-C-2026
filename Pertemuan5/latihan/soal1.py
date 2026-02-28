'''
1. Diberikan list stok barang di gudang: stok_barang = [15, 40, 30, 10, 25]
  a. Temukan indeks dari nilai 10, lalu ubah nilai pada indeks tersebut menjadi 50.
  b. Tambahkan nilai 5 ke akhir list, kemudian urutkan list secara descending (besar ke 
  kecil).
  c. Tampilkan jumlah total seluruh nilai dalam list tersebut.
  d. Gunakan shorthand if (ternary) untuk menampilkan "Stok Aman" jika rata-rata nilai 
  dalam list > 20, jika tidak tampilkan "Waspada".
'''
stok_barang = [15, 40, 30, 10, 25]

# a. Temukan indeks dari nilai 10, lalu ubah nilai pada indeks tersebut menjadi 50.
indeks = stok_barang.index(10)
stok_barang[indeks] = 50
print("List setelah mengubah nilai 10 menjadi 50:", stok_barang)

# b. Tambahkan nilai 5 ke akhir list, kemudian urutkan list secara descending (besar ke kecil).
stok_barang.append(5)
stok_barang.sort(reverse=True)
print("List setelah menambahkan nilai 5 dan mengurutkannya secara descending:", stok_barang)

# c. Tampilkan jumlah total seluruh nilai dalam list tersebut.
total = sum(stok_barang)
print("Jumlah total seluruh nilai dalam list:", total)

# d. Gunakan shorthand if (ternary) untuk menampilkan "Stok Aman" jika rata-rata nilai dalam list > 20, jika tidak tampilkan "Waspada".
print('stok aman') if (sum(stok_barang) / len(stok_barang)) > 20 else print('waspada')