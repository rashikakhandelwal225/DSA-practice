def findDifferentBinaryString(self, nums):
    """
    :type nums: List[str]
    :rtype: str
    """
    for i in range(len(nums) + 1):
        new_num = format(i, "b").zfill(len(nums[0]))
        if new_num not in nums:
            return new_num