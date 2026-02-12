'''
buatlah sebuah class dengan :
-minimun 3 atribut
-2 method

Lalu buatlah 3 object dari class tersebut,
lalu ubahlah salah satu atribut dari object tersebut
'''

class Motor:
    def __init__(self, merk, warna, kecepatan):
        self.merk = merk
        self.warna = warna
        self.kecepatan = kecepatan

    def tambah_kecepatan(self, nilai):
        self.kecepatan += nilai
        return self.kecepatan

    def kurangi_kecepatan(self, nilai):
        self.kecepatan -= nilai
        return self.kecepatan
    
motor1 = Motor("Yamaha", "Merah", 100)
motor2 = Motor("Honda", "Biru", 90)
motor3 = Motor("Suzuki", "Hitam", 80)

# Mengubah atribut warna dari motor2
motor2.warna = "Putih"
print(f"Motor 1: Merk={motor1.merk}, Warna={motor1.warna}, Kecepatan={motor1.kecepatan}")
print(f"Motor 2: Merk={motor2.merk}, Warna={motor2.warna}, Kecepatan={motor2.kecepatan}")
print(f"Motor 3: Merk={motor3.merk}, Warna={motor3.warna}, Kecepatan={motor3.kecepatan}")
print("Setelah mengubah warna motor2:")
print(f"Motor 2: Merk={motor2.merk}, Warna={motor2.warna}, Kecepatan={motor2.kecepatan}")

motor1.tambah_kecepatan(20)
print(f"Kecepatan motor1 setelah ditambah: {motor1.kecepatan}")
motor3.kurangi_kecepatan(10)
print(f"Kecepatan motor3 setelah dikurangi: {motor3.kecepatan}")
 