#Найдите сумму цифр трехзначного числа.
#Пример:
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0)

numbers = int(input('Введите трехзначное число: '))

if numbers < 1000 and numbers > 99 :
    print('Сумма цифр числа',numbers,' - ', (numbers // 100) + (numbers % 100 // 10) + (numbers % 10))
else:
    print('Введено неподходящее число.')
