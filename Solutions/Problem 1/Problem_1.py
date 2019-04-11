# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.


def solution(numbers, k):
    l = len(numbers)
    for i in range(0, l-1):
        for j in range(i + 1, l):
            if numbers[i] + numbers[j] == k:
                return True
    return False


if __name__ == "__main__":
    numbers = [int(x) for x in input().split()]
    k = int(input())
    print(solution(numbers, k))
