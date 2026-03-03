# Desafio Best Time to Buy and Sell Stock
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Estrutura de dados: Array 

# Integrante: Caue Fernandes Caetano

# Problema
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Solução
def max_profit(prices): 
    menor = float('inf') 
    lucro = 0 
    for p in prices: 
        menor = min(menor, p) 
        lucro = max(lucro, p - menor) 
    return lucro 