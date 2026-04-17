class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.head = None
    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            newNode.next = self.head
            return
        lastNode = self.head
        while lastNode.next != self.head:
            lastNode = lastNode.next
        lastNode.next = newNode
        newNode.next = self.head
        return


# Menghapus node berdasarkan data
    def delete(self, data):
        if self.head is None:
            return

        current = self.head
        prev = None

        while True:
            # Jika node ditemukan
            if current.data == data:

                # Jika hanya ada 1 node
                if current == self.head and current.next == self.head:
                    self.head = None

                # Jika menghapus head dan ada lebih dari 1 node maka head harus dipindahkan
                elif current == self.head:
                    last = self.head

                    # Cari node terakhir yang menunjuk ke head lama
                    while last.next != self.head:
                        last = last.next

                    # Head pindah ke node berikutnya (30) dan node lama (10) akan dihapus
                    self.head = self.head.next

                    # Node terakhir menunjuk ke head baru (30)
                    last.next = self.head

                # Jika menghapus node biasa / terakhir
                else:
                  # 10 (prev) -> 20 (current) -> 30 (current.next)
                    prev.next = current.next

                return

            # Geser ke node berikutnya (prev = None, current = 10) -> (prev = 10, current = 20) -> (prev = 20, current = 30)
            prev = current
            current = current.next

            # Jika sudah kembali ke head, berarti data tidak ada
            if current == self.head:
                break

cll = CircularLinkedList()
cll.insertAtEnd(10)
cll.insertAtEnd(20)
cll.insertAtEnd(30)
print(cll.head.data)
print(cll.head.next.data)
print(cll.head.next.next.data)
cll.delete(20)
cll.delete(10)
cll.delete(30)
print(cll.head)  # Output: None (karena semua node sudah dihapus)

x = 5
y = 10
print(x, y)