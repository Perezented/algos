color0 = [2, 1, 0]
color1 = [2, 0, 2, 1, 1, 0]


def sortColors(nums):
    print(nums)
    i = 0
    print(nums[i])
    while i != len(nums)-1:
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        elif nums[i] < nums[i - 1]:
            print(nums[i - 1], 'is less')
            nums[i], nums[i - 1] = nums[i - 1], nums[i]

        else:
            i += 1

    print('End: ', nums)


sortColors(color0)
sortColors(color1)
