#Circular Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            newNode.next = self.head
            return
        lastNode = self.head
        while lastNode.next != self.head:
            lastNode = lastNode.next
        lastNode.next = newNode
        newNode.next = self.head