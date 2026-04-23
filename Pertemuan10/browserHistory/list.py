#Bagian 3: Implementasi Menggunakan List
class StackList2:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, url):
        self.stack.append(url)

    def pop(self):
        if self.is_empty():
            return "Riwayat kosong"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)

#input url
url = input("Masukkan URL: ")

# Contoh penggunaan
if __name__ == "__main__":
    browser_history = StackList2()
    browser_history.push("https://www.google.com")
    browser_history.push("https://www.facebook.com")
    browser_history.push("https://www.youtube.com")
    browser_history.push(url)

    print("Halaman saat ini:", browser_history.peek())
    print("Ukuran riwayat:", browser_history.size())
    
    print("Kembali ke halaman sebelumnya:", browser_history.pop())
    print("Halaman saat ini setelah kembali:", browser_history.peek())