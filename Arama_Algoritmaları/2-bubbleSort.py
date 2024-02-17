"""
İlk indexdeki sayıyı al.
Daha büyük sayı bulana kadar sağa ötele.
Yeni sayı içinde aynı ötelemeyi yapıp daha büyük sayıyı liste sonuna kadar ötele.

"""

#----------Bubble Sort----------#

def bubbleSort(list):
    n=len(list)
    for i in range(0, n-1):
        for j in range(0, n-1-i):
            if (list[j] > list[j+1]):
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
        #print(list)
    print(list)   

#-------------------------------#

import random

listItem=[]
for i in range(4):
    
    j = random.randint(0,100)
    listItem.append(j)
print(listItem)

bubbleSort(listItem)

#-------------------------------#