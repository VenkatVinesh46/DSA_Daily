#K Frequent
import operator


def frequent(arr, k):
    freq = {}
    for i in arr:
        freq[i] = freq.get(i, 0) + 1
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_freq[:k]


