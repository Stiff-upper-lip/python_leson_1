# Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
# str = '0000000000000000000'
# for i in range(5):
#     print('№ {} - {}'.format(i+1, str))


# Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
ent = []
s_ = 0
for i in range(10):
    ent.append(int(input('enter number')))
    if ent[i] == 5:
        s_ += 1
print('пользователь ввел количество пятёрок {} из десяти надуманных чисел'.format(s_))


# Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
# prod = 1
# for i in range(1, 11):
#     prod *= i
# print(prod)


# Найти сумму цифр числа
# num = int(input('введите число: '))
# result = 0
# while num > 0:
#         result += num % 10
#         num //= 10
# print('cумма ваших цифр равна = ', result)


# Найти произведение цифр числа
# num = input('введите число: ')
# prod = 1
# for i in num:
#     prod *= int(i)
# print(prod)

# Найти максимальную цифру в числе
# maxi = 0
# num = input('введите число: ')
# for i in range(len(num)):
#     if (int(num[i]) > maxi):
#         maxi = int(num[i])
# print('максимальное число = ', maxi)


# Найти количество цифр 5 в числе
# num = input('введите число: ')
# count = 0
# for i in range(len(num)):
#     if int(num[i]) == 5:
#         count += 1
# print('количество пятёрок в числе = ', count)


