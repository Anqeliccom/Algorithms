class Solution(object):
    def isIdealPermutation(self, nums):
        n = len(nums)
        global_inversions = 0
        local_inversions = 0

        for i in range(n):
            if nums[i] > i: # список неостортирован, элемент не на своем месте, а значит был хотя бы один больший до него
                global_inversions += nums[i] - i
            
            if abs(nums[i] - i) > 1:
                return False  # Если разница больше 1, это не "идеальная" перестановка, 

            if i < n - 1 and nums[i] > nums[i + 1]:
                local_inversions += 1

        return global_inversions == local_inversions

s = Solution()
nums1 = [1, 0, 2]
print(s.isIdealPermutation(nums1))  # Вывод: True

nums2 = [1, 2, 0]
print(s.isIdealPermutation(nums2))  # Вывод: False

nums3 = [2, 1, 0]
print(s.isIdealPermutation(nums3))  # Вывод: False
