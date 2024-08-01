def numIdenticalPairs(nums) :
    hashmap = {}
    counter = 0
    for num in nums:
        if num not in hashmap:
            hashmap[num] = 1
        else:
            counter += hashmap[num]
            hashmap[num] += 1
    return counter
    # res = 0
    # m = {}
    # for n in nums:
    #     if n not in m:
    #         m[n] = 0
    #     m[n] += 1
    #     res += m[n] - 1
    #
    # return res

nums = [1,2,3,1,1,3]
print(numIdenticalPairs(nums))
