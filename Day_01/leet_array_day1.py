# leet_array_day1.py
# ✅ Brute Force LeetCode Practice on Arrays

# 1. Two Sum


def two_sum(nums, target):
    #Brute Force only
    length = 0
    for _ in nums:
        length += 1

    found = False

    for i in range(length):
        for j in range(i + 1, length):
            if nums[i] + nums[j] == target:
                arr=[i,j]
                print(arr)
                found = True

    if not found:
        print("No such combination")


# 2. Best Time to Buy and Sell Stock
def max_profit(prices):
    # Brute force only
    length=0
    for price in prices:
        length += 1
    maximum_profit=0
    for i in range(length):
        for j in range(i + 1, length):
            profit = prices[j] - prices[i]
            if profit > maximum_profit:
                maximum_profit = profit
    return maximum_profit

# 3. Remove Duplicates from Sorted Array
def remove_duplicates(nums):
    length = 0
    for _ in nums:
        length += 1

    nums_dup_removed = []

    for i in range(length):
        is_present = False
        for val in nums_dup_removed:
            if nums[i] == val:
                is_present = True
                break
        if not is_present:
            nums_dup_removed.append(nums[i])

    return nums_dup_removed



# 4. Merge Sorted Array
def merge(nums1, m, nums2, n):
    # Without using built-ins
    i=m-1
    j=n-1
    k=m+n-1
    while i>=0 and j>=0:
        if nums1[i]>nums2[j]:
            nums1[k] = nums1[i]
            i-=1
        else:
            nums1[k] = nums2[j]
            j-=1
        k-=1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
    return nums1


# 5. Contains Duplicate
def contains_duplicate(nums):
    # Manual check
    length=0
    for num in nums:
        length += 1

    for i in range(length):
        for j in range(i + 1, length):
            if nums[i] == nums[j]:
                return True

    return False




# 6. Maximum Subarray
def max_subarray(nums):
    length=0
    for num in nums:
        length += 1
    max_sum=float('-inf')
    for i in range(length):
        curr_sum=0
        for j in range(i+1, length):
            curr_sum += nums[j]
            if curr_sum > max_sum:
                max_sum = curr_sum

    return max_sum








