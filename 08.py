class Solution(object):
    def isIdealPermutation(self, nums):
        local_inversions = sum([1 for i in range(len(nums) - 1) if nums[i] > nums[i + 1]])

        def merge_and_count_split(left, right, res):
            lsize, rsize = len(left), len(right)
            n = len(res)

            i, j, k = 0, 0, 0

            split_count = 0

            while k < n and i < lsize and j < rsize:
                if left[i] <= right[j]:
                    res[k] = left[i]
                    k += 1
                    i += 1
                else:
                    res[k] = right[j]
                    k += 1
                    j += 1
                    split_count += lsize - i

            while i < lsize:
                res[k] = left[i]
                k += 1
                i += 1

            while j < rsize:
                res[k] = right[j]
                k += 1
                j += 1

            return split_count, res

        def sort_and_count_inversions(array):
            if len(array) == 1:
                return 0, array

            middle = len(array) // 2

            left_count, left = sort_and_count_inversions(array[:middle])
            right_count, right = sort_and_count_inversions(array[middle:])

            buffer = [0] * len(array)

            split, result = merge_and_count_split(left, right, buffer)

            for i in range(len(array)):
                array[i] = result[i]

            return left_count + right_count + split, array

        global_inversions, _ = sort_and_count_inversions(nums)
        return global_inversions == local_inversions

s = Solution()
nums1 = [1, 0, 2]
print(s.isIdealPermutation(nums1))  # Output: True

nums2 = [1, 2, 0]
print(s.isIdealPermutation(nums2))  # Output: False
