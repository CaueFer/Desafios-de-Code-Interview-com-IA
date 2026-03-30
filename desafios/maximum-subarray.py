# Desafio Maximum Subarray (Kadane)
# Link: https://leetcode.com/problems/maximum-subarray/
# Estrutura de dados: Array

# Integrante: Walter Theodoro

# Problema
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Solução
def max_subarray(nums):
    atual = maximo = nums[0]
    for i in range(1, len(nums)):
        atual = max(nums[i], atual + nums[i])
        maximo = max(maximo, atual)
    return maximo
