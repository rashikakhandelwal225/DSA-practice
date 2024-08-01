def halveArray(nums):
    from collections import deque
    ops = 0
    hq = deque([])
    nums.sort()
    og = sum(nums)
    ct = og
    while 2 * ct > og:
        if hq and hq[-1] > nums[-1]:
            new_num = hq.pop()
        else:
            new_num = nums.pop()
        new_num /= 2
        ct -= new_num
        hq.appendleft(new_num)
        ops += 1

    return ops

nums = [5,19,8,1]
print(halveArray(nums))
nums = [3,8,20]
print(halveArray(nums))
nums = [10,
264481,
954862,
874563,
999999,
874521,
987456,
11112,
54654,
654654,
879654 ]
print(halveArray(nums))

