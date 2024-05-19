# # import time
# # import copy
# # import math
# # import random

# # def generate_matrix(size):
# #     return [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]

# # def multiply_classic(A, B):
# #     res = [[0] * len(B[0]) for _ in range(len(A))]
    
# #     for i in range(len(A)):
# #         for j in range(len(B[0])):
# #             for k in range(len(B)):
# #                 res[i][j] += A[i][k] * B[k][j]
                
# #     return res
    
# # def multiply_recursive(A, B):
# #     def degree_2(size):
# #         n = 1
# #         while n < size:
# #             n = n * 2
# #         return n
    
# #     def size_x_size(E, size):
# #         res = [[0] * size for _ in range(size)]
# #         for i in range(len(E)):
# #             for j in range(len(E[0])):
# #                 res[i][j] = E[i][j]
# #         return res
    
# #     def recursive_calls_helper(X, Y):
    
# #         def split_matrices(E):
# #             n = len(E)
# #             n2 = n // 2
# #             A = [E[i][:n2] for i in range(0, n2)]
# #             B = [E[i][n2:] for i in range(0, n2)]
# #             C = [E[i][:n2] for i in range(n2, n)]
# #             D = [E[i][n2:] for i in range(n2, n)]
# #             return A, B, C, D
    
# #         def plus_matrices(A, B, result, start_row, start_col):
# #             for i in range(len(A)):
# #                 for j in range(len(A[0])):
# #                     result[start_row + i][start_col + j] = A[i][j] + B[i][j]
# #             return result
    
# #         rows_X, cols_X = len(X), len(X[0])
# #         rows_Y, cols_Y = len(Y), len(Y[0])
    
# #         if rows_X == 1:
# #             return [[X[0][0] * Y[0][0]]]
# #         else:
# #             A, B, C, D = split_matrices(X)
# #             E, F, G, H = split_matrices(Y)
        
# #             P1 = recursive_calls_helper(A, E)
# #             P2 = recursive_calls_helper(B, G)
# #             P3 = recursive_calls_helper(A, F)
# #             P4 = recursive_calls_helper(B, H)
# #             P5 = recursive_calls_helper(C, E)
# #             P6 = recursive_calls_helper(D, G)
# #             P7 = recursive_calls_helper(C, F)
# #             P8 = recursive_calls_helper(D, H)
        
# #             res = [[0] * cols_Y for _ in range(rows_X)]
            
# #             n2 = len(X) // 2
        
# #             plus_matrices(P1, P2, res, 0, 0)
# #             plus_matrices(P3, P4, res, 0, n2)
# #             plus_matrices(P5, P6, res, n2, 0)
# #             plus_matrices(P7, P8, res, n2, n2)
        
# #             return res
    
# #     def recursive_calls(X, Y):
# #         rows = len(X)
# #         cols = len(Y[0])
# #         size_square_matrix = degree_2(max(len(X), len(X[0]), len(Y), len(Y[0]))) # определим размер ближайшей квадратной матрицы, в которую вписана исходная
# #         X = size_x_size(X, size_square_matrix) # заполняем нулями достроенные ячейки
# #         Y = size_x_size(Y, size_square_matrix)
# #         result_matrix = recursive_calls_helper(X, Y) # работаем по алгоритму как с квадратной
    
# #         result_matrix = [result_matrix[i][:cols] for i in range(rows)] # возвращаем исходный размер

# #         return result_matrix
# #     res = recursive_calls(X,Y)
# #     return res
    
# # def multiply_strassen(A, B):
# #     def degree_2(size):
# #         n = 1
# #         while n < size:
# #             n = n * 2
# #         return n
    
# #     def size_x_size(E, size):
# #         res = [[0] * size for _ in range(size)]
# #         for i in range(len(E)):
# #             for j in range(len(E[0])):
# #                 res[i][j] = E[i][j]
# #         return res
    
# #     def add_matrix(A, B, start_row=0, start_col=0):
# #         result = copy.deepcopy(A)
# #         for i in range(len(B)):
# #             for j in range(len(B[0])):
# #                 result[start_row + i][start_col + j] += B[i][j]
# #         return result
    
    
# #     def shtrasen_helper(X, Y):
        
# #         def split_matrices(E):
# #             n = len(E)
# #             n2 = n // 2
# #             A = [E[i][:n2] for i in range(0, n2)]
# #             B = [E[i][n2:] for i in range(0, n2)]
# #             C = [E[i][:n2] for i in range(n2, n)]
# #             D = [E[i][n2:] for i in range(n2, n)]
# #             return A, B, C, D
            
# #         def plus_matrices(A, B):
# #             return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    
# #         def minus_matrices(A, B):
# #             return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
        
# #         n = len(X)
    
