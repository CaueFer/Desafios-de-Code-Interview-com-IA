# Desafio Reverse Linked List
# Link: https://leetcode.com/problems/reverse-linked-list/
# Estrutura de dados: Lista Encadeada

# Integrante: Walter Theodoro

# Problema
# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Solução
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

def reverse_list(head):
    anterior = None
    atual = head
    while atual:
        prox = atual.next
        atual.next = anterior
        anterior = atual
        atual = prox
    return anterior
