# Desafio Valid Parentheses
# Link: https://leetcode.com/problems/valid-parentheses/ 
# Estrutura de dados: Pilha 

# Integrante: Caue Fernandes Caetano

# Problema
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
#   - Open brackets must be closed by the same type of brackets.
#   - Open brackets must be closed in the correct order.
#   - Every close bracket has a corresponding open bracket of the same type.

# Solução
def is_valid(s): 
    pilha = [] 
    mapa = {')':'(', '}':'{', ']':'['} 
    for c in s: 
        if c in mapa: 
            topo = pilha.pop() if pilha else '#' 
            if mapa[c] != topo: 
                return False 
        else: 
            pilha.append(c) 
    return not pilha 