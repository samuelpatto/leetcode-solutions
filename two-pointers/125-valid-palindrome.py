"""
LeetCode 125: Valid Palindrome
Link: https://leetcode.com/problems/valid-palindrome/

Padrão: Dois Ponteiros (Extremidades Opostas)
Complexidade de Tempo: O(N)
Complexidade de Espaço: O(1)

Descrição:
Verifica se uma string é um palíndromo considerando apenas caracteres alfanuméricos
e ignorando letras maiúsculas/minúsculas. Utiliza dois ponteiros que se movem das
extremidades em direção ao centro.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        texto = ''.join(c.lower() for c in s if c.isalnum())
        
        esquerda = 0
        direita = len(texto) - 1
        
        while esquerda < direita:
            
            if texto[esquerda] != texto[direita]:
                return False
            
            esquerda = esquerda + 1
            direita = direita - 1
            
        return True
