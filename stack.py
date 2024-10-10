class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, symbol):
        self.stack.append(symbol)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None  # Retorna None si la pila está vacía
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def __str__(self):
        return str(self.stack)
