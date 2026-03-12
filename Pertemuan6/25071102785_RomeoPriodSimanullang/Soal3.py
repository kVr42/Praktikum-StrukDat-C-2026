'''
Soal 3. Prosedur Update Stok dan Brand Unique
Deskripsi:
Buat prosedur untuk memperbarui stok setelah pengiriman barang baru datang dan 
mencatat merk apa saja yang tersedia.

Ketentuan Program:
Gunakan data katalog ini:
katalog = [ {'merk': 'Samsung', 'tipe': 'S23', 'sn': 'SAM01', 'stok': 2}, {'merk': 'Oppo', 'tipe': 'Reno 10', 'sn': 'OPP01', 'stok': 5} ]

  1. Buat prosedur update_stok(katalog, sn_target, jumlah_tambah). Cari gadget berdasarkan sn.
  2. Jika sn ditemukan, tambahkan nilai stoknya (tambahkan key stok jika belum ada di dictionary tersebut).
  3. Gunakan set bernama daftar_merk untuk menyimpan semua merk unik yang ada di katalog.
  4. Lakukan pemanggilan prosedur ini sebanyak 3 kali di program utama dengan input berbeda, lalu tampilkan daftar_merk.
'''

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
