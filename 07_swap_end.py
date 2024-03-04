
class Solution:
    def sortArray(self, nums):
        def merge(arr, start1, end1, start2, end2, output):
            left, right, merged_index = start1, start2, output
        
            while left < end1 and right < end2:
                if arr[left] <= arr[right]:
                    arr[merged_index], arr[left] = arr[left], arr[merged_index]
                    left += 1
                else:
                    arr[merged_index], arr[right] = arr[right], arr[merged_index]
                    right += 1
                merged_index += 1
        
            while left < end1:
                arr[merged_index], arr[left] = arr[left], arr[merged_index]
                left += 1
                merged_index += 1
        
            while right < end2:
                arr[merged_index], arr[right] = arr[right], arr[merged_index]
                right += 1
                merged_index += 1
        
            return
        
        
        def merge_sort_with_buffer(arr, left, right, buffer):
            if right - left - 1 > 0:
                mid = (left + right) // 2
                
                merge_sort_with_buffer(arr, left, mid, buffer)
                merge_sort_with_buffer(arr, mid, right, buffer)
                
                merge(arr, left, mid, mid, right, buffer)
                
                for i in range(0, right - left):
                    arr[i + left], arr[i + buffer] = arr[i + buffer], arr[i + left]
        
        
        def merge_sort_not_buffer(arr, left, right):
            if right - left - 1 > 0:
                under_mid = (left + right) // 2
                over_mid = (left + right + 1) // 2
                     
                merge_sort_with_buffer(arr, left, under_mid, under_mid)
                merge(arr, left, under_mid, right, len(arr), over_mid)
                
                merge_sort_not_buffer(arr, left, over_mid)
                
        
        def in_place_merge_sort(arr):
            if len(arr) <= 1:
                return
            mid = (len(arr) // 2) + 1
            
            merge_sort_with_buffer(arr, mid, len(arr), 0)
            merge_sort_not_buffer(arr, 0, mid)
            i = 1
            while i <len(arr) and arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i- 1]
                i+=1
            return arr

        in_place_merge_sort(nums)
        return nums

s = Solution()
arr =  [-4,0,7,4,9,-5,-1,0,-7,-1]
print(s.sortArray(arr))
