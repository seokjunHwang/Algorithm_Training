class Stack(object):
    def isValid(self, s : str) -> bool:
        valid_s = ['()','{}','[]']
        pop_nums = int(len(valid_s) - len(s)/2)

        if pop_nums >= 0:
            for _ in range(pop_nums):
                valid_s.pop()
            combined_string = ''.join(valid_s)
        if s == combined_string:
            return True

        return False
    
s = '(){}[]'
print(Stack().isValid(s))

# 문제를 잘못 이해함.
# s가 무조건 순서대로 쌓여야 하는줄 알았음.
# 순서가바껴도 상관없음. 쌍만 맞으면 됨.





        
