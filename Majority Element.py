class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        counter = 0

        for value in nums:
            if counter == 0:
                candidate = value
            counter += (1 if value == candidate else -1)
        

        return candidate


"""
Boyer-Moore Voting algorithm. Consider element appears [N/2], majority element will balance on top at the end. Initialize candidate value and counter. 
If counter == 0, reset candidate to value, else check if (index) value equals candidate to add 1
"""