# #         if n == 1:
# #             return [[X[0][0] * Y[0][0]]]
# #         else:
# #             A, B, C, D = split_matrices(X)
# #             E, F, G, H = split_matrices(Y)
            
# #             P1 = shtrasen_helper(A, minus_matrices(F, H))
# #             P2 = shtrasen_helper(plus_matrices(A, B), H)
# #             P3 = shtrasen_helper(plus_matrices(C, D), E)
# #             P4 = shtrasen_helper(D, minus_matrices(G, E))
# #             P5 = shtrasen_helper(plus_matrices(A, D), plus_matrices(E, H))
# #             P6 = shtrasen_helper(minus_matrices(B, D), plus_matrices(G, H))
# #             P7 = shtrasen_helper(minus_matrices(A, C), plus_matrices(E, F))
    
# #             Q1 = plus_matrices(minus_matrices(plus_matrices(P5, P4), P2), P6)
# #             Q2 = plus_matrices(P1, P2)
# #             Q3 = plus_matrices(P3, P4)
# #             Q4 = minus_matrices(minus_matrices(plus_matrices(P5, P1), P3), P7)
    
# #             result = [[0 for _ in range(n)] for _ in range(n)]
            
# #             result = add_matrix(result, Q1, 0, 0)
# #             result = add_matrix(result, Q2, 0, n//2)
# #             result = add_matrix(result, Q3, n//2, 0)
# #             result = add_matrix(result, Q4, n//2, n//2)
    
# #             return result
    
# #     def shtrasen(X, Y):
# #         rows_X, cols_X = len(X), len(X[0])
# #         rows_Y, cols_Y = len(Y), len(Y[0])
        
# #         size_square_matrix = degree_2(max(len(X), len(X[0]), len(Y), len(Y[0])))
# #         X = size_x_size(X, size_square_matrix)
# #         Y = size_x_size(Y, size_square_matrix)
    
# #         result_matrix = shtrasen_helper(X, Y)
    
# #         result_matrix = [result_matrix[i][:cols_Y] for i in range(rows_X)]
    
# #         return result_matrix
# #     res = shtrasen(X,Y)
# #     return res

# # def calculate_time(algorithm, size):
# #     matrix1 = generate_matrix(size)
# #     matrix2 = generate_matrix(size)
# #     start_time = time.time()
# #     algorithm(matrix1, matrix2)
# #     return time.time() - start_time

# # def format_table(benchmarks, algos, results):
# #     num_benchmarks = len(benchmarks)
# #     num_algos = len(algos)
# #     max_benchmark_len = max(len(b) for b in benchmarks)
# #     max_result_lens = [max(len(str(results[i][j])) for i in range(num_benchmarks)) for j in range(num_algos)]
# #     max_space_between_algos_results = [max(max_result_lens[i], len(algo)) for i, algo in enumerate(algos)]
# #     max_space_between_benchmark_title = max(max_benchmark_len, 9)

# #     header = f"| Benchmark{' ' * (max_benchmark_len - 9)} |"
# #     for algo, max_len in zip(algos, max_space_between_algos_results):
# #         header += f" {algo}{' ' * (max_len - len(algo))} |"
# #     print(header)
# #     header_line = f"|{'-' * (max_space_between_benchmark_title + 2)}|"
# #     for max_len in max_space_between_algos_results:
# #         header_line += f"{'-' * (max_len + 2)}|"
# #     print(header_line)
    
# #     for i in range(num_benchmarks):
# #         benchmark = benchmarks[i]
# #         row = f"| {benchmark}{' ' * (max_space_between_benchmark_title - len(benchmark))} |"
# #         for j in range(num_algos):
# #             row += f" {results[i][j]}{' ' * (max_space_between_algos_results[j] - len(str(results[i][j])))} |"
# #         print(row)

# # benchmarks = ["sample mean", "standard deviation", "geometric mean"]
# # algos = ["trivial", "recursive_8", "strassen"]
# # results = []

# # # Размеры матриц, степени двойки до 256
# # matrix_sizes = [2 ** i for i in range(1, 9)]

# # for size in matrix_sizes:
# #     row_results = []
# #     for algo in [multiply_classic, multiply_recursive, multiply_strassen]:
# #         row_results.append(calculate_time(algo, size))
# #     results.append(row_results)

# # format_table(benchmarks, algos, results)

# # def calculate_val(algorithm, X, Y):
# #     z1 = measure_time(algorithm, X, Y)
# #     z2 = measure_time(algorithm, X, Y)
# #     z3 = measure_time(algorithm, X, Y)
# #     z4 = measure_time(algorithm, X, Y)
# #     val = [z1, z2, z3, z4]
# #     return val

# # def measure_time(algorithm, X, Y):
# #     start_time = time.time()
# #     algorithm(X, Y)
# #     return time.time() - start_time
    
# # def calculate_sample_mean(val):
# #     return sum(val) / len(val)

