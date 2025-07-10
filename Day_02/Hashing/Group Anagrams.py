"""Group Anagrams

Given list of strings, group them as list of anagram groups."""

def groupAnagrams(strs):
    groups = {}
    for word in strs:
        key = ''.join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))





