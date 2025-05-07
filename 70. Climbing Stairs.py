class Solution:
    def climbStairs(self, n: int) -> int:
        slot_1, slot_2 = 1, 1
        for _ in range(n-1):
            temp_slot = slot_1
            slot_1 += slot_2
            slot_2 = temp_slot
        return slot_1

# Time Complexity: O(N)
# Space Complexity: O(1)