# # def calculate_standard_deviation(val):
# #     mean = calculate_sample_mean(val)
# #     variance = sum((x - mean) ** 2 for x in val) / len(val)
# #     return math.sqrt(variance)

# # def calculate_geometric_mean(val):
# #     k = 1
# #     for x in val:
# #         k *= x
# #     return k ** (1 / len(val))
    
# # if name == "main":
# #     benchmarks = ["Time", "Sample mean", "Standard deviation"]
# #     algos = ["Classic", "Recursive", "Strassen"]
# #     results = []

# #     # Генерация матриц различных размеров и вычисление времени для каждого алгоритма
# #     for size in [2 ** i for i in range(1, 9)]:
# #         X = generate_matrix(size)
# #         Y = generate_matrix(size)
# #         row_results = []

# #         for algo in [multiply_classic, multiply_recursive, multiply_strassen]:
# #             times = [measure_time(algo, X, Y) for _ in range(4)]  # Замер времени несколько раз для усреднения
# #             sample_mean, standard_deviation = calculate_statistics(times)
# #             row_results.append(sample_mean)

# #         results.append(row_results)

# #     # Вывод результатов
# #     format_table(benchmarks, algos, results)


# import time
# import copy
# import math
# import random

# def generate_random_matrix(rows, cols):
#     return [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]

# def generate_power_of_two_matrices(max_power):
#     matrices = []
#     for power in range(1, max_power + 1):
#         size = 2 ** power
#         matrix_X = generate_random_matrix(size, size)
#         matrix_Y = generate_random_matrix(size, size)
#         matrices.append((matrix_X, matrix_Y))
#     return matrices

# def measure_and_calculate_results(algorithm, matrices):
#     results = []
#     for X, Y in matrices:
#         row_results = []
#         row_results.append(measure_time(algorithm, X, Y))
#         row_results.append(calculate_sample_mean(calculate_val(algorithm, X, Y)))
#         row_results.append(calculate_standard_deviation(calculate_val(algorithm, X, Y)))
#         row_results.append(calculate_geometric_mean(calculate_val(algorithm, X, Y)))
#         results.append(row_results)
#     return results

# def format_table(benchmarks, algos, results):
#     num_benchmarks = len(benchmarks)
#     num_algos = len(algos)
    
#     max_benchmark_len = max(len(b) for b in benchmarks)
#     max_result_lens = [max(len(str(results[i][j])) for i in range(len(results))) for j in range(num_algos)]
    
#     max_space_between_algos_results = [max(max_result_lens[i], len(algo)) for i, algo in enumerate(algos)]
#     max_space_between_benchmark_title = max(max_benchmark_len, 9)

#     header = f"| Benchmark{' ' * (max_benchmark_len - 9)} |"
#     for algo, max_len in zip(algos, max_space_between_algos_results):
#         header += f" {algo}{' ' * (max_len - len(algo))} |"
#     print(header)
    
#     header_line = f"|{'-' * (max_space_between_benchmark_title + 2)}|"
#     for max_len in max_space_between_algos_results:
#         header_line += f"{'-' * (max_len + 2)}|"
#     print(header_line)
    
#     for i in range(num_benchmarks):
#         benchmark = benchmarks[i]
#         row = f"| {benchmark}{' ' * (max_space_between_benchmark_title - len(benchmark))} |"
#         for j in range(num_algos):
#             row += f" {results[i][j]}{' ' * (max_space_between_algos_results[j] - len(str(results[i][j])))} |"
#         print(row)

# def calculate_val(algorithm, X, Y):
#     z1 = measure_time(algorithm, X, Y)
#     z2 = measure_time(algorithm, X, Y)
#     z3 = measure_time(algorithm, X, Y)
#     z4 = measure_time(algorithm, X, Y)
#     val = [z1, z2, z3, z4]
#     return val

# def measure_time(algorithm, X, Y):
#     start_time = time.time()
#     algorithm(X, Y)
#     return time.time() - start_time
    
# def calculate_sample_mean(val):
#     return sum(val) / len(val)

# def calculate_standard_deviation(val):
#     mean = calculate_sample_mean(val)
#     variance = sum((x - mean) ** 2 for x in val) / len(val)
#     return math.sqrt(variance)

# def calculate_geometric_mean(val):
#     k = 1
#     for x in val:
#         k *= x
#     return k ** (1 / len(val))
    
# def multiply_classic(A, B):
#     res = [[0] * len(B[0]) for _ in range(len(A))]
    
#     for i in range(len(A)):
#         for j in range(len(B[0])):
#             for k in range(len(B)):
#                 res[i][j] += A[i][k] * B[k][j]
                
#     return res
    
# def multiply_recursive(A, B):
#     def degree_2(size):
#         n = 1
#         while n < size:
#             n = n * 2
#         return n
    
