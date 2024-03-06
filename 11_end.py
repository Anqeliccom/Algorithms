class Solution(object):
    def sortColors(self, nums):
        def flag_sort(nums):
            left, right = 0, len(nums) - 1
        
            i = 0
            while i <= right:
                if nums[i] == 0:
                    nums[i], nums[left] = nums[left], nums[i]
                    left += 1
                    i += 1
                elif nums[i] == 2:
                    nums[i], nums[right] = nums[right], nums[i]
                    right -= 1
                else:
                    i += 1

        flag_sort(nums)
        return nums

solution = Solution()
nums = [2, 0, 2, 1, 1, 0]
sorted_nums = solution.sortColors(nums)
print(sorted_nums)
