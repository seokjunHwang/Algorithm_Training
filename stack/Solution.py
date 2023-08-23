class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack
    
s = "([{()()[[[[][](]]]}])"
print(Solution().isValid(s))

# 솔루션에서는 s에 ((([[]])))이런거까지 모두 true가 되게끔 하였다.
# 나는 ()[]{}{}() 이런식으로 짝이 바로바로 붙어있게끔 되어야 true를 출력하라는 뜻으로 잘못해석하였다.

# < 문제 >
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false