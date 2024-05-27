class Solution(object):
    def thirdMax(self, nums):
        nums = list(set(nums))
        if not nums:
            return None
        n = len(nums)
        if n >= 3:
            nums.sort()
            x = nums[-3]
        else:
            x = nums[-1]
        return x
# Soln = Solution()
# result = Soln.thirdMax(nums)
# print(result)