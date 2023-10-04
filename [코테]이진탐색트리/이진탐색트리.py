# 이진탐색트리 노드삽입과 탐색 코드
# 내용 참조 : https://jayindustry.tistory.com/47

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class binarysearchtree:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        self.current_node_pointer = self.head
        while True:
            if value < self.current_node_pointer.value:
                if self.current_node_pointer.left == None:
                    self.current_node_pointer.left = Node(value)
                    break
                else:
                    self.current_node_pointer = self.current_node_pointer.left

            else:
                if self.current_node_pointer.right == None:
                    self.current_node_pointer.right = Node(value)
                    break
                else:
                    self.current_node_pointer = self.current_node_pointer.right

    def search(self, value):
        self.current_node_pointer = self.head
        while self.current_node_pointer: # 노드가 존재하지 않을때까지 반복
            if self.current_node_pointer.value == value:
                return print(True)
            elif value < self.current_node_pointer.value:
                self.current_node_pointer = self.current_node_pointer.left
            else:
                self.current_node_pointer = self.current_node_pointer.right
        return print(False)
                
head = Node(1)
bts = binarysearchtree(head)
bts.insert(2)
bts.insert(5)
bts.insert(-1)
bts.insert(0)

bts.search(2)
bts.search(11)
bts.search(-1)
bts.search(0)