#     def size_x_size(E, size):
#         res = [[0] * size for _ in range(size)]
#         for i in range(len(E)):
#             for j in range(len(E[0])):
#                 res[i][j] = E[i][j]
#         return res
    
#     def recursive_calls_helper(X, Y):
    
#         def split_matrices(E):
#             n = len(E)
#             n2 = n // 2
#             A = [E[i][:n2] for i in range(0, n2)]
#             B = [E[i][n2:] for i in range(0, n2)]
#             C = [E[i][:n2] for i in range(n2, n)]
#             D = [E[i][n2:] for i in range(n2, n)]
#             return A, B, C, D
    
#         def plus_matrices(A, B, result, start_row, start_col):
#             for i in range(len(A)):
#                 for j in range(len(A[0])):
#                     result[start_row + i][start_col + j] = A[i][j] + B[i][j]
#             return result
    
#         rows_X, cols_X = len(X), len(X[0])
#         rows_Y, cols_Y = len(Y), len(Y[0])
    
#         if rows_X == 1:
#             return [[X[0][0] * Y[0][0]]]
#         else:
#             A, B, C, D = split_matrices(X)
#             E, F, G, H = split_matrices(Y)
        
#             P1 = recursive_calls_helper(A, E)
#             P2 = recursive_calls_helper(B, G)
#             P3 = recursive_calls_helper(A, F)
#             P4 = recursive_calls_helper(B, H)
#             P5 = recursive_calls_helper(C, E)
#             P6 = recursive_calls_helper(D, G)
#             P7 = recursive_calls_helper(C, F)
#             P8 = recursive_calls_helper(D, H)
        
#             res = [[0] * cols_Y for _ in range(rows_X)]
            
#             n2 = len(X) // 2
        
#             plus_matrices(P1, P2, res, 0, 0)
#             plus_matrices(P3, P4, res, 0, n2)
#             plus_matrices(P5, P6, res, n2, 0)
#             plus_matrices(P7, P8, res, n2, n2)
        
#             return res
    
#     def recursive_calls(X, Y):
#         rows = len(X)
#         cols = len(Y[0])
#         size_square_matrix = degree_2(max(len(X), len(X[0]), len(Y), len(Y[0]))) # определим размер ближайшей квадратной матрицы, в которую вписана исходная
#         X = size_x_size(X, size_square_matrix) # заполняем нулями достроенные ячейки
#         Y = size_x_size(Y, size_square_matrix)
#         result_matrix = recursive_calls_helper(X, Y) # работаем по алгоритму как с квадратной
    
#         result_matrix = [result_matrix[i][:cols] for i in range(rows)] # возвращаем исходный размер

#         return result_matrix
#     res = recursive_calls(X,Y)
#     return res
    
# def multiply_strassen(A, B):
#     def degree_2(size):
#         n = 1
#         while n < size:
#             n = n * 2
#         return n
    
#     def size_x_size(E, size):
#         res = [[0] * size for _ in range(size)]
#         for i in range(len(E)):
#             for j in range(len(E[0])):
#                 res[i][j] = E[i][j]
#         return res
    
#     def add_matrix(A, B, start_row=0, start_col=0):
#         result = copy.deepcopy(A)
#         for i in range(len(B)):
#             for j in range(len(B[0])):
#                 result[start_row + i][start_col + j] += B[i][j]
#         return result
    
    
#     def shtrasen_helper(X, Y):
        
#         def split_matrices(E):
#             n = len(E)
#             n2 = n // 2
#             A = [E[i][:n2] for i in range(0, n2)]
#             B = [E[i][n2:] for i in range(0, n2)]
#             C = [E[i][:n2] for i in range(n2, n)]
#             D = [E[i][n2:] for i in range(n2, n)]
#             return A, B, C, D
            
#         def plus_matrices(A, B):
#             return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    
#         def minus_matrices(A, B):
#             return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
        
#         n = len(X)
    
#         if n == 1:
#             return [[X[0][0] * Y[0][0]]]
#         else:
#             A, B, C, D = split_matrices(X)
#             E, F, G, H = split_matrices(Y)
            
#             P1 = shtrasen_helper(A, minus_matrices(F, H))
#             P2 = shtrasen_helper(plus_matrices(A, B), H)
#             P3 = shtrasen_helper(plus_matrices(C, D), E)
#             P4 = shtrasen_helper(D, minus_matrices(G, E))
#             P5 = shtrasen_helper(plus_matrices(A, D), plus_matrices(E, H))
#             P6 = shtrasen_helper(minus_matrices(B, D), plus_matrices(G, H))
#             P7 = shtrasen_helper(minus_matrices(A, C), plus_matrices(E, F))
    
