arr = [11, 13, 21, 3, 4]
stack = [arr[0]]

for i in range(1, len(arr)):
    
    while len(stack) !=0 and  arr[i] > stack[-1]:
        print(f"NGE of {stack[-1]} is {arr[i]}")
        stack.pop()

    stack.append(arr[i])

while len(stack)!=0:
    print(f"NGE of {stack.pop()} does not exist")

