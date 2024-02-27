# Write a program for implementing a  STACK  which should support operations like push, pop, overflow, underflow, display

class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size
        self.top = -1

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
            self.stack.pop()
            self.top -= 1

    def display(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            for i in range(self.top, -1, -1):
                print(self.stack[i])

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
        
# Driver code
if __name__ == "__main__":
    stack = Stack(5)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.display()
    stack.push(6)
    stack.push(7)
    stack.pop()
    stack.pop()
    stack.display()
    print(stack.overflow())
    print(stack.underflow())