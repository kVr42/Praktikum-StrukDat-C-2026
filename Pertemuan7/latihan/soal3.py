'''
3. Case: Layanan Valet VIP tetap memungkinkan kendaraan untuk menyalip.
Namun, karena keterbatasan sistem (Singly Linked List), petugas hanya bisa
melihat kendaraan di depannya. Kendaraan VIP baru dapat disisipkan tepat di
belakang kendaraan VIP tertentu yang sudah ada dalam antrean. Karena hanya
satu arah, untuk pengecekan urutan, petugas harus membacanya dari kendaraan
paling depan hingga paling belakang.
a. Tugas:
  1. Gunakan struktur Singly Linked List (hanya memiliki pointer next).
  2. Buat fungsi sisipkan_vip(plat_baru, plat_target):
     Mencari plat_target dalam antrean, lalu menyisipkan plat_baru tepat setelahnya.
  3. Buat fungsi tampilkan_antrean() untuk menunjukkan urutan kendaraan dari depan ke belakang.
b. Logika: Menelusuri list dari head untuk mencari plat_target. Setelah
ditemukan, buat node baru, hubungkan next dari node baru ke next milik
target, lalu ubah next milik target ke node baru.
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

    def sisipkan_vip(self, plat_baru, plat_target):
        if self.head is None:
            return
        current = self.head
        while current is not None:
            if current.plat == plat_target:
                new_node = Node(plat_baru)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def hapuskendaraan(self, plat):
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

    def tampilkan_antrean(self):
        current = self.head
        while current is not None:
            print(current.plat)
            current = current.next
        print()

antrean = LinkedList()
antrean.tambahKendaraan("A1")
antrean.tambahKendaraan("B2")
antrean.tambahKendaraan("C3")
antrean.tambahKendaraan("D4")
antrean.tambahKendaraan("E5")
antrean.tampilkan_antrean()

antrean.sisipkan_vip("VIP1", "D4")
antrean.tampilkan_antrean()

antrean.hapuskendaraan("C3")
antrean.tampilkan_antrean()