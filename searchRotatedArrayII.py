from collections import defaultdict
class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        nums_count = defaultdict(int)

        for num in nums:
            nums_count[nums] += 1

        return target in nums_count

    def search(self, nums: list[int], target: int) -> bool:
        # Initialize the lo and hi pointers for binary search
        lo, hi = 0, len(nums) - 1

        # Iterate until lo is less than or equal to hi
        while lo <= hi:
            # Initialize the midway pointer
            mid = (lo + hi) // 2

            # Stop iterating when the target is found
            if nums[mid] == target:
                return True

            # If all numbers are equal, increment lo, decremenet hi, and move to the next iteration
            if nums[lo] == nums[mid] == nums[hi]:
                lo += 1
                hi -=1
            # If the value at lo is less than or equal to the value at mid, the pivot is on the right size of the split.
            elif nums[lo] <= nums[mid]:
                # If the target falls between lo and mid, move hi to where mid was (minus one since mid was not the target)
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                # Otherwise, move lo to where mid was (plus one since mid was not the target)
                else:
                    lo = mid + 1
            # If not, the pivot is on the left side of the split.
            else:
                # if the target falls between mid and hi, move lo to where mid was (plus one since mid was not the target)
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                # Otherwise, move hi to wher mid was (minus one since mid was not the target)
                else:
                    hi = mid - 1

        # If the loop was not escaped, the value was not found, so return False
        return False