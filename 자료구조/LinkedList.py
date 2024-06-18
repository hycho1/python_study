class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def __len__(self) -> int:
        return self.length

    # str
    def __str__(self):
        if self.head is None:
            return "Linked list is empty!"
        res = "head"
        node = self.head
        while node is not None:
            res += " → " + str(node.data)
            node = node.next
        return res

    # appendleft(x): 연결 리스트의 처음에 data를 추가한다.
    def appendleft(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = Node(data)
            node.next = self.head
            self.head = node
        
        self.length += 1

    # append(x): 연결 리스트의 끝 data를 추가한다.
    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next != None:
                node = node.next
            node.next = Node(data)

        self.length += 1


if __name__ == "__main__":
    my_list = LinkedList()
    print(f"연결 리스트 생성.  연결 리스트의 길이 = {len(my_list)}")
    print(my_list)
    print()
    for i in range(4):
        if i % 2:
            my_list.append(i)
        else:
            my_list.appendleft(i)
        print(f"{i}을(를) 추가.  연결 리스트의 길이 = {len(my_list)}")
        print(my_list)
        print()

'''
popleft(): 연결 리스트에서 첫 노드의 값을 반환하고, 노드는 삭제한다.
pop(): 연결 리스트에서 마지막 노드의 값을 반환하고, 노드는 삭제한다.
insert(i, x): 연결 리스트의 i번 인덱스에 x를 추가한다.
remove(x): 연결 리스트에서 값이 x인 노드를 찾아 삭제한다.
reverse(): 연결 리스트를 제자리에서 순서를 뒤집는다.
'''    



