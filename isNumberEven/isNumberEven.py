def isEven(num: int):
    if num == 0:
        return True
    
    return not isEven(num-1)


def isNumberEven(num: int):
    even = True
    for _ in range(num):
        even = not even
    
    return even


for i in range(6):
    print(i, isNumberEven(i))