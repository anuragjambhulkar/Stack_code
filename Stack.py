class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty")  # Raise an exception

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Stack is empty")  # Raise an exception

# Example usage
my_stack = Stack()

# Add items to the stack
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print("Stack after pushing 1, 2, 3:", my_stack.stack)

# Remove an item from the stack
print("Popped item:", my_stack.pop())
print("Stack after popping an item:", my_stack.stack)

# Check if the stack is empty
print("Is the stack empty?", my_stack.is_empty())

# Peek at the top item of the stack
print("Top item:", my_stack.peek())
