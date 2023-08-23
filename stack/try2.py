class Stack(object):
    def isValid(self, s : str) -> bool:
        valid_s = ['()','{}','[]']
        s_list = [s[i:i+2] for i in range(0, len(s), 2)]
        # range(범위)는 0부터 s길이까지, i를 2씩 증가시킨다.)
        if s: 
            for j in s_list:
                if j in valid_s:
                    pass
                else:
                    return False
            return True
        return False

    
s = '()[]'
print(Stack().isValid(s))







        
