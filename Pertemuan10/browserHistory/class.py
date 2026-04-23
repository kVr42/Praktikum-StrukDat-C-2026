#Bagian 1: Implementasi Menggunakan Class
class StackList:
      def __init__(self):
        self.items = [] # Menggunakan list bawaan Python

      def is_empty(self):
        return len(self.items) == 0

      def push(self, url):
        self.items.append(url)

      def pop(self):
        if self.is_empty():
          return "Riwayat kosong"
        return self.items.pop()

      def peek(self):
        if self.is_empty():
          return None
        return self.items[-1]

      def size(self):
        return len(self.items)

# Contoh penggunaan
if __name__ == "__main__":
    browser_history = StackList()
    browser_history.push("https://www.google.com")
    browser_history.push("https://www.facebook.com")
    browser_history.push("https://www.youtube.com")

    print("Halaman saat ini:", browser_history.peek())
    print("Ukuran riwayat:", browser_history.size())
    
    print("Kembali ke halaman sebelumnya:", browser_history.pop())
    print("Halaman saat ini setelah kembali:", browser_history.peek())