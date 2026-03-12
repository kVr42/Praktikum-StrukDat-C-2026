'''
1. Case: Sebuah sistem parkir mencatat plat nomor kendaraan yang masuk dalamsebuah array. Kamu diminta untuk memisahkan kendaraan berdasarkan aturan ganjil-genap.
a. Input: ["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"]
b. Tugas:
  1. Buat fungsi yang menerima array tersebut.
  2. Identifikasi angka terakhir pada plat nomor (abaikan huruf dibelakang).
  3. Pisahkan menjadi dua array baru: ganjil dan genap.
c. Logika: Mengambil karakter angka terakhir dari string dan menggunakan operator modulus (%).
'''

'''
plat_nomor = []
for i in range(4):
    plat = input("Masukkan plat nomor kendaraan: ")
plat_nomor.append(plat)
'''

def pisahkan_ganjil_genap(plat_array):
    ganjil = []
    genap = []

    for plat in plat_array:
        bagian = plat.split() 
        angka = bagian[1]
        digit_terakhir = int(angka[-1])

        if digit_terakhir % 2 == 0:
            genap.append(plat)
        else:
            ganjil.append(plat)

    return ganjil, genap


platnomor = ["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"]


ganjil, genap = pisahkan_ganjil_genap(plat_nomor)

print("Plat Ganjil:", ganjil)
print("Plat Genap:", genap)