class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, kode, judul):
        index = self.hash_function(kode)
        for i, (k, _) in enumerate(self.table[index]):
            if k == kode:
                self.table[index][i] = (kode, judul) #untuk update data jika kode sudah ada
                return
        self.table[index].append((kode, judul)) #untuk menambahkan data baru jika kode belum ada

    def search(self, kode):
        index = self.hash_function(kode)
        for k, judul in self.table[index]:
            if k == kode:
                return judul
        return "Buku tidak ditemukan"

    def delete(self, kode):
        index = self.hash_function(kode)
        for i, (k, _) in enumerate(self.table[index]):
            if k == kode:
                del self.table[index][i]
                return

    def display(self):
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Bucket {i}: {bucket}")

# Contoh penggunaan
hash_table = HashTable()
hash_table.insert("BK111", "Mahir C++ Dalam Satu Jam")
hash_table.insert("BK222", "Python Dasar")
hash_table.insert("BK333", "Matematika Diskrit")
hash_table.insert("BK444", "Atomic Habits")
print("\nhasil insert:")
hash_table.display()

hash_table.insert("BK045", "Mein Kampf")
hash_table.insert("BK111", "Bumi Manusia")
hash_table.insert("BK555", "sejarah geosentrisme")
print("\nhasil insert:")
hash_table.display()

print("\nMencari buku BK222:")
hasil_search = hash_table.search("BK222")
print(f"Hasil pencarian BK222: {hasil_search}")

print("\nMencari buku yang tidak ada:")
hasil_search = hash_table.search("BK999")
print(f"Hasil pencarian BK999: {hasil_search}")

hash_table.delete("BK333")
print("\nSetelah menghapus BK333:")
hash_table.display()