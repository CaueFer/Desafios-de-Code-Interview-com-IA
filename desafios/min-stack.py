# Desafio Min Stack
# Link: https://leetcode.com/problems/min-stack/
# Estrutura de dados: Pilha

# Integrante: Caue Fernandes

# Problema
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class with push, pop, top and getMin operations.

# Solução
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]
