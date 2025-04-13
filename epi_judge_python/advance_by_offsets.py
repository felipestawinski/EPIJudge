from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    if len(A) == 1: return True
    for i in range(len(A)):
        if A[i] == 0:
            counter = 1
            for j in range(i-1, -1, -1):
                if i == len(A)-1:
                    if A[j] >= counter:
                        break
                    
                if A[j] > counter:
                    break
        
                counter += 1
            if counter == i+1:
                return False
            
    return True
               


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
