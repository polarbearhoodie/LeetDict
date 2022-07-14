import math


def two_sum(arr_in: list[int], target: int) -> (int, int):
    ref = {}

    for i, en in enumerate(arr_in):
        g = ref.get(en, default=-1)
        if g != -1:
            return g, i
        else:
            ref[target - en] = i

    return -1, -1


def arbitrage(arr_in: list[int]) -> (int, int, float):
    a, b = -1, -1
    prior_min = 10000  # big number
    prior_cap = 0  # minimum number
    for i, en in enumerate(arr_in):
        if en < prior_min:
            prior_min = en
            a = i
        if en - prior_min > prior_cap:
            prior_cap = en - prior_min
            b = i

    return a, b, prior_cap


def contains_duplicate(arr_in: list[int]) -> bool:
    ref = {}
    for en in arr_in:
        if ref.get(en, False):
            return True
        else:
            ref[en] = True

    return False


# problem
def product_arr_less_self(arr_in: list[int]) -> list[int]:
    n = len(arr_in)

    # create the output array
    # O(n2 *m) need to speed up by factor of n or m
    # not allowed to vectorize
    j = []
    for i in range(n):
        j.append(1)

    prior = 1
    for i in range(n-1):
        prior *= arr_in[i]
        j[i+1] *= prior

    prior = 1
    for i in range(n-1):
        prior *= arr_in[n-i]
        j[n - 1 - i] *= prior

    return j


def max_subarray(arr_in: list[int]) -> int:
    max_sum = 0
    sum_so_far = 0
    for en in arr_in:
        sum_so_far += en
        if sum_so_far < 0:
            sum_so_far = 0

        if sum_so_far > max_sum:
            max_sum = sum_so_far

    return max_sum


# same idea as max subarray
# not necessarily? is there an O(n2)
def max_product(arr_in: list[int]) -> int:
    msf = 0
    swap = [1, 1]  # edge case if max is 0?

    for x in arr_in:
        swap = [x*y for y in swap]

        if max(swap) > msf:
            msf = max(swap)

        if x < 0:
            swap[0] = 1

        if x == 0:
            swap = [1, 1]

    return msf


def watershed(arr):
    start = 0
    end = len(arr) - 1
    msf = 0

    while start < end:
        lm = min(arr[start], arr[end]) * (end - start)
        if lm > msf:
            msf = lm

        if arr[start] <= arr[end]:
            start += 1
        else:
            end -= 1

    return msf

