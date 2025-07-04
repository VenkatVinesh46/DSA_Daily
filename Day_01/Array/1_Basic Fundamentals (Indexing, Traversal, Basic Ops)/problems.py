"""A. Basic Fundamentals (Indexing, Traversal, Basic Ops)
Find the maximum element in the array

Find the minimum element in the array

Reverse the array (in-place)

Search for an element and return its index (or -1 if not found)

Count frequency of a given element in the array

Calculate sum and average of all elements

Find the second maximum number in the array (without sorting)

Find the second minimum number (without sorting)

Find the difference between maximum and minimum elements"""


#Find the maximum element in the array
def find_max(arr):
    max_val = arr[0]  # Avoid using 'max' as a variable name
    length = 0
    for i in arr:
        length += 1

    for i in range(length):
        if arr[i] > max_val:
            max_val = arr[i]

    return max_val

#Find the minimum element in the array

def find_min(arr):
    min_val = arr[0]
    length = 0
    for i in arr:
        length += 1
    for i in range(length):
        if arr[i]< min_val:
            min_val = arr[i]
    return min_val

#Reverse the array (in-place)
def reverse_array(arr):
    length = 0
    for _ in arr:
        length += 1
    for i in range(length // 2):
        arr[i], arr[length - 1 - i] = arr[length - 1 - i], arr[i]
    return arr

#Search for an element and return its index (or -1 if not found)
def search(arr,k):
    length = 0
    for _ in arr:
        length += 1
    for i in range(length):
        if arr[i] == k:
            return i
    return -1
#Count frequency of a given element in the array

def count_frequency(arr, k):
    count = 0
    for element in arr:
        if element == k:
            count += 1
    return count

#Calculate sum and average of all elements

def sum_average(arr):
    total = 0
    length = 0
    for _ in arr:
        length += 1
    for i in range(length):
        total += arr[i]
    average = total / length
    return total, average

#Find the second maximum number in the array (without sorting)

def second_max(arr):
    length = 0
    for _ in arr:
        length += 1

    maximum = float('-inf')
    second_max = float('-inf')

    for i in range(length):
        if arr[i] > maximum:
            second_max = maximum
            maximum = arr[i]
        elif arr[i] > second_max and arr[i] != maximum:
            second_max = arr[i]

    if second_max == float('-inf'):
        return None  # Handle case when no second max exists
    return second_max

#Find the second minimum number (without sorting)

def second_min(arr):
    length = 0
    for _ in arr:
        length += 1

    minimum = float('inf')
    second_min = float('inf')

    for i in range(length):
        if arr[i] < minimum:
            second_min = minimum
            minimum = arr[i]
        elif arr[i] < second_min and arr[i] != minimum:
            second_min = arr[i]

    if second_min == float('inf'):
        return None  # No second minimum exists
    return second_min

#Find the difference between maximum and minimum elements"

def diff_max_min(arr):
    length = 0
    max_val = float('-inf')
    min_val = float('inf')

    for _ in arr:
        length += 1

    for i in range(length):
        if arr[i] > max_val:
            max_val = arr[i]
        if arr[i] < min_val:
            min_val = arr[i]

    return max_val - min_val
