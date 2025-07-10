"""✅ Problem: Valid Anagram
Description:
Given two strings s and t, write a function to determine if t is an anagram of s.

Two strings are anagrams if they contain the same characters with the same frequencies, just possibly in a different order."""

def validAnagram(s, t):
    if len(s) != len(t):
        return False

    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in t:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] < 0:
            return False

    return True
