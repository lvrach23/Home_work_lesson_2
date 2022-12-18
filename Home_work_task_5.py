#Реализуйте алгоритм перемешивания списка. (рандомно поменять местами элементы списка между собой)
import random
list1 = [1, 2, 3, 4, 5,]
for i in range(len(list1)):
    k = random.randrange(0, 5)
    j = random.randrange(0, 5)
    temp = list1[k]
    list1[k] = list1[j] 
    list1[j] = temp
print(list1)
