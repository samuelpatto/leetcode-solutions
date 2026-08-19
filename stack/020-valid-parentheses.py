"""
LeetCode 20: Valid Parentheses
Link: https://leetcode.com/problems/valid-parentheses/

Padrão: Stack (Pilha - LIFO)
Complexidade de Tempo: O(N)
Complexidade de Espaço: O(N)

Descrição:
Verifica a validade do fechamento de escopos em uma string de símbolos.
Utiliza uma pilha para armazenar os caracteres de abertura e valida se cada
caractere de fechamento corresponde ao topo atual da pilha.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        pilha = []
        mapeamento = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            
            if char in mapeamento:
                if pilha:
                    ultimo_item = pilha.pop()
                else:
                    ultimo_item = "#"
                
                if mapeamento[char] != ultimo_item:
                    return False
            else:
                pilha.append(char)
        return len(pilha) == 0
