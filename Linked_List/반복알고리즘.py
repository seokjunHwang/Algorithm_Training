# list = [ 1,2,3,4,5] 라면, 리버스 링크드리스트에서 노드1은 null, 노드2는 1을.. 이런식으로 가리켜야한다.
# prev, curr이란 두개의 포인터가 필요하다.

from typing import Optional
"""
0(n) : time 복잡도 : 링크드리스트 루프를 1번돌기 때문
0(1) : space 복잡도 : 2개 변수 외에는 추가메모리를 사용하지 않음
"""
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head : Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            temp_next = curr.next # 처음 curr.next값을 임시변수에 저장
            curr.next = prev
            prev , curr = curr , temp_next
        return prev

"""
작동원리

1) 처음값
null 1->2->3->4->5->null 에서..

2) 결과물
null<-1<-2<-3<-4<-5 null로 바꿔준다.
                  p c
3) 과정
null<-1 2->3->4->5->null
p     c

: 노드 1의 넥스트포인터를(curr.next) null로 바꿔주고 p를 c포인터위치로, c를 다음노드위치로 바꿔준다.
: 위처럼 다음작업을 반복하기 위해 temp_next에 c의 초기 다음노드위치를 저장해놓은것이다.

4) 과정 반복
null<-1<-2  3->4->5->null
      p  c

"""
