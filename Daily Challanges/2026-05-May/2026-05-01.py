from collections import defaultdict
def group_anagrams(words):
    groups = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word))
        groups[sorted_word].append(word)
    return list(groups.values())

print(group_anagrams(["listen", "silent", "hello", "enlist", "world"]))
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))