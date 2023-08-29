# 재귀적으로 접근시, 문제 하나가 여러개의 작은 하위문제로 쪼개질 수 있는지 보라.

from typing import Optional

class LinkNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
"""
0(n) : time 복잡도 : 재귀함수 호출횟수가 링크드리스트 노드와 같기때문
0(1) : space 복잡도 : 재귀함수 콜 스택이 링크드리스트 노드갯수에 따라 높아지기 때문
"""
class Solution:
    def reverseList(self, head = Optional[LinkNode]) -> Optional[LinkNode]:
        if not head or not head.next: # head가 없거나 1개의 노드일땐(next노드가없다)
            return head # 그대로 반환
        new_tail = head.next # F를 통과한 인자는 거꾸로 바뀌는데, 그럼 그 마지막인자(맨아래 모식도에서 2)가 마지막노드가 될꺼기때문
        new_head = self.reverseList(head.next) # 두번째 노드를 재귀함수 인자로 넘긴다.
        new_tail.next = head
        head.next = None
        return new_head

head = [1,2,3,4,5]
print(Solution().reverseList(head))


"""
reverseList를 F함수라고 가정할 때,
head = [1,2,3,4,5]를 인자로 넘길때 아래처럼 호출이된다.

F(1->2->3->4->5->null) : 이 부분을 2부분으로 나눈다.
   F(2->3->4->5->null) -> 1 -> null  :  노드 1에 대한 나머지는 서브링크드리스트이다.
      F(3->4->5->null) -> 2 -> null  : 이렇게 재귀적으로 3,4,5를 인자로 넘긴다.
              ... 계속진행 ...

마지막 F(5->null)만 남을땐 인자로 넘어온 얘들을 결과로 호출한다. 그럼 아래처럼 역순으로 올라간다.

F(1->2->3->4->5->null) : 이 부분을 2부분으로 나눈다.
   F(2->3->4->5->null) -> 1 -> null  :  노드 1에 대한 나머지는 서브링크드리스트이다.
      F(3->4->5->null) -> 2 -> null 
           5->4   ->null             : 이런식으로 다시 역순으로 올라간다.

최종적단계에서 아래 모식도처럼 바꾼다.

 <---------
1 5->4->3->2
->null

1은 원래 2를 가리키는데 null을 가리키도록 바꾸고
2는 원래 null을 가리키는데 1을 가리키도록 바꾼다.
"""