#             Q1 = plus_matrices(minus_matrices(plus_matrices(P5, P4), P2), P6)
#             Q2 = plus_matrices(P1, P2)
#             Q3 = plus_matrices(P3, P4)
#             Q4 = minus_matrices(minus_matrices(plus_matrices(P5, P1), P3), P7)
    
#             result = [[0 for _ in range(n)] for _ in range(n)]
            
#             result = add_matrix(result, Q1, 0, 0)
#             result = add_matrix(result, Q2, 0, n//2)
#             result = add_matrix(result, Q3, n//2, 0)
#             result = add_matrix(result, Q4, n//2, n//2)
    
#             return result
    
#     def shtrasen(X, Y):
#         rows_X, cols_X = len(X), len(X[0])
#         rows_Y, cols_Y = len(Y), len(Y[0])
        
#         size_square_matrix = degree_2(max(len(X), len(X[0]), len(Y), len(Y[0])))
#         X = size_x_size(X, size_square_matrix)
#         Y = size_x_size(Y, size_square_matrix)
    
#         result_matrix = shtrasen_helper(X, Y)
    
#         result_matrix = [result_matrix[i][:cols_Y] for i in range(rows_X)]
    
#         return result_matrix
#     res = shtrasen(X,Y)
#     return res
    
# benchmarks = ["Time", "Sample mean", "Standard deviation", "Geometric mean"]
# algos = ["Classic", "Recursive", "Strassen"]

# matrices = generate_power_of_two_matrices(3)

# results_classic = measure_and_calculate_results(multiply_classic, matrices)
# results_recursive = measure_and_calculate_results(multiply_recursive, matrices)
# results_strassen = measure_and_calculate_results(multiply_strassen, matrices)

# format_table(benchmarks, algos, results_classic)
# format_table(benchmarks, algos, results_recursive)
# format_table(benchmarks, algos, results_strassen)



import time
import copy
import math

def multiply_classic(A, B):
    res = [[0] * len(B[0]) for _ in range(len(A))]
    
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                res[i][j] += A[i][k] * B[k][j]
                
    return res
    
def multiply_recursive(A, B):
    def degree_2(size):
        n = 1
        while n < size:
            n = n * 2
        return n
    
    def size_x_size(E, size):
        res = [[0] * size for _ in range(size)]
        for i in range(len(E)):
            for j in range(len(E[0])):
                res[i][j] = E[i][j]
        return res
    
    def recursive_calls_helper(X, Y):
    
        def split_matrices(E):
            n = len(E)
            n2 = n // 2
            A = [E[i][:n2] for i in range(0, n2)]
            B = [E[i][n2:] for i in range(0, n2)]
            C = [E[i][:n2] for i in range(n2, n)]
            D = [E[i][n2:] for i in range(n2, n)]
            return A, B, C, D
    
        def plus_matrices(A, B, result, start_row, start_col):
            for i in range(len(A)):
                for j in range(len(A[0])):
                    result[start_row + i][start_col + j] = A[i][j] + B[i][j]
            return result
    
        rows_X, cols_X = len(X), len(X[0])
        rows_Y, cols_Y = len(Y), len(Y[0])
    
        if rows_X == 1:
            return [[X[0][0] * Y[0][0]]]
        else:
            A, B, C, D = split_matrices(X)
            E, F, G, H = split_matrices(Y)
        
            P1 = recursive_calls_helper(A, E)
            P2 = recursive_calls_helper(B, G)
            P3 = recursive_calls_helper(A, F)
            P4 = recursive_calls_helper(B, H)
            P5 = recursive_calls_helper(C, E)
            P6 = recursive_calls_helper(D, G)
            P7 = recursive_calls_helper(C, F)
            P8 = recursive_calls_helper(D, H)
        
            res = [[0] * cols_Y for _ in range(rows_X)]
            
            n2 = len(X) // 2
        
            plus_matrices(P1, P2, res, 0, 0)
            plus_matrices(P3, P4, res, 0, n2)
            plus_matrices(P5, P6, res, n2, 0)
            plus_matrices(P7, P8, res, n2, n2)
        
            return res
    
    def recursive_calls(X, Y):
        rows = len(X)
        cols = len(Y[0])
        size_square_matrix = degree_2(max(len(X), len(X[0]), len(Y), len(Y[0]))) # определим размер ближайшей квадратной матрицы, в которую вписана исходная
        X = size_x_size(X, size_square_matrix) # заполняем нулями достроенные ячейки
        Y = size_x_size(Y, size_square_matrix)
        result_matrix = recursive_calls_helper(X, Y) # работаем по алгоритму как с квадратной
    
        result_matrix = [result_matrix[i][:cols] for i in range(rows)] # возвращаем исходный размер

        return result_matrix
    res = recursive_calls(X,Y)
    return res
    
