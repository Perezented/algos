class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while n != 0:
            print(nums1)
            nums1[m] = nums2[n-1]
            m += 1
            n -= 1
        nums1.sort()
