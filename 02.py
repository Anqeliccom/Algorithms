x = int(input())
y = int(input())

def karasuba(x, y):
    # выход из рекурсии чтобы избежать бесконечности
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y

    # находим N/2 из формулы
    n = max(len(str(x)), len(str(y))) # берем макс, потом меньшее дополняем
    n2 = n // 2

    # вычисляем части
    a, b = divmod(x, 10 ** n2)
    c, d = divmod(y, 10 ** n2)

    # рекурсивно вычисляем ac, bd и (a+b)(c+d)
    ac = karasuba(a, c)
    bd = karasuba(b, d)
    ab_cd = karasuba(a + b, c + d)

    # вычисляем ad + bc
    ad_bc = ab_cd - ac - bd

    # суммируем со сдвигами (с теми самыми дополнениями)
    return (10 ** (2 * n2)) * ac + (10 ** n2) * ad_bc + bd

res = karasuba(x, y)
print(res)

# Тесты

x1 = 123
y1 = 456
assert karasuba(x1, y1) == x1 * y1

x2 = 12345
y2 = 456
assert karasuba(x2, y2) == x2 * y2

x3 = 123
y3 = 45678
assert karasuba(x3, y3) == x3 * y3