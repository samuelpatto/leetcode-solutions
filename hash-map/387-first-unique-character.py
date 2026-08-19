"""
LeetCode 387: First Unique Character in a String
Link: https://leetcode.com/problems/first-unique-character-in-a-string/

Padrão: Hash Map (Two-Pass)
Complexidade de Tempo: O(N)
Complexidade de Espaço: O(1) - Limita-se a 26 caracteres minúsculos

Descrição:
Encontra o índice do primeiro caractere não repetido em uma string.
Faz uma primeira passada para contar a frequência dos caracteres em um dicionário
e uma segunda passada para encontrar o primeiro caractere com contagem igual a 1.
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        contagem = {}
        
        for letra in s:
            if letra in contagem:
                contagem[letra] = contagem[letra] + 1
            else:
                contagem[letra] = 1
        
        for i, letra in enumerate(s):
            if contagem[letra] == 1:
                return i
        
        return -1            
                
              
    
