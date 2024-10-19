#true_math

# Если делим на 0, то возвращается inf (знак бесконечности)
from math import inf


def dividetrue(first, second):
    if second == 0:
        return inf
    else:
        return first / second