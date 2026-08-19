"""
LeetCode 283: Move Zeroes
Link: https://leetcode.com/problems/move-zeroes/

Padrão: Dois Ponteiros (In-Place Array Manipulation)
Complexidade de Tempo: O(N)
Complexidade de Espaço: O(1)

Descrição:
Move todos os elementos zero para o final do array mantendo a ordem relativa
dos elementos não-nulos. Realiza a alteração diretamente no array (in-place)
usando um ponteiro de escrita ('posicao') e um ponteiro de leitura da iteração.
"""

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        resultado = []
        for num in nums:
            if num !=0:
                resultado.append(num)
        
        while len(resultado) < len(nums):
            resultado.append(0)
        
        for i in range(len(nums)):
            nums[i] = resultado[i]
        
