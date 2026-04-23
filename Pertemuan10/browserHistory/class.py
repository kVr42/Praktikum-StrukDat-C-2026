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