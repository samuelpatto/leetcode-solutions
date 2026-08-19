"""
LeetCode 2325: Decode the Message
Link: https://leetcode.com/problems/decode-the-message/

Padrão: Hash Map (Tabela de Mapeamento)
Complexidade de Tempo: O(N + M) - Onde N é o tamanho da chave e M da mensagem
Complexidade de Espaço: O(1) - Guardamos no máximo 26 letras do alfabeto

Descrição:
Mapeia a primeira aparição de cada letra da 'key' para as letras do alfabeto (a-z).
Em seguida, decodifica a mensagem substituindo os caracteres com base na tabela criada.
"""

class Solution:
    def decodeMessage(self, key: str, mensagem: str,) -> str:
        tabela = {}
        letras_alfabeto = "abcdefghijklmnopqrstuvwxyz"
        indice_alfabeto = 0
        
        for caractere in key:
            if caractere != " " and caractere not in tabela:
                tabela[caractere] = letras_alfabeto[indice_alfabeto]
                indice_alfabeto += 1
        
        resultado = ""
        for letra in mensagem:
            if letra == " ":
                resultado = resultado + " "
            else:
                resultado = resultado + tabela[letra]
        
        return resultado 
