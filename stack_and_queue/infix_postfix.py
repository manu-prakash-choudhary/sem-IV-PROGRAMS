# Infix to Postfix Conversion 
# https://lnogueir.github.io/expression-tree-gen/
# https://raj457036.github.io/Simple-Tools/prefixAndPostfixConvertor.html

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

    def peek(self):
        if self.top == -1:
            return -1
        else:
            return self.stack[self.top]
        
def infix_to_postfix(expression):
    # Dictionary to hold precedence of operators
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    # Function to check if a character is an operator
    def is_operator(char):
        return char in precedence

    # Function to compare precedence of operators
    def compare_precedence(op1, op2):
        return precedence[op1] >= precedence[op2]

    # Stack to hold operators
    stack = Stack(100)
    postfix = Stack(100)

    for char in expression:
        if char.isalnum():
            postfix.push(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while stack.peek() != '(':
                postfix.push(stack.peek())
                stack.pop()
            stack.pop()
        elif is_operator(char):
            while not stack.underflow() and stack.peek()!='(' and compare_precedence(stack.peek(), char):
                postfix.push(stack.peek())
                stack.pop()
            stack.push(char)
    while not stack.underflow():
        postfix.push(stack.peek())
        stack.pop()

    return ''.join(postfix.stack)


def postfix_evaluator(expression):
    stack = Stack(100)
    for char in expression:
        if char.isdigit():
            stack.push(int(char))
        else:
            operand2 = stack.peek()
            stack.pop()
            operand1 = stack.peek()
            stack.pop()
            if char == '+':
                stack.push(operand1 + operand2)
            elif char == '-':
                stack.push(operand1 - operand2)
            elif char == '*':
                stack.push(operand1 * operand2)
            elif char == '/':
                stack.push(operand1 / operand2)
            elif char == '^':
                stack.push(operand1 ** operand2)
    return stack.peek()


# infix_expression = "a+b*c-(d/e+f)*g"

# infix_expression2 = "2+2*3-(4/1+2)"
infix_ = '2*(3+4)-5'
postfix_expression = infix_to_postfix(infix_expression)
result = postfix_evaluator(postfix_expression)
print("Infix Expression:", infix_expression)
print("Postfix Expression:", postfix_expression)
print("Result:", result)







'''

---------------------------------------------Infix to POSTFIX(POLISH NOTATION)----------------------------------
An expression is a combination of operands (numbers or variables) and operators (like +, -, *, /, etc.). In an infix expression, the operators are written between the operands (e.g., 3 + 4). In a postfix expression (also known as Reverse Polish Notation or RPN), the operators follow the operands (e.g., 3 4 +).

Converting an infix expression to a postfix expression involves using a stack data structure, which is like a pile of plates or books, where you can only add or remove items from the top.

Here's the step-by-step algorithm:

1. Create an empty stack and an empty postfix expression string.
2. Scan the infix expression from left to right.
3. For each element in the infix expression:
   a. If the element is an operand (a number or a variable), append it to the postfix expression string.
   b. If the element is an opening parenthesis '(', push it onto the stack.
   c. If the element is an operator:
      i. While the stack is not empty and the top element of the stack is an operator with higher or equal precedence than the current operator, pop the operator from the stack and append it to the postfix expression string.
      ii. Push the current operator onto the stack.
   d. If the element is a closing parenthesis ')':
      i. While the top of the stack is not an opening parenthesis '(', pop the operator from the stack and append it to the postfix expression string.
      ii. Pop the opening parenthesis '(' from the stack (and discard it).
4. While the stack is not empty, pop the remaining operators from the stack and append them to the postfix expression string.

The order of precedence for operators is typically: parentheses > exponentiation > multiplication/division > addition/subtraction. If two operators have the same precedence, they are processed from left to right (left-associative).

Here's an example of how the algorithm works for the infix expression "2 * (3 + 4) - 5":

1. Create an empty stack and an empty postfix expression string.
2. Scan the infix expression from left to right:
   a. '2' is an operand, append it to the postfix expression string: "2 "
   b. '*' is an operator, push it onto the stack: [*]
   c. '(' is an opening parenthesis, push it onto the stack: [*, (]
   d. '3' is an operand, append it to the postfix expression string: "2 3 "
   e. '+' is an operator with lower precedence than '*', so push it onto the stack: [*, (, +]
   f. '4' is an operand, append it to the postfix expression string: "2 3 4 "
   g. ')' is a closing parenthesis, so:
      i. Pop '+' from the stack and append it to the postfix expression string: "2 3 4 +"
      ii. Pop '(' from the stack (and discard it).
   h. '-' is an operator with lower precedence than '*', so push it onto the stack: [*, -]
   i. '5' is an operand, append it to the postfix expression string: "2 3 4 + 5 "
3. While the stack is not empty, pop the remaining operators from the stack and append them to the postfix expression string:
   a. Pop '-' from the stack and append it to the postfix expression string: "2 3 4 + 5 -"
   b. Pop '*' from the stack and append it to the postfix expression string: "2 3 4 + 5 - *"

The final postfix expression is: "2 3 4 + 5 - *"

Here's the Python code for converting an infix expression to a postfix expression:

```python
PRECEDENCE = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

def infix_to_postfix(infix_expr):
    stack = []
    postfix = []

    for token in infix_expr:
        if token.isalnum():
            postfix.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            if stack:
                stack.pop()  # Discard the '('
        else:
            while stack and stack[-1] in PRECEDENCE and PRECEDENCE[stack[-1]] >= PRECEDENCE[token]:
                postfix.append(stack.pop())
            stack.append(token)

    while stack:
        postfix.append(stack.pop())

    return ''.join(postfix)

# Example usage
infix_expression = "2 * (3 + 4) - 5"
postfix_expression = infix_to_postfix(infix_expression)
print(f"Infix expression: {infix_expression}")
print(f"Postfix expression: {postfix_expression}")
```

In this code, we define a dictionary `PRECEDENCE` that maps operators to their precedence levels. The `infix_to_postfix` function takes an infix expression as input and returns the corresponding postfix expression.

The function iterates through the tokens (operands and operators) in the infix expression. If the token is an operand, it is appended to the postfix expression list. If the token is an opening parenthesis, it is pushed onto the stack. If the token is an operator, it is pushed onto the stack after popping and appending higher or equal precedence operators from the stack to the postfix expression list. If the token is a closing parenthesis, operators are popped from the stack and appended to the postfix expression list until an opening parenthesis is encountered (which is then discarded).

After the loop, any remaining operators on the stack are popped and appended to the postfix expression list. Finally, the postfix expression list is joined into a string and returned.

In the example usage, the infix expression "2 * (3 + 4) - 5" is converted to the postfix expression "2 3 4 + 5 - *".







-----------------------------------------------EVALUATING A POSTFIX EXPRESSION---------------------------------------------

Evaluating a postfix expression is relatively straightforward because the operands are always followed by the operator that applies to them. The process involves using a stack data structure to keep track of operands and perform operations as operators are encountered.

Here's the step-by-step algorithm for evaluating a postfix expression:

1. Create an empty stack.
2. Scan the postfix expression from left to right.
3. For each element in the postfix expression:
   a. If the element is an operand (a number or a variable), push it onto the stack.
   b. If the element is an operator:
      i. Pop the top two operands from the stack (let's call them operand1 and operand2).
      ii. Perform the operation specified by the operator on operand2 and operand1 (in that order) and push the result back onto the stack.
4. After scanning the entire postfix expression, the final result will be the single value left on the stack.

Here's an example of how the algorithm works for the postfix expression "2 3 4 + 5 - *":

1. Create an empty stack: []
2. Scan the postfix expression from left to right:
   a. '2' is an operand, push it onto the stack: [2]
   b. '3' is an operand, push it onto the stack: [2, 3]
   c. '4' is an operand, push it onto the stack: [2, 3, 4]
   d. '+' is an operator, so:
      i. Pop the top two operands: operand1 = 4, operand2 = 3
      ii. Perform the operation 3 + 4 and push the result onto the stack: [2, 7]
   e. '5' is an operand, push it onto the stack: [2, 7, 5]
   f. '-' is an operator, so:
      i. Pop the top two operands: operand1 = 5, operand2 = 7
      ii. Perform the operation 7 - 5 and push the result onto the stack: [2, 2]
   g. '*' is an operator, so:
      i. Pop the top two operands: operand1 = 2, operand2 = 2
      ii. Perform the operation 2 * 2 and push the result onto the stack: [4]
3. After scanning the entire postfix expression, the final result (4) is the single value left on the stack.

Here's the Python code for evaluating a postfix expression:

```python
def evaluate_postfix(postfix_expr):
    stack = []

    for token in postfix_expr:
        if token.isdigit():
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            # You can add more operator cases as needed

            stack.append(result)

    return stack.pop()

# Example usage
postfix_expression = "2 3 4 + 5 - *"
result = evaluate_postfix(postfix_expression)
print(f"Postfix expression: {postfix_expression}")
print(f"Result: {result}")
```

In this code, the `evaluate_postfix` function takes a postfix expression as input and returns the final result after evaluating the expression.

The function iterates through the tokens (operands and operators) in the postfix expression. If the token is an operand (a digit), it is converted to an integer and pushed onto the stack. If the token is an operator, the top two operands are popped from the stack, the operation is performed on them, and the result is pushed back onto the stack.

After the loop, the final result is the single value left on the stack, which is returned.

In the example usage, the postfix expression "2 3 4 + 5 - *" is evaluated, and the result (4) is printed.

Note that this implementation assumes that the postfix expression is valid and only includes single-digit operands and the basic arithmetic operators (+, -, *, /). You can extend it to handle more complex cases, such as multi-digit operands, variables, and additional operators, as needed.






'''
# https://dpaste.org/AxNkB