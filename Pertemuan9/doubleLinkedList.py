#double linked list

class node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class doubleLinkedList:
  def __init__(self):
    self.head = None
  def insertAtEnd(self, data):
    newNode = node(data)
    if self.head is None:
      self.head = newNode
      return
    lastNode = self.head
    while lastNode.next:
      lastNode = lastNode.next
    lastNode.next = newNode
    newNode.prev = lastNode

  def insertAtBeginning(self, data):
    newNode = node(data)
    if self.head is None:
      self.head = newNode
      return
    newNode.next = self.head
    self.head.prev = newNode
    self.head = newNode
  def deleteNode(self, key):
    currentNode = self.head
    while currentNode:
      if currentNode.data == key:
        if currentNode.prev:
          currentNode.prev.next = currentNode.next
        else:
          self.head = currentNode.next
        if currentNode.next:
          currentNode.next.prev = currentNode.prev
        return
      currentNode = currentNode.next

  def display(self):
    currentNode = self.head
    while currentNode:
      print(currentNode.data, end=' ')
      currentNode = currentNode.next
    print()

dll = doubleLinkedList()
dll.insertAtEnd(10)
dll.insertAtEnd(20)
dll.insertAtEnd(30)
dll.insertAtBeginning(5)
dll.deleteNode(10)
dll.display()