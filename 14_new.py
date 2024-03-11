from random import randint

class Solution:
    def Calc_sentr_stat(self, nums):
        def lomuto_partition(arr, pivot_index):
            pivot = arr[pivot_index]
            arr[pivot_index], arr[0] = arr[0], arr[pivot_index]
            l, h, c = 0, 0, 0 + 1

            while c <= (len(arr) - 1):
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

        def kth(array, k):
            if len(array) == 1:
                return array[0]
                
            pivot_index = randint(0, len(array) - 1)
            l, _ = lomuto_partition(array, pivot_index)
            
            if l == k:
                return array[l]
            elif l > k:
                return kth(array[:l], k)
            else:
                return kth(array[l + 1:], k - l - 1)
        
        def central_statistics(arr):
            arr_y = [i[1] for i in arr]
            return kth(arr_y, len(arr_y) // 2)
        
        return central_statistics(nums)

solution = Solution()
arr = [[7,1], [5, 2], [6, 3], [3, 1], [1, 2], [4,1]]
sorted_arr = solution.Calc_sentr_stat(arr)
print(sorted_arr)

