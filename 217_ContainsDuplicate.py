class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        values_set = set()

        for value in nums:
            if value not in values_set:
                values_set.add(value)
            else:
                return True
        
        return False



"""

Create value set. If value not in set add, else return True (means there is already one)

"""
