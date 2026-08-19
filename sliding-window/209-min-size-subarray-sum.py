"""
LeetCode 209: Minimum Size Subarray Sum
Link: https://leetcode.com/problems/minimum-size-subarray-sum/

Padrão: Dynamic Sliding Window (Janela Deslizante Dinâmica)
Complexidade de Tempo: O(N)
Complexidade de Espaço: O(1)

Descrição:
Encontra o menor comprimento de um sub-array contínuo cuja soma seja maior ou igual a 'target'.
A expansão da janela ocorre com o ponteiro 'direita' e a contração acontece com o ponteiro
'esquerda' enquanto a soma se mantiver válida.
"""

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        inicio = 0
        soma_atual = 0
        tamanho_minimo = float ('inf')
        
        for fim in range(len(nums)):
            soma_atual += nums[fim]
            
            while soma_atual >= target:
                
                tamanho_atual = fim - inicio + 1
                if tamanho_atual < tamanho_minimo:
                    tamanho_minimo = tamanho_atual
                
                soma_atual -= nums[inicio]
                inicio += 1
        
        return tamanho_minimo if tamanho_minimo !=float('inf') else 0            
