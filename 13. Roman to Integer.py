class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_to_value = {"I": 1, "V": 5,  "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        value = symbol_to_value[s[0]]

        for index in range(1, len(s)):
            if symbol_to_value[s[index]] > symbol_to_value[s[index - 1]]:
                value = value - symbol_to_value[s[index - 1]] + symbol_to_value[s[index]] - symbol_to_value[s[index - 1]]
            else:
                value = value + symbol_to_value[s[index]]
        return value

# Time Complexity: O(N)
# Space Complexity: O(1)
