"""
LeetCode 242: Valid Anagram
Link: https://leetcode.com/problems/valid-anagram/

Padrão: Hash Map / Contagem de Frequência
Complexidade de Tempo: O(N)
Complexidade de Espaço: O(1) - O alfabeto tem tamanho fixo (26 letras)

Descrição:
Verifica se a string 't' é um anagrama de 's' comparando a contagem de frequência
de cada caractere através de um dicionário.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        anagrama_t={}
        anagrama_s={}
        
        for letra in s:
            if letra in anagrama_s:
                anagrama_s[letra] = anagrama_s[letra] + 1
            else:
                anagrama_s[letra] = 1
        
        for letra in t:
            if letra in anagrama_t:
                anagrama_t[letra] = anagrama_t[letra] + 1
            else:
                anagrama_t[letra] = 1        
        
        return anagrama_s == anagrama_t
