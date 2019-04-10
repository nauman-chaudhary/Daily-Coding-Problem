# This problem was asked by Uber.
#
# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?
import math


def bruteforce(arr):
    final_arr = []
    for i in range(0, len(arr)):
        temp = arr[i]
        arr[i] = 1
        product = 1
        for x in arr:
            product *= x
        final_arr.append(product)
        arr[i] = temp
    return final_arr

if __name__ == "__main__":
    arr = [int(x) for x in input().strip().split()]
    print(bruteforce(arr))