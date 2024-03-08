from random import randint

class Solution:
    def Calc_sentr_stat(self, nums):
        def hoare_partition(arr, pivot_index):
            pivot = arr[pivot_index]
            i, j = 0, len(arr) - 1
            while True:
                # если текущий равен пивоту и находится левее него или правее, то не обмениваем, чтобы сохранить позицию
                while arr[i] < pivot or (arr[i] == pivot and i < pivot_index):  
                    i += 1
                while arr[j] > pivot or (arr[j] == pivot and j > pivot_index):
                    j -= 1
                if i >= j:
                    return j
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        def kth(array, k):
            if len(array) == 1:
                return array[0]
                
            pivot_index = randint(0, len(array) - 1)
            p = hoare_partition(array, pivot_index)

            if p == k:
                return array[p]
            elif p > k:
                return kth(array[:p], k)
            else:
                return kth(array[p + 1:], k - p - 1)
        
        def central_statistics(arr):
            arr_y = [i[1] for i in arr]
            return kth(arr_y, len(arr_y) // 2)
        
        return central_statistics(nums)

solution = Solution()
arr = [[7,1], [5, 2], [6, 3], [3, 1], [1, 2]]
sorted_arr = solution.Calc_sentr_stat(arr)
print(sorted_arr)
