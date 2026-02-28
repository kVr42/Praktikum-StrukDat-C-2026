'''
3. Terdapat dua data pendaftar UKM (Unit Kegiatan Mahasiswa): 
ukm_coding = {"Andi", "Budi", "Caca", "Deni"}
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"}
a. Tampilkan mahasiswa yang hanya mendaftar di ukm_coding saja (tidak mendaftar di 
robotik).
b. Tampilkan daftar seluruh mahasiswa unik yang mendaftar di salah satu atau kedua 
UKM tersebut.
c. Cek apakah "Andi" merupakan anggota dari ukm_robotik. Tampilkan hasil dalam 
bentuk boolean.
'''
ukm_coding = {"Andi", "Budi", "Caca", "Deni"}
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"}

# a. Tampilkan mahasiswa yang hanya mendaftar di ukm_coding saja (tidak mendaftar di robotik).
coding_only = ukm_coding.difference(ukm_robotik)
print("Mahasiswa yang hanya mendaftar di UKM Coding:", coding_only)

# b. Tampilkan daftar seluruh mahasiswa unik yang mendaftar di salah satu atau kedua UKM tersebut.
total_mahasiswa = ukm_coding.union(ukm_robotik)
print("Daftar seluruh mahasiswa unik:", total_mahasiswa)

# c. Cek apakah "Andi" merupakan anggota dari ukm_robotik. Tampilkan hasil dalam bentuk boolean.
print("Apakah Andi adalah anggota UKM Robotik?:", "Andi" in ukm_robotik)
