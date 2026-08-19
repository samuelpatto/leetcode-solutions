"""
LeetCode 349: Intersection of Two Arrays
Link: https://leetcode.com/problems/intersection-of-two-arrays/

Padrão: Hash Set
Complexidade de Tempo: O(N + M)
Complexidade de Espaço: O(N)

Descrição:
Retorna um array com os elementos únicos presentes em ambos os conjuntos.
Utiliza conjuntos (sets) para garantir valores únicos e realizar a busca em O(1).
"""

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        resultado = []
        
        for num in nums2:
            
            if num in set1 and num not in resultado:
                
                resultado.append(num)
                
        return resultado
