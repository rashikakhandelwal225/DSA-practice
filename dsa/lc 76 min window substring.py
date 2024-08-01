def minWindow(s, t):
    if not s or not t:
        return ""

    t_hashmap = {}
    for ch in t:
        if ch in t_hashmap:
            t_hashmap[ch] += 1
        else:
            t_hashmap[ch] = 1

    count = 0
    start_index = 0
    min_len = float("inf")
    l = 0
    hashmap = {}

    while l < len(s):
        # Adjust window to include s[l]
        if s[l] in t_hashmap:
            if t_hashmap[s[l]] > 0:
                count += 1
            t_hashmap[s[l]] -= 1

        # Check if current window contains all characters of t
        while count == len(t):
            # Update min length of window
            if l - start_index + 1 < min_len:
                min_len = l - start_index + 1
                hashmap[min_len] = s[start_index:l + 1]

            # Try to contract from the left
            if s[start_index] in t_hashmap:
                t_hashmap[s[start_index]] += 1
                if t_hashmap[s[start_index]] > 0:
                    count -= 1

            start_index += 1

        l += 1

    if min_len == float("inf"):
        return ""
    else:
        return hashmap[min_len]

    # t_hashmap = {}
    # for ch in t:
    #     if ch not in t_hashmap:
    #         t_hashmap[ch] = 1
    #     else:
    #         t_hashmap[ch] += 1
    # count = 0
    # start_index = 0
    # min_len = len(s)
    # l = 0
    # prev_min = min_len
    # r = len(s)
    # hashmap = {}
    #
    # while l < r:
    #     if s[l] in t_hashmap and t_hashmap[s[l]] == 0:
    #         t_hashmap[s[l]] == 0
    #         l += 1
    #         count += 1
    #     elif s[l] in t_hashmap:
    #         count += 1
    #         t_hashmap[s[l]] -= 1
    #         l += 1
    #     else:
    #         l += 1
    #         count += 1
    #
    #     flag = all(value == 0 for value in t_hashmap.values())
    #
    #     if flag == True:
    #         # update min length of window
    #         min_len = min(min_len, count)
    #         # if min_len >= len(t):
    #         #     hashmap[min_len] = s[start_index:start_index + count]
    #         if count <= prev_min and min_len >= len(t):
    #             hashmap[count] = s[start_index:start_index + count]
    #             prev_min = count
    #         else:
    #             min_len = prev_min
    #
    #         # if min_len >= len(t):
    #         #     hashmap[min_len] = s[start_index:start_index + count]
    #
    #         start_index += 1
    #         l = start_index
    #         count = 0
    #         for ch in t:
    #             if ch not in t_hashmap:
    #                 t_hashmap[ch] = 1
    #             else:
    #                 t_hashmap[ch] += 1
    #
    # print(hashmap)
    # if hashmap != {}:
    #     return hashmap[min_len]
    # else:
    #     return ""

# s = "abc"
# t= "ac"
# print(minWindow(s, t))

s="cabwefgewcwaefgcf"
t ="cae"
print(minWindow(s, t))

# s = "bbaa"
# t = "aba"
# print(minWindow(s, t))
#
# s = "ab"
# t = "a"
# print(minWindow(s, t))
#
# s = "ADOBECODEBANC"
# t = "ABC"
# print(minWindow(s, t))
#
# s = "a"
# t = "a"
# print(minWindow(s, t))
#
# s = "a"
# t = "aa"
# print(minWindow(s, t))
#
# s = "a"
# t = "b"
# print(minWindow(s, t))


