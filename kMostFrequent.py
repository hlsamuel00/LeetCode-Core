import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Initialize a defaultdict of integers to store counts of unique values in the input list
        unique_counts = defaultdict(int)
        
        # Calculate the counts of unique values
        for num in nums:
            unique_counts[num] += 1

        # Initialize an empty list to serve as a min-heap
        pq = []

        # Iterate through the count dictionary and add a num_count/num tuple to the min-heap while maintaining size k.
        for num, num_count in unique_counts.items():
            if len(pq) < k:
                heapq.heappush(pq, (num_count, num))
            elif num_count > pq[0][0]:
                heapq.heappushpop(pq, (num_count, num))

        # Return the unique nums from the heap
        return [heapq.heappop(pq)[1] for _ in range(k)]