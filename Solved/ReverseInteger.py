# 7. Reverse Integer
# Easy

# 3903

# 6060

# Add to List

# Share
# Given a 32-bit signed integer, reverse digits of an integer.

# Note:
# Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
# Example 4:

# Input: x = 0
# Output: 0


# Constraints:

# -231 <= x <= 231 - 1

class Solution:
    def reverse(self, x: int) -> int:
        print(x, bin(x), len(bin(x)))
        y = ''

        for lett in str(x):
            if lett != '-':
                y = lett + y
        if str(x)[0] == '-':
            y = '-' + y
        if len(bin(int(y))) < 35:
            return int(y)
        else:
            print('thats a big number', len(bin(int(y))))
            return 0
