"""
LeetCode 217: Contains Duplicate
Link: https://leetcode.com/problems/contains-duplicate/

Padrão: Hash Set
Complexidade de Tempo: O(N)
Complexidade de Espaço: O(N)

Descrição:
Verifica se algum valor aparece pelo menos duas vezes no array.
Utiliza um conjunto (set) para realizar buscas em tempo constante O(1).
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        vistos = set()
        for num in nums:
            if num in vistos:
                return True
            vistos.add(num)
        return False
