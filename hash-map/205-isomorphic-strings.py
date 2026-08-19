"""
LeetCode 205: Isomorphic Strings
Link: https://leetcode.com/problems/isomorphic-strings/

Padrão: Hash Map (Mapeamento Bijetivo)
Complexidade de Tempo: O(N)
Complexidade de Espaço: O(1) - Limita-se ao tamanho do alfabeto/ASCII

Descrição:
Verifica se os caracteres de uma string 's' podem ser substituídos para formar 't'.
Garante uma relação de um-para-um (bijetiva) usando dois dicionários para mapear
as correspondências s -> t e t -> s de forma consistente.
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapeamento_s_t = {}
        mapeamento_t_s = {}
        
        for letra_s, letra_t in zip(s, t):
           
            if letra_s in mapeamento_s_t and mapeamento_s_t[letra_s] != letra_t:
                return False
            if letra_t in mapeamento_t_s and mapeamento_t_s[letra_t] != letra_s:
                return False
            
            
            mapeamento_s_t[letra_s] = letra_t
            mapeamento_t_s[letra_t] = letra_s
            
        return True
