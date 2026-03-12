'''
Soal 4. Perhitungan Komisi Sales Bertingkat (Rekursi)
Deskripsi:
PyGadget Hub memberikan komisi kepada sales berdasarkan total penjualan bulanan. 
Persentase komisi disimpan dalam sebuah Tuple of Tuples yang diurutkan dari target 
tertinggi ke terendah.
Ketentuan Program:
Gunakan data skema_komisi berikut:
  skema_komisi = (
    (100000000, 10), # Penjualan >= 100jt -> Komisi 10%
    (50000000, 5), # Penjualan >= 50jt -> Komisi 5%
    (20000000, 2), # Penjualan >= 20jt -> Komisi 2%
    (0, 0) # Di bawah 20jt -> Tidak ada komisi
  )
1. Buat fungsi rekursif hitung_komisi(total_penjualan, skema, index=0) yang memeriksa setiap elemen dalam tuple skema mulai dari index 0.
2. Jika total_penjualan lebih besar atau sama dengan target di skema[index][0], maka kembalikan nilai persen komisi tersebut.
3. Jika belum memenuhi target di index tersebut, panggil fungsi yang sama dengan index + 1.
4. Di program utama, minta input Nama Sales dan Total Penjualan.
5. Hitung Nominal Komisi (Total Penjualan * Persen / 100) dan tampilkan rinciannya
'''

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

cek_komisi = persen_komisi

if cek_komisi == 0:
    print("Tidak ada komisi")
else:
    print(f"Persen Komisi: {persen_komisi}%")
    print(f"Nominal Komisi: {nominal_komisi}")