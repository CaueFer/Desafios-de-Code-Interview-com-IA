# Desafio Linked List Cycle
# Link: https://leetcode.com/problems/linked-list-cycle/
# Estrutura de dados: Lista Encadeada

# Integrante: Walter Theodoro

# Problema
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# Return true if there is a cycle in the linked list, otherwise return false.

# Solução
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    lento = rapido = head
    while rapido and rapido.next:
        lento = lento.next
        rapido = rapido.next.next
        if lento == rapido:
            return True
    return False
