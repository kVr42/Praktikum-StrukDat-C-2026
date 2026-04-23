#Bagian 2: Implementasi Menggunakan Linked List
class Node:
    def __init__(self, url):
        self.url = url
        self.next = None

class stacklinkedlist:
    def __init__(self):
        self.top = None
        self.count = 0

    def is_empty(self):
        return self.top is None

    def push(self, url):
        new_node = Node(url)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self):
        if self.is_empty():
            return "Riwayat kosong"
        url = self.top.url
        self.top = self.top.next
        self.count -= 1
        return url

    def peek(self):
        if self.is_empty():
            return None
        return self.top.url

    def size(self):
        return self.count

'''
Setiap kali pengguna mengunjungi halaman web baru, URL halaman tersebut akan ditumpuk.
Jika pengguna menekan tombol "Back", halaman terakhir akan dihapus dari riwayat dan pengguna kembali ke halaman sebelumnya.
Sistem ini sangat cocok menggunakan struktur data Stack (LIFO - Last In First Out).
'''

# Contoh penggunaan
stack = stacklinkedlist()
stack.push("https://www.example.com")
stack.push("https://www.google.com")
stack.push("https://www.youtube.com")
print(stack.pop())  # Output: https://www.youtube.com
print(stack.peek())  # Output: https://www.google.com
print(stack.size())  # Output: 2