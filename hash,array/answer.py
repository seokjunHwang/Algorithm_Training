# Hash / Array
# Hash 는 공간차원을 희생하는대신, 시간차원을 줄이는 효과. 빠른 검색과 저장이 가능.
# 1,2,3,1에서 중복인 요소가있는지 찾는 문제에서 hash 사용

from typing import List
# 타입 힌트를 제공하여 입력과 반환을 명시한다.

class solution():
    def containDuplicate(self, nums: List[int]) -> bool:
        # 이 구문은 "입력과 반환이 이런형태이다" 라는 힌트를주어 코드 가독성을 높이는 효과.
        # nums: List[int]는 매개변수 nums에 타입 힌트를 사용한 것입니다. 이것은 입력 nums가 정수 리스트임을 명시합니다. 
        # List[int]는 int를 원소로 갖는 리스트를 의미합니다.
        # -> bool은 함수의 반환 타입 힌트입니다. 이것은 함수 containsDuplicate가 불리언 값을 반환함을 명시합니다.
        hashset = set()
        for i in nums:
            if i in hashset:
                return print("True") # True
            # True 반환 시, 여기서 코드는 끝!
            # else는 생략( = "같은것이 이미 들어있지 않으면,")
            hashset.add(i) 
        return print("False") # False
    
nums_list = [1,2,3,4,5]
solution().containDuplicate(nums_list)

# 원리)
# 1,2,3,1의 배열이 있는 상태에서 배열(n)만큼의 hash 공간을 만든다. space : O(1) -> O(n) / time : 0(n) : 한번만 순환하니까.
# hash set이라고하는 이 공간을 사용한다.
# 1을 인풋시, 중복임을 보고 없으면 hashset에 넣는다.
# 이렇게 쭉 진행하다가 다시 1을 인풋하는데 중복요소가 존재하면 true반환 

# 타입힌트 부가설명)
# 매개변수로 정수 리스트가 아닌 다른 타입의 변수를 전달하면, 타입 힌트 자체의 존재는 실제 실행에 영향을 주지 않습니다. 
# 대신 코드 에디터, 개발 환경 및 파이썬 정적 타입 검사기 (예: mypy)에서 경고를 받게 됩니다. 이 때문에 실제 실행 시, 코드에서 에러가 발생할 수 있습니다.