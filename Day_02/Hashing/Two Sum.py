""" Two Sum

Given array and target, find indices of two numbers adding up to target (unordered array)."""

def two_sum(arr, target):
    freq = {}
    for idx, num in enumerate(arr):
        diff = target - num
        if diff in freq:
            return [freq[diff], idx]
        freq[num] = idx
    return False
