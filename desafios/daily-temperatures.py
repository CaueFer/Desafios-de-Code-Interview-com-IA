# Desafio Daily Temperatures
# Link: https://leetcode.com/problems/daily-temperatures/
# Estrutura de dados: Pilha Monotônica

# Integrante: Walter Theodoro

# Problema
# Given an array of integers temperatures representing daily temperatures, return an array answer
# such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
# If there is no future day for which this is possible, keep answer[i] == 0.

# Solução
def daily_temperatures(temperatures):
    res = [0] * len(temperatures)
    pilha = []
    for i, t in enumerate(temperatures):
        while pilha and temperatures[pilha[-1]] < t:
            idx = pilha.pop()
            res[idx] = i - idx
        pilha.append(i)
    return res
