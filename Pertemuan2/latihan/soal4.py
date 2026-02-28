'''
4. Data nilai mahasiswa disimpan dalam format berikut:
nilai_siswa = {
"S01": {"nama": "Dina", "tugas": 80, "uts": 75,
"uas": 85},
"S02": {"nama": "Abdul Harris", "tugas": 90, "uts":
88, "uas": 92},
"S03": {"nama": "Sheila", "tugas": 70, "uts": 65,
"uas": 70}
}
1. Tambahkan data siswa baru: "S04" dengan nama "Fafa", nilai tugas 85, UTS
80, dan UAS 90.

2. Hitunglah nilai akhir setiap siswa dengan bobot: (Tugas 20% + UTS 30% +
UAS 50%) dan tampilkan hasilnya.
3. Tampilkan nama siswa yang memiliki nilai UAS di atas 80.
'''
nilai_siswa = {
    "S01": {"nama": "Dina", "tugas": 80, "uts": 75, "uas": 85},
    "S02": {"nama": "Abdul Harris", "tugas": 90 , "uts": 88, "uas": 92},
    "S03": {"nama": "Sheila", "tugas": 70, "uts": 65, "uas": 70}
}
# 1. Tambahkan data siswa baru: "S04" dengan nama "Fafa", nilai tugas 85, UTS 80, dan UAS 90.
nilai_siswa["S04"] = {"nama": "Fafa", "tugas": 85, "uts": 80, "uas": 90}

# 2. Hitunglah nilai akhir setiap siswa dengan bobot: (Tugas 20% + UTS 30% + UAS 50%) dan tampilkan hasilnya.
for siswa_id, data in nilai_siswa.items():
    nilai_akhir = (data["tugas"] * 0.2) + (data["uts"] * 0.3) + (data["uas"] * 0.5)
    print(f"Nilai akhir {data['nama']} (ID: {siswa_id}): {nilai_akhir}")

# 3. Tampilkan nama siswa yang memiliki nilai UAS di atas 80.
print("Siswa dengan nilai UAS di atas 80:")
for data in nilai_siswa.values():
    if data["uas"] > 80:
        print(data["nama"])