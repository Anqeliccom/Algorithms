def counting_sort(arr_of_strings, index):
    
    K = max(ord(s[index]) for s in arr_of_strings) + 1

    C = [0] * K
    R = ["" for _ in range(len(arr_of_strings))]

    for s in arr_of_strings:
        C[ord(s[index])] += 1

    for i in range(1, K):
        C[i] += C[i - 1]

    for i in range(len(arr_of_strings) - 1, -1, -1):
        char_index = ord(arr_of_strings[i][index])
        R[C[char_index] - 1] = arr_of_strings[i]
        C[char_index] -= 1

    return R

def lsd_radix_sort(arr_of_strings):

    for i in range(len(arr_of_strings[0]) - 1, -1, -1):
        arr_of_strings = counting_sort(arr_of_strings, i)

    return arr_of_strings


arr = ["abc", "bac", "cab", "hig", "fed", "pol"]
    
# сортируем с использованием поразрядной сортировки
sorted_res = lsd_radix_sort(arr)
    
# cортируем с помощью сортировки, использующей сравнение
expected_res = sorted(arr)

assert sorted_res == expected_res

print("Тест успешно пройден")
