class Node:
    def __init__(self, nama, keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
        
    #enqueue (tambah ke belakang)
    def enqueue(self, nama, keluhan):
        new_node = Node(nama, keluhan)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
        print(f"[DAFTAR] {nama} terdaftar dengan keluhan: {keluhan} (No. Antrian: {self._size})")
        
    #dequeue (ambil dari depan)
    def dequeue(self):
        if self.isEmpty():
            print("[PANGGIL] Antrian kosong, tidak ada pasien yang bisa dipanggil.")
            return None
        removed_node = self.head
        self.head = self.head.next
        if self.head is None:  # Jika antrian menjadi kosong setelah dequeue
            self.tail = None
        self._size -= 1
        print(f"[PANGGIL] Dokter memanggil: {removed_node.nama} (keluhan: {removed_node.keluhan})")
        return removed_node
      
    #peek/front (lihat depan tanpa hapus)
    def peek(self):
        if self.isEmpty():
            print("[PEEK] Antrian kosong, tidak ada pasien yang bisa dilihat.")
            return None
        print(f"[PEEK] Pasien berikutnya: {self.head.nama} — {self.head.keluhan}")
        return self.head
      
    #isEmpty (cek apakah antrian kosong)
    def isEmpty(self):
        return self.head is None
      
    #size (hitung jumlah pasien)
    def size(self):
        print(f"[INFO] Jumlah pasien menunggu: {self._size} orang")
        return self._size
      
    #clear (kosongkan antrian)
    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0
        print("[CLEAR] Sesi poliklinik selesai. Antrian dikosongkan.")
        
    #tampilkan antrian
    def display(self):
        if self.isEmpty():
            print("[ANTRIAN SAAT INI] Antrian kosong.")
            return
        print("[ANTRIAN SAAT INI]")
        current = self.head
        no = 1
        while current:
            print(f"{no}. {current.nama} → {current.keluhan}")
            current = current.next
            no += 1


antrian = Queue()

print("====================================")
print(" SISTEM ANTRIAN POLI UMUM")
print(" RS Sehat Bersama")
print("====================================\n")

# 1
print("[CEK] Apakah antrian kosong?")
print("→ YA, antrian masih kosong.\n" if antrian.isEmpty() else "→ TIDAK kosong\n")

# 2-4
antrian.enqueue("Budi", "demam tinggi")
antrian.enqueue("Ani", "batuk pilek")
antrian.enqueue("Citra", "sakit kepala")

# 5
print(f"\n[INFO] Jumlah pasien menunggu: {antrian.size()} orang\n")

# 6
antrian.peek()

# 7
antrian.dequeue()

# 8
antrian.enqueue("Dodi", "nyeri perut")

# 9
antrian.display()

# 10
antrian.dequeue()

# 11
print(f"\n[INFO] Jumlah pasien masih menunggu: {antrian.size()} orang\n")

# 12
antrian.clear()

# 13
print("\n[CEK] Apakah antrian kosong?")
print("→ YA, antrian sudah kosong." if antrian.isEmpty() else "→ TIDAK kosong")

print("\n====================================")
print(" Simulasi Selesai!")
print("====================================")
