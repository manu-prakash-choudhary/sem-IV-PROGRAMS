# Write a program to design a circular queue(k) which Should implement the below functions 
# Enqueue 
# Dequeue
# Front 
# Rear


class CircularQueue:
    def __init__(self, k):
        self.size = k
        self.queue = [None] * k
        self.front = self.rear = -1

    def enqueue(self, value):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp

    def front_element(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            return self.queue[self.front]

    def rear_element(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            return self.queue[self.rear]
        
    def display(self):
        if self.front == -1:
            print("Queue is empty")
        elif self.rear >= self.front:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
            print()



cq = CircularQueue(5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)

print("Front element:", cq.front_element())  # Output: 1
print("Rear element:", cq.rear_element())    # Output: 5

cq.dequeue()
cq.dequeue()
cq.display()  # Output: 3 4 5
print("Front element:", cq.front_element())  # Output: 3
print("Rear element:", cq.rear_element())    # Output: 5
