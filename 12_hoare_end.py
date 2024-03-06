import random

class Solution:
    def sortArray(self, nums):
        def hoare_partition(arr, left, right):

            pivot_index = random.randint(left, right)
            pivot = arr[pivot_index]
        
            i, j = left, right
        
            while True:
                while arr[i] < pivot:
                    i += 1
                while arr[j] > pivot:
                    j -= 1
                if i >= j:
                    return j
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        
        def hoare_quicksort(arr, left, right):
            if left < right:
                k = hoare_partition(arr, left, right)
                hoare_quicksort(arr, left, k)
                hoare_quicksort(arr, k + 1, right)
                
        hoare_quicksort(nums, 0, len(nums) - 1)
        return nums

solution = Solution()
arr = [2,5,3,4,1,33,2,12]
sorted_arr = solution.sortArray(arr)
print(sorted_arr)
