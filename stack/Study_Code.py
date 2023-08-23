class Stack(object):
    def isValid(self, s : str) -> bool:
        valid_s = ['()','{}','[]']
        s_list = [s[i:i+2] for i in range(0, len(s), 2)]
        # s스트링문장을 2개씩 끊어서 리스트요소로 넣는다.
        # range(범위)는 0부터 s길이까지, i를 2씩 증가시킨다.)

        # 만약 s가 존재한다면 을 아래 2가지로 나타낼 수 있다.
        # if len(s)>0: -> 1번
        if s: # -> 2번
            for j in s_list: # s의 모든요소가 valid_s에 포함되어있다면, True
                if j in valid_s:
                    pass
                else:
                    return False
            return True
        return False

# 파이썬 슬라이싱에서의 슬라이싱은 끝 인덱스가 포함되지 않고 끝 인덱스의 직전까지 포함된다.
# 고로, sentence[0:2]이면 실제로 0~1번째 인덱스까지를 일컫는다.