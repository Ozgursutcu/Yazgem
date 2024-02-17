#En küçük değer bulunana kadar ilerle.
#Sağındaki değerle karşılaştır küçükse sola doğru karşılaştırma yaparak ilerle.
#Soldaki değer küçükse dur.

#----------Insertion Sort----------#

def insertionSort(list):
    n=len(list)
    for i in range(1, n):
        num=list[i]
        index=i
        print(num,end=": \n")
        while (index > 0 and num < list[index-1]): #If we change the comparison operator on 2nd condition to opposite we can change the sorting to opposite
            list[index]=list[index-1]
            index-=1
            print(list[:i+1])
        list[index]=num
        print(list[:i+1])
        print("-"*40)

#----------------------------------#

import random

listItem=[]
for i in range(5):
    j = random.randint(0,100)
    listItem.append(j)
print(listItem)

insertionSort(listItem)

#----------------------------------#