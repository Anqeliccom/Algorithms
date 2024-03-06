import random

class Solution:
    def sortArray(self, nums):
        def lomuto_partition(arr, left, right):

            pivot_index = random.randint(left, right)
            pivot = arr[pivot_index]
            arr[pivot_index], arr[left] = arr[left], arr[pivot_index]
            l, h, c = left, left, left + 1

            while c <= right:
                if arr[c] < pivot:
                    tmp = arr[c]
                    arr[c], arr[h + 1] = arr[h + 1], arr[l]
                    arr[l] = tmp
                    l += 1
                    h += 1
                    c += 1
                elif arr[c] == pivot:
                    arr[h + 1], arr[c] = arr[c], arr[h + 1]
                    h += 1 
                    c += 1
                else:
                    c += 1

            return l, h

        def lomuto_quicksort(arr, left, right):
            if left < right:
                l, h = lomuto_partition(arr, left, right)
                lomuto_quicksort(arr, left, l - 1)
                lomuto_quicksort(arr, h + 1, right)

        lomuto_quicksort(nums, 0, len(nums) - 1)
        return nums

solution = Solution()
arr = [5, 1, 1, 2, 0, 0]
sorted_arr = solution.sortArray(arr)
print(sorted_arr)
