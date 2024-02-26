class Solution(object):
    def hIndex(self, citations):

        def shell_sort(array, k_arr):
            for k in k_arr:
                for i in range(k, len(array)):
                    j = i
                    while j - k >= 0 and array[j - k] < array[j]:
                        array[j - k], array[j] = array[j], array[j - k]
                        j -= k
        
            return array

        def h_index(citations, k_arr):
            shell_sort(citations, k_arr)
            
            for i, value in enumerate(citations):
                if i + 1 > value:
                    return i
            return len(citations)
        
        n = len(citations)
        k_arr = [2**i - 1 for i in range(n.bit_length() - 1, -1, -1) if 2**i - 1 <= n]
        print(k_arr)

        return h_index(citations, k_arr)

solution = Solution()
citations = [3,0,1,6,5]
result = solution.hIndex(citations)
print(result)