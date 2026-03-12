'''
2. Case: Kendaraan yang sudah selesai urusan harus keluar melalui satu pintu yang
sama. Karena ini antrean, kendaraan yang pertama datang harus pertama keluar
(FIFO). Namun, karena ada kendala teknis, terkadang ada kendaraan di urutan
tertentu yang "mogok" dan harus dihapus dari daftar antrean secara paksa.
a. Tugas:
  1. Buat struktur Node dan LinkedList.
  2. Buat fungsi tambahKendaraan(plat) untuk menambah kendaraan ke akhir list (Tail).
  3. Buat fungsi hapusKendaraan(plat) untuk menghapus kendaraan tertentu jika ia mogok di tengah antrean.
b. Logika: Melakukan traversal (penelusuran) dari head hingga menemukan
plat yang cocok, lalu menyambungkan node sebelumnya langsung ke node
sesudahnya.
'''

class Node:
    def __init__(self, plat):
        self.plat = plat
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambahKendaraan(self, plat):
        new_node = Node(plat)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def hapusKendaraan(self, plat):
        if self.head is None:
            return
        if self.head.plat == plat:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.plat == plat:
                current.next = current.next.next
                return
            current = current.next

    def tampilkanKendaraan(self):
        current = self.head
        while current is not None:
            print(current.plat)
            current = current.next
        print()


kendaraan = LinkedList()
kendaraan.tambahKendaraan("B 1234 ABC")
kendaraan.tambahKendaraan("D 8888 XYZ")
kendaraan.tambahKendaraan("A 111 TUV")
kendaraan.tambahKendaraan("B 2022 EFG")
kendaraan.tampilkanKendaraan()

kendaraan.hapusKendaraan("B 2022 EFG")
kendaraan.tampilkanKendaraan()