'''
Cerita Latar Belakang
Sebuah perusahaan logistik bernama "Cepat Sampai" menggunakan sistem kode lokasi gudang
yang berbentuk pohon biner. Setiap gudang (Node) dapat memiliki maksimal dua cabang jalur
distribusi (Left Child dan Right Child).
Manajer operasional perlu melakukan audit rutin untuk memastikan semua gudang terkunjungi.
Ada tiga metode audit yang digunakan:
  1. Audit Prioritas (Pre-Order): Mengecek gudang utama sebelum cabang-cabangnya.
  2. Audit Berurutan (In-Order): Mengecek dari jalur kiri, lalu pusat, baru ke kanan.
  3. Audit Akhir (Post-Order): Mengecek semua cabang terlebih dahulu sebelum kembali ke gudang pusat.


Tugas
Buatlah program Python untuk membangun struktur Binary Tree secara manual dan melakukan
ketiga jenis traversal tersebut.
Operasi yang Wajib Diimplementasikan:
  1. insert_manual(): Membangun pohon sesuai struktur yang ditentukan di skenario.
  2. traverse_preorder(): Menampilkan urutan gudang dengan metode Pre-Order.
  3. traverse_inorder(): Menampilkan urutan gudang dengan metode In-Order.
  4. traverse_postorder(): Menampilkan urutan gudang dengan metode Post-Order.
  5. get_leaf_nodes(): Menampilkan daftar gudang yang merupakan Leaf Node (gudang ujung yang tidak punya cabang lagi).


Skenario Pengujian
Bangunlah struktur pohon berikut di dalam programmu:
  • A adalah Root.
  • A memiliki anak kiri B dan anak kanan C.
  • B memiliki anak kiri D dan anak kanan E.
  • C memiliki anak kanan F (anak kiri kosong).
Setelah pohon terbentuk, tampilkan:
  1. Hasil penelusuran Pre-Order.
  2. Hasil penelusuran In-Order.
  3. Hasil penelusuran Post-Order.



Contoh Output yang Diharapkan:

SISTEM AUDIT DISTRIBUSI "CEPAT SAMPAI"
======================================
[INFO] Membangun Struktur Gudang...
[INFO] Struktur berhasil dibuat.

HASIL AUDIT:
1. Pre-Order : A - B - D - E - C - F
2. In-Order : D - B - E - A - C - F
3. Post-Order : D - E - B - F - C - A

[DATA] Gudang Ujung (Leaf Nodes): D, E, F
======================================
Audit Selesai!

Aturan Penting
  • DILARANG menggunakan modul collections.deque atau queue.
  • Struktur harus dibangun menggunakan class Node dengan atribut data, left, dan right.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    def insert_manual(self):
        self.root = Node('A')
        self.root.left = Node('B')
        self.root.right = Node('C')
        self.root.left.left = Node('D')
        self.root.left.right = Node('E')
        self.root.right.right = Node('F')
    def traverse_preorder(self, node, result):
        if node:
            result.append(node.data)
            self.traverse_preorder(node.left, result)
            self.traverse_preorder(node.right, result)
    def traverse_inorder(self, node, result):
        if node:
            self.traverse_inorder(node.left, result)
            result.append(node.data)
            self.traverse_inorder(node.right, result)
    def traverse_postorder(self, node, result):
        if node:
            self.traverse_postorder(node.left, result)
            self.traverse_postorder(node.right, result)
            result.append(node.data)
    def get_leaf_nodes(self, node, leaf_nodes):
        if node:
            if not node.left and not node.right:
                leaf_nodes.append(node.data)
            self.get_leaf_nodes(node.left, leaf_nodes)
            self.get_leaf_nodes(node.right, leaf_nodes)


if __name__ == "__main__":
    print("SISTEM AUDIT DISTRIBUSI \"CEPAT SAMPAI\"")
    print("======================================")
    print("[INFO] Membangun Struktur Gudang...")
    
    tree = BinaryTree()
    tree.insert_manual()
    
    print("[INFO] Struktur berhasil dibuat.\n")
    
    print("HASIL AUDIT:")
    
    preorder_result = []
    tree.traverse_preorder(tree.root, preorder_result)
    print("1. Pre-Order :", " - ".join(preorder_result))
    
    inorder_result = []
    tree.traverse_inorder(tree.root, inorder_result)
    print("2. In-Order :", " - ".join(inorder_result))
    
    postorder_result = []
    tree.traverse_postorder(tree.root, postorder_result)
    print("3. Post-Order :", " - ".join(postorder_result))
    
    leaf_nodes = []
    tree.get_leaf_nodes(tree.root, leaf_nodes)
    print("\n[DATA] Gudang Ujung (Leaf Nodes):", ", ".join(leaf_nodes))
    
    print("======================================")
    print("Audit Selesai!")