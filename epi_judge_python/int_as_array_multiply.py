from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    # TODO - you fill in here.
    sign = -1 if num1[0] < 0 or num2[0] < 0 else 1
    int_num = 1
    m = 1

    for n1 in reversed(range(num1)):
        m = 1
        for n2 in reversed(range(num2)):
            int_num += num2[n2] * num1[n1] * m
    return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
