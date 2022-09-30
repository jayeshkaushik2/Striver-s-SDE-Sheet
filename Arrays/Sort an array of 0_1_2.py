def sortColors(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    l = 0
    r = len(nums)-1
    m = 0
    while l <= r and m <= r:
        if nums[m] == 0:
            nums[l], nums[m] = nums[m], nums[l]
            l += 1
            m += 1
        elif nums[m] == 1:
            m += 1
        elif nums[m] == 2:
            nums[m], nums[r] = nums[r], nums[m]
            r -= 1

nums = [2,0,2,1,1,0] # output [0,0,1,1,2,2]
sortColors(nums)
print(nums)