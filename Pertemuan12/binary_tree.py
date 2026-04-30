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