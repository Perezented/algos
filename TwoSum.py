# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# Example 1:

# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]
# Example 3:

# Input: nums = [3, 3], target = 6
# Output: [0, 1]


# Constraints:

# 2 <= nums.length <= 105
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.


numList1 = [11, 2, 15, 7]   # to equal 9, [1, 3]
numList2 = [3, 2, 4]    # to equal 6, [1, 2]
numList3 = [0, 4, 3, 0]  # to equal 0, [0, 3]
numList4 = [2, 5, 5, 11]  # to equal 10, [1, 2]


def twoSum(nums, target):
    currNum = target
    index = 0
    jindex = 0

    def findSubNumbers(numsList, index, jindex, currNum):
        if index == jindex:
            index += 1
        while numsList[index] + numsList[jindex] != currNum:
            if index != len(numsList) - 1:
                index += 1
            else:
                index = 0
                jindex += 1
        if jindex != index:
            return [jindex, index]
        else:
            index += 1
            return findSubNumbers(nums, index, jindex, currNum)

    return findSubNumbers(nums, index, jindex, currNum)

#     # start off, sub target with first jindex
#     if currNum - numsList[jindex] > 0:
#         currNum -= numsList[jindex]
#     elif currNum - numsList[jindex] < 0:
#         jindex += 1
#         return findSubNumbers(numsList, index, jindex, currNum)
#     elif currNum == 0:
#         if index == jindex and index < len(numsList)-1:
#             index += 1
#         if numsList[jindex]+numsList[index] != currNum:
#             index += 1
#         else:
#             return [jindex, index]
#         return findSubNumbers(numsList, index, jindex, currNum)

#     # sub from the next number in the index, next index != jindex
#     while index != len(numsList):
#         if index == jindex and index < len(numsList)-1:
#             index += 1
#         # looking for currNum to be zero
#         if (currNum - numsList[index]) == 0:
#             return [jindex, index]
#         index += 1
#     # if currNum minus next index != 0 then its not our num.
#     # if index is == numsList len, then move to next jindex
#     if index == len(numsList):
#         index = 0
#         if jindex < len(numsList)-1:
#             jindex += 1
#         currNum = target
#         return findSubNumbers(nums, index, jindex, currNum)
# return findSubNumbers(nums, index, jindex, currNum)


twoSum(numList1, 9)
twoSum(numList2, 6)
twoSum(numList3, 0)
twoSum(numList4, 10)
