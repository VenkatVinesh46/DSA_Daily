"""Part 1: Logic-Focused Problems (10)
These require no shortcuts — just loops, functions, sets, and dictionaries.

First Unique Character
Given a string, return the index of the first non-repeating character.
Hint: Use a frequency counter and two passes.

Check if Rearrangement is Palindrome
Given a string, check if any permutation can form a palindrome.

Majority Element (> n/2)
Given an array, return the majority element if it exists.

Check if Two Strings are Isomorphic
Two strings are isomorphic if there's a one-to-one mapping between characters.

Word Pattern Match
Pattern = "abba", String = "dog cat cat dog" → True
Map pattern characters to words.

First Repeating Element
Return the first element that repeats in a list.

Frequency Sort
Sort elements of a list in decreasing order of frequency.

Reconstruct Itinerary Path
You're given start and end city pairs. Reconstruct the trip.

Unique Characters Substring Count
Count substrings with all unique characters in a string.

Ransom Note Check
Given two strings magazine and note, return True if the note can be constructed using magazine characters."""
from scipy.signal import freqs


#First Unique Character

def first_unique_char(arr):
    freq={}
    for i in range(len(arr)):
        if arr[i] not in freq:
            freq[arr[i]] = 1
        else:
            freq[arr[i]] += 1
    for key in arr:
        if freq[key]==1:
            return key

    return None

#Check if Rearrangement is Palindrome

def can_form_palindrome(arr):
    freq={}
    for ch in arr:
        freq[ch] = freq.get(ch, 0) + 1
    odd_count = 0
    for count in freq.values():
        if count%2!=0:
            odd_count += 1
    return odd_count<=1


# Majority Element

def majority_element(arr):
    freq = {}
    for ch in arr:
        freq[ch] = freq.get(ch, 0) + 1

    length = len(arr)
    for key in freq:
        if freq[key] > length // 2:
            return key

    return None

# Isomorphic strings

def is_isomorphic(arr1, arr2):
    if len(arr1) != len(arr2):
        return False

    map1 = {}
    map2 = {}

    for ch1, ch2 in zip(arr1, arr2):
        if ch1 in map1:
            if map1[ch1] != ch2:
                return False
        else:
            map1[ch1] = ch2

        if ch2 in map2:
            if map2[ch2] != ch1:
                return False
        else:
            map2[ch2] = ch1

    return True

#Word Pattern Match

def word_pattern(pattern, s):
    words = s.split()


    if len(pattern) != len(words):
        return False

    char_to_word = {}
    word_to_char = {}


    for ch, word in zip(pattern, words):
        if ch in char_to_word:
            if char_to_word[ch] != word:
                return False
        else:
            char_to_word[ch] = word

        if word in word_to_char:
            if word_to_char[word] != ch:
                return False
        else:
            word_to_char[word] = ch

    return True

#First Repeating Element

def first_repeating(arr):
    freq = {}
    for ch in arr:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in freq:
        if freq[ch]>1:
            return ch
    return False


#Frequency Sort

def frequency_sort(arr):
    freq = {}
    for ch in arr:
        freq[ch] = freq.get(ch, 0) + 1

    sorted_arr=sorted(freq.items(), key=lambda x: x[1], reverse=True)
    result=[]
    for ch,count in sorted_arr:
        result.extend([ch] * count)


    return result


#Unique Substrings

def count_unique_substrings(s):
    n=len(s)
    count=0
    for i in range(n):
        seen=set()
        for j in range(i,n):
            if s[j] in seen:
                break
            seen.add(s[j])
            count+=1
    return count


#Ransom Note Check

def ransom_note_check(magazine, note):
    if len(note)>len(magazine):
        return False
    freq={}
    for ch in magazine:
        freq[ch]=freq.get(ch, 0) + 1
    for ch in note:
        if ch not in freq:
            return False
        if freq[ch]>0:
            freq[ch]-=1
        else:
            return False
    return True





