# Desafio Contains Duplicate
# Link: https://leetcode.com/problems/contains-duplicate/
# Estrutura de dados: Array + Set

# Integrante: Walter Theodoro

# Problema
# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.

# Solução
def contains_duplicate(nums):
    return len(nums) != len(set(nums))
