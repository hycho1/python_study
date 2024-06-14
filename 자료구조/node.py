class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

print(node1.data)
print(node1.next.data)
print(node1.next.next.data)

node = Node(10)
node.next = Node(20)
node.next.next = Node(30)

while node:
    print(node.data)
    node = node.next

