# Definition for singly-linked list.
# Reverse_linkedlist : 'stack' algorithmic solution

from typing import Optional

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
0(n) : time 복잡도
0(n) : space 복잡도

"""
class Solution(object):
    def reverseList(self, head : Optional[ListNode]) -> Optional[ListNode] :
        stack = []
        node = head

        # stack에 head의 각 노드 추가
        while node: # 링크드리스트 각 노드에 접근, node(head)가 존재할때만 무한루프
            stack.append(node)
            node = node.next

        # stack에서 노드를 하나씩제거하면서 거꾸로 뒤집히는 링크드리스트 만듦
        dummy = ListNode(-1) # dummy에 저장된 값(-1)은 중요하지않다.
        node = dummy
        while stack: # stack에 무언가 있는동안만 루프를 돈다.
            node.next = stack.pop() # 현재 노드의 next를 스택에서 꺼낸얘랑 같게 만들어준다.
            node = node.next # 현재노드를 변경하여 그 다음 노드에서 작업할 수 있도록한다.
        node.next = None # 마지막 노드의 next를 null값으로

        return dummy.next # dummy.next = 거꾸로 뒤집힌 링크드리스트의 첫번째 노드

        
