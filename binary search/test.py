import math

a = [7,3,1,4,5,2]
target = 5
a.sort()
print(a)
# # middle value # 중복값 없애기
if len(a) == len(set(a)):
    if target in a:
        a.sort()
        # middle value
        while True:
            if len(a) % 2 == 1:
                middle_index = int(math.floor(len(a))/2)
            else:
                middle_index = int(len(a)/2 - 1 )
            middle_value = a[middle_index]
            print(middle_index)

            if middle_value == target:
                print(middle_value)
                break
            elif middle_value < target:
                a = a[middle_index+1:]
                print(a)
            else:
                a = a[:middle_index+1] # 슬라이싱의 끝은 그 직전까지라서 +1을 해줘야함.
                print(a)
    else:
        print(False)

else:
    print("There are duplicate values in the s list.")
