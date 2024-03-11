# The Next greater Element for an element x is the first greater element on the right side of x in the array. Elements for which no greater element exist, consider the next greater element as -1. 

# Python program to print next greater element using stack

# Stack Functions to be used by printNGE()

class Stack:
    def __init__(self, size):
        self.stack = []
        self.top = -1
        self.size = size

    def push(self, value):
        if self.top == self.size - 1:
            print("Stack Overflow")
        else:
            self.stack.append(value)
            self.top += 1

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
        else:
            val = self.stack.pop()
            self.top -= 1
            return val

    def display(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            for i in range(self.top, -1, -1):
                print(self.stack[i], end=" ")
            print()

    def overflow(self):
        if self.top == self.size - 1:
            return True
        else:
            return False

    def underflow(self):
        if self.top == -1:
            return True
        else:
            return False

def NGE(arr):
    nxt = -1
    for i in range(0,len(arr)):
        for j in range(i, len(arr)):
            if arr[i]<arr[j]:
                print(f'NGE of {arr[i]} is {arr[j]}')
                break
        else:
            print(f'NGE of {arr[i]} is -1')


def NGE_stack(arr):
    stack = Stack(len(arr))
    stack.push(arr[0])
    
    for i in range(1, len(arr)):
        next = arr[i]
        if stack.underflow() == False:
            element = stack.pop()
            while element < next:
                print(f'NGE of {element} is {next}')
                if stack.underflow():
                    break
                element = stack.pop()
            if element>next:
                stack.push(element)
        stack.push(next)
    
    while not stack.underflow():
        element = stack.pop()
        print(f'NGE of {element} is -1')


arr = [11, 13, 21, 3]
NGE_stack(arr)
