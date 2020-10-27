nums0 = [1, 1, 2]  # 2, nums = [1,2]
nums1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]  # 5, nums = [0,1,2,3,4]
nums2 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3,
         3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4]  # 5, nums = [0,1,2,3,4]
nums3 = [1, 1]
nums4 = [1, 1, 1, 1]


def remove_dupes_from_list(nums):
    # print(nums)

    def prepend(nums, secondNums):
        for i in secondNums:
            nums.insert(0, i)
    for i in range(len(nums)):
        if i != len(nums) - 1:

            if nums[i] < nums[i + 1]:
                nums.append(nums[i])
            elif nums[i] > nums[i + 1] and nums[i] != nums[-1]:
                nums.append(nums[i])
                prepend(nums, sorted(nums[i + 1:], reverse=True))
                print(int(len(nums[i + 1:]) / 2), nums[i+1:])
                return int(len(nums[i + 1:]) / 2)
            elif nums[i] == nums[i + 1] and nums[i] == nums[-1]:
                print(nums)
                nums.insert(0, nums[i])
                print(len(nums[i+1:])/2)
                return int(len(nums[i+1:])/2)


remove_dupes_from_list(nums0)
print('-'*40)
remove_dupes_from_list(nums1)
print('-'*40)
remove_dupes_from_list(nums2)
print('-'*40)
remove_dupes_from_list(nums3)
print('-'*40)
remove_dupes_from_list(nums4)
print('-'*40)
