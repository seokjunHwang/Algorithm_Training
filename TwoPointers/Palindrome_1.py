# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing
# all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# 1. 특수문자,공백등을 지우기
# 2. 다 소문자화시키기
# 3. 투포인트 사용 : 처음과 끝포인트를 비교하여 같으면 시작+1,끝-1포인트끼리 비교하는 방식으로 끝까지감.
# 4. 만약 같지 않다면 false반환


class Solution(object):
    def isPalindrome(self, s) -> bool:
        
        # 소문자+숫자 문자열로 만들기
        result = ""
        for i in s:
            # 문자만 사용하려면 .isalpha()메서드
            # 문자+숫자 : .isalnum()메서드 사용
            if i.isalnum():
                result += i
        result = result.lower()        

        # 투포인트사용 : palindrome판별
        s = 0
        e = len(result) - 1
        while True:
            if result[s] == result[e]:
                s += 1
                e -= 1
                if s >= e: # 이거 처음에 s <= e로 해서 계속 안되었던것임.
                    print(result)
                    return True
            else:
                print(result)
                return False

s = "A 안 ^^ ;; 3223 안a ;"
print(Solution().isPalindrome(s)) # 여기서 print를 해주면 함수 return값이 프린트 된다.

"""
:type s: str
:rtype: bool
"""
