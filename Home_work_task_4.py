#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
#Позиции хранятся в отдельном списке
# пример n=4, lst1=[4,-2,1,3] - списко на основе n, а позиции элементов lst2=[3,1].
import random
number = int(input())
list1 = []
list2 = [3,1]
answer = 1
for i in range(number):
    list1.append(random.randrange(number*-1, number))
for i in list2:
    answer *= list1[i]
print(answer)
