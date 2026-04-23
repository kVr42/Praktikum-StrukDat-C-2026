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

# Contoh penggunaan
if __name__ == "__main__":
    browser_history = stacklinkedlist()
    browser_history.push("https://www.google.com")
    browser_history.push("https://www.facebook.com")
    browser_history.push("https://www.youtube.com")

    print("Halaman saat ini:", browser_history.peek())
    print("Ukuran riwayat:", browser_history.size())
    
    print("Kembali ke halaman sebelumnya:", browser_history.pop())
    print("Halaman saat ini setelah kembali:", browser_history.peek())