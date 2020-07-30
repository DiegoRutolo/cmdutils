def isEven(num: int):
    if num == 0:
        return True
    
    return not isEven(num-1)

for i in range(5):
    print(i, isEven(i))