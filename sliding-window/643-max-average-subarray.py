"""
LeetCode 643: Maximum Average Subarray I
Link: https://leetcode.com/problems/maximum-average-subarray-i/

Padrão: Fixed Sliding Window (Janela Deslizante Fixa)
Complexidade de Tempo: O(N)
Complexidade de Espaço: O(1)

Descrição:
Encontra a maior média entre todos os sub-arrays contínuos de tamanho 'k'.
Mantém uma soma móvel da janela de tamanho 'k', adicionando o novo elemento
à direita e removendo o elemento que sai à esquerda.
"""

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        soma_atual = sum(nums[:k])
        maior_soma = soma_atual
        
        for i in range(k, len(nums)):
            
            soma_atual = soma_atual + nums[i] - nums[i - k]
            
            if soma_atual > maior_soma:
                maior_soma = soma_atual
                
        
        return maior_soma / k
