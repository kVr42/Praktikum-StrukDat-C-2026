print("NAMA :Romeo Priod Simanullang")
print("NIM  :25071102785")
print("KELAS:TI-25-C")
print("PRODI:Teknik Informatika")

class Queue:
    def __init__(self):
        self._data = []

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self._data.pop(0)
        else:
            return "Queue kosong"

    def front(self):
        if not self.is_empty():
            return self._data[0]
        else:
            return "Queue kosong"

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def display(self):
        return self._data


# Simulasi penggunaan
q = Queue()

q.enqueue("Alek")
q.enqueue("Dinda")
q.enqueue("Edan")

print("Isi Queue:", q.display())
print("Dilayani:", q.dequeue())
print("Sisa Queue:", q.display())
