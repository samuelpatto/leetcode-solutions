"""
LeetCode 35: Search Insert Position
Link: https://leetcode.com/problems/search-insert-position/

Padrão: Busca Binária
Complexidade de Tempo: O(log N)
Complexidade de Espaço: O(1)

Descrição:
Encontra o índice de um elemento em um array ordenado. Caso o elemento não exista,
retorna o índice exato onde ele deveria ser inserido para manter a ordenação.
Ao final do loop da busca binária, o ponteiro 'esquerda' representa a posição
correta de inserção.
"""

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        esquerda = 0
        direita = len(nums) - 1

        while esquerda <= direita:
            meio = (esquerda + direita) // 2
            
            if nums [meio] == target:
                return meio
            
            elif nums[meio] < target:
                esquerda = meio + 1

            else:
                direita = meio - 1

        return esquerda
