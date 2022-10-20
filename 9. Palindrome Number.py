# Approach without converting the integer to a string
# Space complexity = O(1)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        elif 0 <= x < 10: return True
        else:
            divider = 1
            # Get the largest power of 10, which is equal or smaller than x
            # If x = 1000021, divider = 1000000
            while x >= (10 * divider):
                divider *= 10
                
            while x != 0:
                left_digit = x // divider
                right_digit = x % 10
                
                if left_digit != right_digit: return False
                else:
                    x = x % divider     # Remove left digit
                    x = x // 10     # Remove right digit
                    divider = divider // 100   # Remove 2 digits(0s) from right
            return True
        
# Approach 2 with converting the integer to a string
# Time complexity = O(n)    # n = no. of digits in x
# Space complexity = O(1)

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0: return False
#         elif 0 <= x < 10: return True
#         else:
#             s = str(x)
#             for i in range(len(s) // 2):    # Checking whether left and right pointers have the same value
#                 if s[i] != s[-(i+1)]:
#                     return False
#             return True

# Approach 1 with converting the integer to a string
# Time complexity = O(n)    # n = no. of digits in x
# Space complexity = O(1)

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0: return False
#         elif 0 <= x < 10: return True
#         else:
#             s = str(x)
#             return s == s[::-1]
