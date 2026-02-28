'''
2. Diberikan list berisi tuple data mahasiswa dan poin keaktifan: data_aktivitas = [("Diki",
88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)]
a. Lakukan perulangan pada list tersebut. Jika poin > 80, tampilkan: "[Nama]
mendapatkan predikat Gold". Jika poin 50-80, tampilkan: "[Nama] mendapatkan
predikat Silver". Di bawah itu, tampilkan: "[Nama] mendapatkan predikat Bronze"
'''
data_aktivitas = [("Diki", 88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)]

for nama, poin in data_aktivitas:
  if poin > 80:
    print(f"{nama} mendapatkan predikat Gold")
  elif poin >= 50:
    print(f"{nama} mendapatkan predikat Silver")
  else:
    print(f"{nama} mendapatkan predikat Bronze")