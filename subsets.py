class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        # Initialize an empty list to hold all subsets found
        subsets = []

        # Begin the DFS traversal at the start of the input
        self._get_subsets(0, [], nums, subsets)

        # Return the list of subsets that were found
        return subsets
       
    # This helper method employs DFS to get all combinations of subsets from the input list.
    def _get_subsets(self, index: int, cur_subset: list[int], nums: list[int], combinations: list[list[int]]) -> None:
        # Base Case: If the index is equal to the length of teh input list, we add the combination to the list by making a deep copy of the current subset.
        if index == len(nums):
            combinations.append(cur_subset[:])
            return

        # Pre-recurse: None

        # Recurse: Recursively traverse the next index without and with the value at the current index in the input list.
        self._get_subsets(index + 1, cur_subset, nums, combinations)
        self._get_subsets(index + 1, cur_subset + [nums[index]], nums, combinations)

        # Post-recurse: None