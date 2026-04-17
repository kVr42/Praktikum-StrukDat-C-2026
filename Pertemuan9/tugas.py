# DOUBLE LINKED LIST

class Node:
    def __init__(self, plat):
        self.plat = plat
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def tambah_kendaraan(self, plat):
        new_node = Node(plat)
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = new_node
        new_node.prev = temp

    def tampilkan_maju(self):
        print("[Maju]")
        temp = self.head
        while temp:
            print(temp.plat)
            temp = temp.next

    def tampilkan_mundur(self):
        print("[Mundur]")
        temp = self.head
        while temp.next:
            temp = temp.next
        
        while temp:
            print(temp.plat)
            temp = temp.prev

    def hapus_kendaraan(self, plat):
        temp = self.head

        while temp:
            if temp.plat == plat:
                # jika node adalah head
                if temp.prev is None:
                    self.head = temp.next
                    if self.head:
                        self.head.prev = None
                else:
                    temp.prev.next = temp.next
                    if temp.next:
                        temp.next.prev = temp.prev
                return
            temp = temp.next


# TES DOUBLE LINKED LIST

dll = DoubleLinkedList()

dll.tambah_kendaraan("B 1111 AA")
dll.tambah_kendaraan("D 2222 BB")
dll.tambah_kendaraan("A 3333 CC")
dll.tambah_kendaraan("B 4444 DD")

print("Sebelum:")
dll.tampilkan_maju()

dll.hapus_kendaraan("A 3333 CC")

print("Sesudah:")
dll.tampilkan_maju()



# CIRCULAR LINKED LIST

class NodeCircular:
    def __init__(self, nama):
        self.nama = nama
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def tambah_petugas(self, nama):
        new_node = NodeCircular(nama)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        
        temp.next = new_node
        new_node.next = self.head

    def giliran_berikutnya(self, n):
        temp = self.head
        for i in range(n):
            print(f"Giliran {i+1}: {temp.nama}")
            temp = temp.next


# TES CIRCULAR LINKED LIST

cll = CircularLinkedList()

cll.tambah_petugas("Alek")
cll.tambah_petugas("Dinda")
cll.tambah_petugas("Edan")
cll.tambah_petugas("Ingot")

cll.giliran_berikutnya(6)

# Petugas nganggur

def petugas_nganggur(cll, n):
    temp = cll.head
    for i in range(n):
        print(f"Giliran {i+1}: {temp.nama}")
        temp = temp.next
    print(f"Petugas nganggur: {temp.nama}")