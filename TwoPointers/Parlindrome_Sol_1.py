# solution 1
# 많은 저장공간 요구

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = "" # 특수문자없애고 소문자만 들어가게끔 저장

        for i in s:
            if i.isalnum():
                newStr += i.lower() # 소문자변환
        return newStr == newStr[::-1] # 뒤집어도 같은지 판별
        # 뒤집어도 같으면 true반환
    
sentence = "qwe 313 ewq^3^"
print(Solution().isPalindrome(sentence))