def multiply_strassen(A, B, threshold=64):
    def degree_2(size):
        n = 1
        while n < size:
            n = n * 2
        return n
    
    def size_x_size(E, size):
        res = [[0] * size for _ in range(size)]
        for i in range(len(E)):
            for j in range(len(E[0])):
                res[i][j] = E[i][j]
        return res
    
    def add_matrix(A, B, start_row=0, start_col=0):
        result = copy.deepcopy(A)
        for i in range(len(B)):
            for j in range(len(B[0])):
                result[start_row + i][start_col + j] += B[i][j]
        return result
    
    def shtrasen_helper(X, Y):
        def split_matrices(E):
            n = len(E)
            n2 = n // 2
            A = [E[i][:n2] for i in range(0, n2)]
            B = [E[i][n2:] for i in range(0, n2)]
            C = [E[i][:n2] for i in range(n2, n)]
            D = [E[i][n2:] for i in range(n2, n)]
            return A, B, C, D
            
        def plus_matrices(A, B):
            return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    
        def minus_matrices(A, B):
            return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
        
        n = len(X)
    
        if n < threshold:  # используем классическое умножение для матриц малого размера
            return multiply_classic(X, Y)
        
        if n == 1:
            return [[X[0][0] * Y[0][0]]]
        else:
            A, B, C, D = split_matrices(X)
            E, F, G, H = split_matrices(Y)
            
            P1 = shtrasen_helper(A, minus_matrices(F, H))
            P2 = shtrasen_helper(plus_matrices(A, B), H)
            P3 = shtrasen_helper(plus_matrices(C, D), E)
            P4 = shtrasen_helper(D, minus_matrices(G, E))
            P5 = shtrasen_helper(plus_matrices(A, D), plus_matrices(E, H))
            P6 = shtrasen_helper(minus_matrices(B, D), plus_matrices(G, H))
            P7 = shtrasen_helper(minus_matrices(A, C), plus_matrices(E, F))
    
            Q1 = plus_matrices(minus_matrices(plus_matrices(P5, P4), P2), P6)
            Q2 = plus_matrices(P1, P2)
            Q3 = plus_matrices(P3, P4)
            Q4 = minus_matrices(minus_matrices(plus_matrices(P5, P1), P3), P7)
    
            result = [[0 for _ in range(n)] for _ in range(n)]
            
            result = add_matrix(result, Q1, 0, 0)
            result = add_matrix(result, Q2, 0, n // 2)
            result = add_matrix(result, Q3, n // 2, 0)
            result = add_matrix(result, Q4, n // 2, n // 2)
    
            return result
    
    def shtrasen(X, Y):
        rows_X, cols_X = len(X), len(X[0])
        rows_Y, cols_Y = len(Y), len(Y[0])
        
        size_square_matrix = degree_2(max(len(X), len(X[0]), len(Y), len(Y[0])))
        X = size_x_size(X, size_square_matrix)
        Y = size_x_size(Y, size_square_matrix)
    
        result_matrix = shtrasen_helper(X, Y)
    
        result_matrix = [result_matrix[i][:cols_Y] for i in range(rows_X)]
    
        return result_matrix

    res = shtrasen(A, B)
    return res

def format_table(benchmarks, algos, results):
    num_benchmarks = len(benchmarks)
    num_algos = len(algos)
    
    max_benchmark_len = max(len(b) for b in benchmarks)
    max_result_lens = [max(len(str(results[i][j])) for i in range(num_benchmarks)) for j in range(num_algos)]
    
    max_space_between_algos_results = [max(max_result_lens[i], len(algo)) for i, algo in enumerate(algos)]
    max_space_between_benchmark_title = max(max_benchmark_len, 9)


    header = f"| Benchmark{' ' * (max_benchmark_len - 9)} |"
    for algo, max_len in zip(algos, max_space_between_algos_results):
        header += f" {algo}{' ' * (max_len - len(algo))} |"
    print(header)
    
    header_line = f"|{'-' * (max_space_between_benchmark_title + 2)}|"
    for max_len in max_space_between_algos_results:
        header_line += f"{'-' * (max_len + 2)}|"
    print(header_line)
    
    for i in range(num_benchmarks):
        benchmark = benchmarks[i]
        row = f"| {benchmark}{' ' * (max_space_between_benchmark_title - len(benchmark))} |"
        for j in range(num_algos):
            row += f" {results[i][j]}{' ' * (max_space_between_algos_results[j] - len(str(results[i][j])))} |"
        print(row)

def calculate_val(algorithm, X, Y):
    z1 = measure_time(algorithm, X, Y)
    z2 = measure_time(algorithm, X, Y)
    z3 = measure_time(algorithm, X, Y)
    z4 = measure_time(algorithm, X, Y)
    val = [z1, z2, z3, z4]
    return val

def measure_time(algorithm, X, Y):
    start_time = time.time()
    algorithm(X, Y)
    return time.time() - start_time
    
def calculate_sample_mean(val):
    return sum(val) / len(val)

def calculate_standard_deviation(val):
    mean = calculate_sample_mean(val)
    variance = sum((x - mean) ** 2 for x in val) / len(val)
    return math.sqrt(variance)

def calculate_geometric_mean(val):
    k = 1
    for x in val:
        k *= x
    return k ** (1 / len(val))
    
X = [[1, 2, 3, 9, 5, 3, 1, 5, 5, 3, 1, 5, 1, 2, 3, 9, 5, 6, 9, 2, 5, 3, 1, 5, 7, 8, 6, 5, 1, 2, 3, 9, 5, 6, 1, 2, 7, 8, 5, 9, 1, 2, 3, 9, 5, 3, 1, 5, 1, 2, 3, 9, 5, 3, 1, 5, 5, 3, 1, 5, 1, 2, 3, 9, 5, 6, 1, 2, 7, 8, 5, 9, 1, 2, 3, 9, 5, 3, 1, 5, 1, 2, 3, 9, 5, 3, 1, 5, 5, 3, 1, 5, 1, 2, 3, 9, 1, 2, 3, 9, 5, 3, 1, 5, 5, 3, 1, 5, 1, 2, 3, 9, 5, 6, 9, 2, 5, 3, 1, 5, 7, 8, 6, 5, 1, 2, 3, 9], [5, 6, 1, 2, 7, 8, 5, 9, 1, 2, 3, 9, 5, 3, 1, 5, 1, 2, 3, 9, 5, 3, 1, 5, 5, 3, 1, 5, 1, 2, 3, 9, 1, 2, 3, 9, 5, 3, 1, 5, 5, 3, 1, 5, 1, 2, 3, 9, 5, 6, 9, 2, 5, 3, 1, 5, 7, 8, 6, 5, 1, 2, 3, 9, 1, 2, 3, 9, 5, 3, 1, 5, 5, 3, 1, 5, 1, 2, 3, 9, 5, 6, 9, 2, 5, 3, 1, 5, 7, 8, 6, 5, 1, 2, 3, 9, 5, 6, 1, 2, 7, 8, 5, 9, 1, 2, 3, 9, 5, 3, 1, 5, 1, 2, 3, 9, 5, 3, 1, 5, 5, 3, 1, 5, 1, 2, 3, 9], [5, 6, 1, 2, 7, 8, 5, 9, 1, 2, 3, 9, 5, 3, 1, 5, 1, 2, 3, 9, 5, 3, 1, 5, 5, 3, 1, 5, 1, 2, 3, 9, 1, 2, 3, 9, 5, 3, 1, 5, 5, 3, 1, 5, 1, 2, 3, 9, 5, 6, 9, 2, 5, 3, 1, 5, 7, 8, 6, 5, 1, 2, 3, 9, 1, 2, 3, 9, 5, 3, 1, 5, 5, 3, 1, 5, 1, 2, 3, 9, 5, 6, 9, 2, 5, 3, 1, 5, 7, 8, 6, 5, 1, 2, 3, 9, 5, 6, 1, 2, 7, 8, 5, 9, 1, 2, 3, 9, 5, 3, 1, 5, 1, 2, 3, 9, 5, 3, 1, 5, 5, 3, 1, 5, 1, 2, 3, 9], [1, 2, 3, 9, 5, 3, 1, 5, 5, 3, 1, 5, 1, 2, 3, 9, 5, 6, 9, 2, 5, 3, 1, 5, 7, 8, 6, 5, 1, 2, 3, 9, 5, 6, 1, 2, 7, 8, 5, 9, 1, 2, 3, 9, 5, 3, 1, 5, 1, 2, 3, 9, 5, 3, 1, 5, 5, 3, 1, 5, 1, 2, 3, 9, 5, 6, 1, 2, 7, 8, 5, 9, 1, 2, 3, 9, 5, 3, 1, 5, 1, 2, 3, 9, 5, 3, 1, 5, 5, 3, 1, 5, 1, 2, 3, 9, 1, 2, 3, 9, 5, 3, 1, 5, 5, 3, 1, 5, 1, 2, 3, 9, 5, 6, 9, 2, 5, 3, 1, 5, 7, 8, 6, 5, 1, 2, 3, 9]]
Y = [[5, 6, 1, 2, 7, 8, 5, 9, 1, 2, 3, 9, 5, 3, 1, 5, 1, 2, 3, 9, 5, 3, 1, 5, 5, 3, 1, 5, 1, 2, 3, 9, 1, 2, 3, 9, 5, 3, 1, 5, 5, 3, 1, 5, 1, 2, 3, 9, 5, 6, 9, 2, 5, 3, 1, 5, 7, 8, 6, 5, 1, 2, 3, 9, 1, 2, 3, 9, 5, 3, 1, 5, 5, 3, 1, 5, 1, 2, 3, 9, 5, 6, 9, 2, 5, 3, 1, 5, 7, 8, 6, 5, 1, 2, 3, 9, 5, 6, 1, 2, 7, 8, 5, 9, 1, 2, 3, 9, 5, 3, 1, 5, 1, 2, 3, 9, 5, 3, 1, 5, 5, 3, 1, 5, 1, 2, 3, 9], [1, 2, 3, 9, 5, 3, 1, 5, 5, 3, 1, 5, 1, 2, 3, 9, 5, 6, 9, 2, 5, 3, 1, 5, 7, 8, 6, 5, 1, 2, 3, 9, 5, 6, 1, 2, 7, 8, 5, 9, 1, 2, 3, 9, 5, 3, 1, 5, 1, 2, 3, 9, 5, 3, 1, 5, 5, 3, 1, 5, 1, 2, 3, 9, 5, 6, 1, 2, 7, 8, 5, 9, 1, 2, 3, 9, 5, 3, 1, 5, 1, 2, 3, 9, 5, 3, 1, 5, 5, 3, 1, 5, 1, 2, 3, 9, 1, 2, 3, 9, 5, 3, 1, 5, 5, 3, 1, 5, 1, 2, 3, 9, 5, 6, 9, 2, 5, 3, 1, 5, 7, 8, 6, 5, 1, 2, 3, 9], [1, 2, 3, 9, 5, 3, 1, 5, 5, 3, 1, 5, 1, 2, 3, 9, 5, 6, 9, 2, 5, 3, 1, 5, 7, 8, 6, 5, 1, 2, 3, 9, 5, 6, 1, 2, 7, 8, 5, 9, 1, 2, 3, 9, 5, 3, 1, 5, 1, 2, 3, 9, 5, 3, 1, 5, 5, 3, 1, 5, 1, 2, 3, 9, 5, 6, 1, 2, 7, 8, 5, 9, 1, 2, 3, 9, 5, 3, 1, 5, 1, 2, 3, 9, 5, 3, 1, 5, 5, 3, 1, 5, 1, 2, 3, 9, 1, 2, 3, 9, 5, 3, 1, 5, 5, 3, 1, 5, 1, 2, 3, 9, 5, 6, 9, 2, 5, 3, 1, 5, 7, 8, 6, 5, 1, 2, 3, 9], [5, 6, 1, 2, 7, 8, 5, 9, 1, 2, 3, 9, 5, 3, 1, 5, 1, 2, 3, 9, 5, 3, 1, 5, 5, 3, 1, 5, 1, 2, 3, 9, 1, 2, 3, 9, 5, 3, 1, 5, 5, 3, 1, 5, 1, 2, 3, 9, 5, 6, 9, 2, 5, 3, 1, 5, 7, 8, 6, 5, 1, 2, 3, 9, 1, 2, 3, 9, 5, 3, 1, 5, 5, 3, 1, 5, 1, 2, 3, 9, 5, 6, 9, 2, 5, 3, 1, 5, 7, 8, 6, 5, 1, 2, 3, 9, 5, 6, 1, 2, 7, 8, 5, 9, 1, 2, 3, 9, 5, 3, 1, 5, 1, 2, 3, 9, 5, 3, 1, 5, 5, 3, 1, 5, 1, 2, 3, 9]]
benchmarks = ["Time", "Sample mean", "Standard deviation", "Geometric mean"]
algos = ["Classic", "Recursive", "Strassen"]
results = []


row1_results = []
row1_results.append(measure_time(multiply_classic, X, Y))
row1_results.append(measure_time(multiply_recursive, X, Y))
row1_results.append(measure_time(multiply_strassen, X, Y))
results.append(row1_results)
    
row2_results = []
row2_results.append(calculate_sample_mean(calculate_val(multiply_classic, X, Y)))
row2_results.append(calculate_sample_mean(calculate_val(multiply_recursive, X, Y)))
row2_results.append(calculate_sample_mean(calculate_val(multiply_strassen, X, Y)))
results.append(row2_results)

row3_results = []
row3_results.append(calculate_standard_deviation(calculate_val(multiply_classic, X, Y)))
row3_results.append(calculate_standard_deviation(calculate_val(multiply_recursive, X, Y)))
row3_results.append(calculate_standard_deviation(calculate_val(multiply_strassen, X, Y)))
results.append(row3_results)

row4_results = []
row4_results.append(calculate_geometric_mean(calculate_val(multiply_classic, X, Y)))
row4_results.append(calculate_geometric_mean(calculate_val(multiply_recursive, X, Y)))
row4_results.append(calculate_geometric_mean(calculate_val(multiply_strassen, X, Y)))
results.append(row4_results)

format_table(benchmarks, algos, results)