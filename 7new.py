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
        
        def merge_sort_with_buffer(arr, left, right, buffer_left):
            if right - left - 1 == 0:
                arr[left], arr[buffer_left] = arr[buffer_left], arr[left]
                return
            
            under_mid = (left + right) // 2
            over_mid = (left + right + 1) // 2
                
            merge_sort_with_buffer(arr, left, under_mid, over_mid)
            merge_sort(arr, left, over_mid)
            merge(arr, left, over_mid, over_mid, right, buffer_left)
    
        def merge_sort(arr, left = None, right = None):
            if left == None and right == None:
                left = 0
                right = len(arr)
            
            if right - left - 1 == 0:
                return
        
            under_mid = (left + right) // 2
            over_mid = (left + right + 1) // 2    
            merge_sort_with_buffer(arr, left, under_mid, over_mid)
        
            while over_mid - left - 1 > 0:
                new_right = over_mid
                under_mid = (left + over_mid) // 2
                over_mid = (left + over_mid + 1) // 2
                merge_sort_with_buffer(arr, over_mid, new_right, left)
                merge(arr, left, under_mid, new_right, right, over_mid)
            
            left += 1 
            while left < right and arr[left - 1]> arr[left]:
                arr[left - 1], arr[left] = arr[left], arr[left - 1]
                left += 1

        merge_sort(nums)
        return nums

s = Solution()
arr =  [-4,0,7,4,9,-5,-1,0,-7,-1]
print(s.sortArray(arr))