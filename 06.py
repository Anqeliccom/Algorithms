class Solution(object):
    def wiggleSort(self, nums):

        def selection_sort(array):
            # сортировка выбором
            for i in range(len(array)):
                min_index = i
                for j in range(i + 1, len(array)):
                    if array[min_index] > array[j]:
                        min_index = j
                array[i], array[min_index] = array[min_index], array[i]

            # расставляем элементы
            sr = len(array) // 2
            array[::2], array[1::2] = array[:sr][::-1], array[sr:][::-1]

        selection_sort(nums)

solution = Solution()
nums = [1, 5, 1, 1, 6, 4]
solution.wiggleSort(nums)
print(nums)