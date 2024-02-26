def division(dividend, divider):
    digits = [int(digit) for digit in str(dividend)]
    
    result = []
    ost = 0
    
    for i in digits:
        i += ost * 10  # учитываем остаток от предыдущего разряда
        c = 0
        whole = 0
        
        # своё деление
        for j in range(9, -1, -1):
            c = divider * j
            if c <= i:
                whole = j
                break

        ost = i - whole * divider # свой остаток
        result.append(whole)

    result_str = [str(digit) for digit in result]
    result_string = ''.join(result_str)
    result_number = int(result_string)
    
    return result_number, ost

# Пример использования
dividend = 43916
divider = 78

result, remainder = division(dividend, divider)
print("Результат:", result)
print("Остаток:", remainder)
