"""
LeetCode 344: Reverse String
Link: https://leetcode.com/problems/reverse-string/

Padrão: Dois Ponteiros (In-Place Swap)
Complexidade de Tempo: O(N)
Complexidade de Espaço: O(1)

Descrição:
Inverte um array de caracteres alterando a coleção diretamente em memória (in-place)
trocando os elementos das extremidades em direção ao centro.
"""

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        esquerda = 0
        direita = len(s) - 1
        
        while esquerda < direita:
            
            s[esquerda], s[direita] = s[direita], s[esquerda]
            
            
            esquerda = esquerda + 1
            direita = direita - 1
