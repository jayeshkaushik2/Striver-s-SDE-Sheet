def findDuplicate(nums: list[int]) -> int:
    temp = dict()
    for ele in nums:
        if ele in temp:
            return ele
        else:
            temp[ele] = 1
    
    # nums.sort()
    # prev = nums[0]
    # for i in range(1, len(nums)):
    #     if nums[i] == prev:
    #         return prev
    #     prev = nums[i]

nums = [1,3,4,2,2]
# Output: 2
res = findDuplicate(nums=nums)
print(res)