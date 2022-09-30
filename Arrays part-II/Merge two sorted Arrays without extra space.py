def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    p1 = m-1
    p2 = n-1
    i = len(nums1) - 1
    
    while p2 >= 0:
        if p1>= 0 and nums1[p1] > nums2[p2]:
            nums1[i] = nums1[p1]
            p1 -= 1
            i -= 1
        else:
            nums1[i] = nums2[p2]
            p2 -= 1
            i -= 1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6] 
n = 3
# Output: [1,2,2,3,5,6]
merge(nums1=nums1, m=m, nums2=nums2, n=n)
print(nums1)