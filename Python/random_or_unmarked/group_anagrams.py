from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)

    for s in strs:
        count = [0] * 26

        for char in s:
            count[ord(char) - ord('a')] += 1
        
        groups[tuple(count)].append(s)
    
    return list(groups.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
print(group_anagrams([""])) # Output: [[""]]
print(group_anagrams(["a"])) # Output: [["a"]]
