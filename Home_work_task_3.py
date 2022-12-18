#Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
number = int(input())
sum = 0
sequence = 0
dict = {}
for i in range(1,number+1):
    sequence = round((1+1/i)**i, 2)
    sum +=sequence
    dict[i]=sequence
print(dict)
print(sum)