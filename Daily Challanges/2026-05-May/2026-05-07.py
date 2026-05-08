def get_longest_substring(s):
    n = len(s)
    window_size = len(s)-1
    memory = set()
    while window_size > 0:
        for i in range(n-window_size+1):
            window = s[i:i+window_size]
            if window in memory:
                return window
            memory.add(window)
        window_size -= 1
        memory = set()
    return s

print(get_longest_substring("abracadabra"))
print(get_longest_substring("hello world hello"))