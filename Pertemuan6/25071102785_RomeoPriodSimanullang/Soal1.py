'''
Soal 1. Fungsi Registrasi Produk dengan Serial Number
Topik: Fungsi, Return Value, Dictionary, String Validation
Deskripsi:
PyGadget Hub memerlukan fungsi untuk mendaftarkan produk baru. Setiap produk harus 
memiliki Serial Number (SN) unik.
Ketentuan Program:
1.Buat fungsi registrasi_gadget(merk, tipe, harga, sn) yang menerima 4 parameter.
  Merk(string), tipe(string), harga(float), sn(string)
2. Validasi input:
  • Harga harus di atas 1.000.000.
  • sn (Serial Number) harus berisi minimal 5 karakter.
  • Jika tidak valid, cetak pesan error spesifik dan kembalikan None.
3. Jika valid, kembalikan dictionary dengan key: merk, tipe, harga, sn, dan status (default: "Tersedia").
4. Di program utama, gunakan perulangan untuk input 3 gadget, simpan ke dalam list inventaris, dan tampilkan di akhir.
'''

def registrasi_gadget(merk, tipe, harga, sn):
    if harga < 1000000:
        print("Harga harus di atas 1.000.000.")
        return None
    if len(sn) < 5:
        print("SN harus berisi minimal 5 karakter.")
        return None
    return {"merk": merk, "tipe": tipe, "harga": harga, "sn": sn, "status": "Tersedia"}

inventaris = []
for i in range(3):
    merk = input("Merk: ")
    tipe = input("Tipe: ")
    harga = float(input("Harga: "))
    sn = input("SN: ")
    gadget = registrasi_gadget(merk, tipe, harga, sn)
    if gadget is not None:
        inventaris.append(gadget)

for gadget in inventaris:
    print("Merk:", gadget["merk"])
    print("Tipe:", gadget["tipe"])
    print("Harga:", gadget["harga"])
    print("SN:", gadget["sn"])
    print("Status:", gadget["status"])
    print()