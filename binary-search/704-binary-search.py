"""
LeetCode 704: Binary Search
Link: https://leetcode.com/problems/binary-search/

Padrão: Busca Binária (Divisão e Conquista)
Complexidade de Tempo: O(log N)
Complexidade de Espaço: O(1)

Descrição:
Realiza uma busca logarítmica em um array de inteiros previamente ordenado.
Divide o espaço de busca pela metade a cada iteração comparando o elemento
do meio (mid) com o valor alvo (target).
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        esquerda = 0
        direita = len(nums) - 1
        
        while esquerda <= direita:
            meio = (esquerda + direita) // 2
            
            if nums[meio] == target:
                return meio
            
            elif nums[meio] < target:
                esquerda = meio + 1
                
            else:
                direita = meio - 1
                
        return -1
