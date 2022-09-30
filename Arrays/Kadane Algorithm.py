def maxSubArray(nums: list[int]) -> int:
    max_sum = nums[0]
    cur_sum = nums[0]
    for i in range(1, len(nums)):
        if cur_sum > 0:
            cur_sum += nums[i]
        else:
            cur_sum = nums[i]
        if cur_sum > max_sum:
            max_sum = cur_sum
    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4] # output = 6
res = maxSubArray(nums=nums)
print(res)