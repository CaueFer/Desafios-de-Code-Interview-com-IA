# Desafio Remove Nth Node From End
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Estrutura de dados: Lista Encadeada 

# Integrante: Caue Fernandes Caetano

# Problema
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Solução
def remove_nth_from_end(head, n): 
    dummy = ListNode(0, head) 
    lento = rapido = dummy 
    for _ in range(n+1): 
        rapido = rapido.next 
    while rapido: 
        lento = lento.next 
        rapido = rapido.next 
    lento.next = lento.next.next 
    return dummy.next 