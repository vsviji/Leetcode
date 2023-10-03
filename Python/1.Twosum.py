class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
        # If no pair is found, return an empty list.
        return []

# Create an instance of the Solution class
a = Solution()

# Call the twoSum method with a list and target value
result = a.twoSum([3, 4, 9, 6, 4], 8)

# Print the result (indices of the pair that sums up to the target)
print(result)

'''
Output
[1,4]
'''
