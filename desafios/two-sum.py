# Desafio Two Sum
# Link: https://leetcode.com/problems/two-sum/ 
# Estrutura de dados: Array + HashMap 

# Integrante: Caue Fernandes Caetano

# Problema
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Solução
def two_sum(nums, target): 
    mapa = {} 
    for i, num in enumerate(nums): 
        complemento = target - num 
        if complemento in mapa: 
            return [mapa[complemento], i] 
        mapa[num] = i 