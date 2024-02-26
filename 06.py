class Solution(object):
    def wiggleSort(self, nums):
        def merge_sort(nums):
            # сортируем с помощью merge sort
            if len(nums) > 1:
                mid = len(nums) // 2
                left_half = nums[:mid]
                right_half = nums[mid:]

                merge_sort(left_half)
                merge_sort(right_half)

                i, j, k = 0, 0, 0

                while i < len(left_half) and j < len(right_half):
                    if left_half[i] < right_half[j]:
                        nums[k] = left_half[i]
                        i += 1
                    else:
                        nums[k] = right_half[j]
                        j += 1
                    k += 1

                while i < len(left_half):
                    nums[k] = left_half[i]
                    i += 1
                    k += 1

                while j < len(right_half):
                    nums[k] = right_half[j]
                    j += 1
                    k += 1
        
        def wiggle_sort(array):
            merge_sort(array)
            sr = len(array) // 2
            if len(array) % 2 != 0:
                sr += 1
            array[::2], array[1::2] = array[:sr][::-1], array[sr:][::-1]

        wiggle_sort(nums)

solution = Solution()
nums = [1, 5, 1, 1, 6, 4]
solution.wiggleSort(nums)
print(nums)
