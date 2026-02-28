'''
3. Terdapat dua set yang berisi daftar keahlian (skill) dari dua tim pengembang:
tim_frontend = {"HTML", "CSS", "JavaScript", "React"}
tim_backend = {"Python", "JavaScript", "SQL",
"NodeJS"}
  1. Tentukan keahlian yang dimiliki oleh kedua tim (irisan).
  2. Tentukan keahlian yang hanya dimiliki oleh tim_backend.
  3. Gabungkan kedua set tersebut untuk melihat daftar total keahlian unik yang
  tersedia di perusahaan.
'''
tim_frontend = {"HTML", "CSS", "JavaScript", "React"}
tim_backend = {"Python", "JavaScript", "SQL", "NodeJS"}

# 1. Tentukan keahlian yang dimiliki oleh kedua tim (irisan).
irisan = tim_frontend.intersection(tim_backend)
print("Keahlian yang dimiliki oleh kedua tim:", irisan)

# 2. Tentukan keahlian yang hanya dimiliki oleh tim_backend.
hanya_backend = tim_backend.difference(tim_frontend)
print("Keahlian yang hanya dimiliki oleh tim backend:", hanya_backend)

# 3. Gabungkan kedua set tersebut untuk melihat daftar total keahlian unik yang tersedia di perusahaan.
total_keahlian = tim_frontend.union(tim_backend)
print("Total keahlian unik di perusahaan:", total_keahlian)