def countGoodSubstrings(s):
    l = 0
    r = 2
    count = 0
    while r < len(s):
        if s[l] != s[l + 1] and s[l] != s[r] and s[l + 1] != s[r]:
            count += 1
            l += 1
            r += 1
        else:
            l += 1
            r += 1
    return count

    # count = 0
    # prev_str = ""
    #
    # for i in range(0, len(s) - 2):
    #     low = i
    #     high = i + 2
    #     unique = 0
    #
    #     while low != high:
    #         if low==0 and high == i+2 and s[low] != s[high]:
    #             prev_str = s[high]
    #             high -= 1
    #             unique += 1
    #         elif low >= 0 and s[low] != s[high]:
    #             if s[high] != prev_str:
    #                 prev_str = s[high]
    #                 high -= 1
    #                 unique += 1
    #             else:
    #                 break
    #         else:
    #             break
    #
    #     if unique == 2:
    #         count += 1
    # return count

# s = "qyyqdpcupszzqrjxggqbqwxelaftnqpmihcqq"
# print(countGoodSubstrings(s))

s= "xyzzaz"
print(countGoodSubstrings(s))