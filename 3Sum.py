class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Sort the input list in ascending order
        nums.sort()

        # Initialize an empty list to store the triplets found
        triplets = []

        # Iterate through each value in num. If the current num is equal to the previous num, skip it. Use the helper function to find the two-sum of the opposite of num and store the value in the triplets list.
        for idx, num in enumerate(nums):
            if idx and num == nums[idx - 1]:
                continue
            
            self.twoSum(nums[idx+1:], -num, triplets)
        
        # Return triplets list
        return triplets

    # This helper function finds the two-sum of the remaining list in O(n) time.
    def twoSum(self, nums: list[int], target: int, triplets: list[list[int]]) -> list[int]:
        # Initialize two pointers to the front and end of the list.
        lo, hi = 0, len(nums) - 1

        # Iterate while the lo pointer is less than the hi pointer.
        while lo < hi:

            # If the sum of the values at the pointers is greater than the target, decrement the hi pointer
            if nums[lo] + nums[hi] > target:
                hi -= 1
            # If the sum of the values at the pointers is less than the target, increment the lo pointer
            elif nums[lo] + nums[hi] < target:
                lo += 1
            # Otherwise, the values are equal, append the triplet to the list, increase lo until it no longer equals the next value, and decrease hi until it no longer equals the previous value.
            else:
                triplet = [-target, nums[lo], nums[hi]]
                triplets.append(triplet)
                while lo < hi and nums[lo] == triplet[1]:
                    lo += 1
                while lo < hi and nums[hi] == triplet[2]:
                    hi -= 1
        