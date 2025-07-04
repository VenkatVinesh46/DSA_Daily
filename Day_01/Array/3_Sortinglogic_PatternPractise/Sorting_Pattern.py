"""🔹 Sorting Logic (5 Problems) – Manual only
Bubble sort manually

Selection sort manually

Sort descending order manually

Count number of swaps in bubble sort

Sort and return k-th smallest

🔹 Pattern Practice (5 Problems) – Using array as logic base
Find pair with sum = target (brute force)

Check for duplicates (manual logic)

Return array without using list slicing

Find first repeating element

Count how many times each element appears (without dict)"""


#Bubble_sort
def bubble_sort(arr):
    length=0
    for i in arr:
        length+=1
    for i in range(length-1):
        for j in range(length-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

#Selection_sort

def selection_sort(arr):
    length=0
    for i in arr:
        length+=1
    for i in range(length):
        min_index=i
        for j in range(i+1,length):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[min_index],arr[i]=arr[i],arr[min_index]
    return arr

#Sort descending order manually

def descending_order(arr):
    length = 0
    for _ in arr:
        length += 1

    for i in range(length - 1):
        for j in range(length - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

#Count number of swaps in bubble sort

def count_swaps_in_bubble_sort(arr):
    length = 0
    for _ in arr:
        length += 1
    no_swaps = 0

    for i in range(length-1):
        for j in range(length-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                no_swaps += 1
    return no_swaps

#Sort and return k-th smallest

def sort_return_kth_smallest(arr, k):
    length=0
    for i in arr:
        length+=1
    for i in range(length-1):
        for j in range(length-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr[k-1]



#Find pair with sum = target (brute force)

def target_pair(arr,value):
    length=0
    for i in arr:
        length+=1
    for i in range(length):
        if arr[i]+arr[i+1]==value:
            return arr[i], arr[i + 1]
        break
    else:
        print("Target not found")

#Check for duplicates (manual logic)

def check_duplicates(arr):
    length=0
    list_of_duplicates=[]
    for i in arr:
        length+=1
    for i in range(length):
        for j in range(i+1,length):
            if arr[i]==arr[j] and arr[i] not in list_of_duplicates:
                list_of_duplicates+=arr[i]
    return list_of_duplicates


#Find first repeating element

def traverse(arr):
    length=0
    array=[]
    for i in arr:
        length+=1
    for i in range(length):
        array.append(arr[i])

    return array

#Find first repeating element

def first_repeating(arr):
    length = 0
    for _ in arr:
        length += 1

    for i in range(length):
        for j in range(i + 1, length):
            if arr[i] == arr[j]:
                return arr[i]  # Return the first repeating element immediately

    return "No repeating element found"


#Count how many times each element appears (without dict)

def count_all_frequencies(arr):
    length = 0
    for _ in arr:
        length += 1

    for i in range(length):
        count = 0
        for j in range(length):
            if arr[i] == arr[j]:
                count += 1
        print(arr[i], "appears", count, "times")






