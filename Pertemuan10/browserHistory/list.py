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