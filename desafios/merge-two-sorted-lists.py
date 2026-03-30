# Desafio Merge Two Sorted Lists
# Link: https://leetcode.com/problems/merge-two-sorted-lists/
# Estrutura de dados: Lista Encadeada

# Integrante: Walter Theodoro

# Problema
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list and return the head of the merged linked list.

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

def merge_two_lists(l1, l2):
    dummy = ListNode()
    atual = dummy
    while l1 and l2:
        if l1.val < l2.val:
            atual.next = l1
            l1 = l1.next
        else:
            atual.next = l2
            l2 = l2.next
        atual = atual.next
    atual.next = l1 if l1 else l2
    return dummy.next
