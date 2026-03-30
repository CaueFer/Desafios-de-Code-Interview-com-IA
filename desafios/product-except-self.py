# Desafio Product of Array Except Self
# Link: https://leetcode.com/problems/product-of-array-except-self/
# Estrutura de dados: Array

# Integrante: Walter Theodoro

# Problema
# Given an integer array nums, return an array answer such that answer[i] is equal to
# the product of all the elements of nums except nums[i].
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Solução
def product_except_self(nums):
    n = len(nums)
    res = [1] * n
    prefixo = 1
    for i in range(n):
        res[i] = prefixo
        prefixo *= nums[i]
    sufixo = 1
    for i in range(n - 1, -1, -1):
        res[i] *= sufixo
        sufixo *= nums[i]
    return res
