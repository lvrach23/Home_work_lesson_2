#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример: - 6782 -> 23 - 0,56 -> 11
num =float(input("введите число: "))
sum = 0
count = 0
if num % 1 == 0:
    while num != 0:
        sum+=num%10
        num//=10
    print(int(sum))
else:
    while round(num % 1, 1) != 0:
        num *= 10
        count += 1
    while num % 10 != 0:
        sum+=num%10
        num//=10
    print(int(sum))

