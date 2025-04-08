from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    # TODO - you fill in here.
    if A[-1] != 9:
        A[-1] += 1
        return A
    else:
        x = 1
        flag = 0
        for i in reversed(range(len(A))):
            curr_sum = A[i] + x
            print(f"curr_sum: {curr_sum}")
            if curr_sum == 10:
                A[i] = 0
                x = 1
                flag += 1
            else:
                A[i] = curr_sum
                x = 0
                break
        if flag == len(A):
            return [1] + A

    return A



    return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
