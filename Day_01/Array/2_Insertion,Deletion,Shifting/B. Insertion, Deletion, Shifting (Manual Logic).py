"""B. Insertion, Deletion, Shifting (Manual Logic)
Insert an element at a specific index (manually shift right)

Delete an element from a specific index (manually shift left)

Remove all occurrences of a specific element



Remove duplicates (without using set() or dict)

Merge two arrays manually

Left rotate array by one position

Right rotate array by one position

Check if element exists (linear search)
"""

#Insert an element at a specific index (manually shift right)

def insert_at_idx(arr, idx, val):
    length=0
    for i in arr:
        length+=1
    new_arr=[0]*(length+1)
    for i in range(idx):
        new_arr[i]=arr[i]
    new_arr[idx]=val
    for i in range(idx,length):
        new_arr[i+1]=arr[i]
    return new_arr

#Delete an element from a specific index (manually shift left)




def delete_at_index(arr, index):
    length = 0
    for _ in arr:
        length += 1

    if index < 0 or index >= length:
        return "Invalid index"

    new_arr = [0] * (length - 1)

    for i in range(index):
        new_arr[i] = arr[i]

    for i in range(index + 1, length):
        new_arr[i - 1] = arr[i]

    return new_arr

#Remove all occurrences of a specific element
def remove_all_occurrences(arr, k):
    length = 0
    for _ in arr:
        length += 1

    i = 0
    while i < length:
        if arr[i] == k:
            arr = delete_at_index(arr, i)
            length -= 1  # array got smaller
        else:
            i += 1
    return arr


# ✅ Remove duplicates manually (without set or dict)
def remove_duplicates(arr):
    length = 0
    for _ in arr:
        length += 1

    i = 0
    while i < length:
        j = i + 1
        while j < length:
            if arr[i] == arr[j]:
                arr = delete_at_index(arr, j)
                length -= 1
                # Don't increment j, check current position again
            else:
                j += 1
        i += 1
    return arr
#Merge two arrays manually

def merge_arrays(arr1, arr2):
    merged_arr = []
    len_arr1=0
    len_arr2=0
    for i in arr1:
        len_arr1+=1
    for i in arr2:
        len_arr2+=1
    for i in range(len_arr1):
        merged_arr.append(arr1[i])
    for i in range(len_arr2):
        merged_arr.append(arr2[i])
    return merged_arr

#Left rotate array by one position

def left_rotate(arr):
    length =0
    for i in arr:
        length+=1
    left_rot_arr=[0]*length
    for i in range(length):
        left_rot_arr[i]=arr[(i+1)%length]
    return left_rot_arr

#Right rotate array by one position

def right_rotate(arr):
    length =0
    for i in arr:
        length+=1
    right_rot_arr=[0]*length
    for i in range(length):
        right_rot_arr[(i+1)%length]=arr[i]
    return right_rot_arr

#Check if element exists (linear search)

def liner_search(arr, k):
    length = 0
    for i in arr:
        length+=1
    for i in range(length):
        if arr[i] == k:
            return True

    return False
















