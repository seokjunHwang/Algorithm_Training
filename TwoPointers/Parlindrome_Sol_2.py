# Solution2
# 두 개의 포인터를 이동하며 같은지 판별
# 시간차원 O(n) , 공간차원 O(1) : 추가메모리를 사용하지않는다.

# class안에 함수나 인자를 쓰려면 self.을 붙여준다.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r: # l이 r보다 작을때까지만 반복한다.

            # 특수문자가 나오면 l 포인터를 다음으로 옮긴다.
            while l < r and not self.alphaNum(s[l]):
                l += 1
            # 오른쪽 포인터도 같이 적용한다.
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower(): # 만약 같은문자가 아니면
                return False
            # 모두 끝마치면 그 다음으로 포인터 이동
            l, r = l + 1, r - 1
        return True
    
    # 영,숫자만 가능하도록 하는 함수.
    def alphaNum(self, c):
        # ord : 아스키문자 범위를 일컫는데, 해당 범위에 해당되면 true반환, 아니면 false반환.
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
    
sentence = "er13^^ 31  re "
print(Solution().isPalindrome(sentence))