a = float(input())
b = float(input())
r = a/b
if a > b:
    print("Фирма работает в прибыль")
    print("Рентабельность составляет " + str(r))
    d = int(input("Введите число сотрудников фирмы"))
    print("Прибыль фирмы в расчете на одного сотрудника: "+ str((a-b)/d))
if a < b:
    print("Фирма работает в убыток")
if a == b:
    print("Фирма работает ни в прибыль, ни в убыток")
