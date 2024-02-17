
#Listenin en küçük elemanını bul.
#En sola gönder.
#Listenin baştan ikinci indexine listenin kalanındaki en küçük sayıyı bulup taşı.
#Index değerini arttırarak devam et.


#----------Selection Sort----------#

def selectionSort(list):
    n=len(list)
    for i in range(0, n-1):
        print("Input: ",list)
        minIndex=i
        for j in range(i+1, n):
            if (list[j] < list[minIndex]):
                minIndex=j
        if (minIndex!=i): #Do if variable isn't on the index that it should be on
            temp=list[i]
            list[i]=list[minIndex]
            list[minIndex]=temp
        print("Output: ",list)
        print("-"*40)

#----------------------------------#

import random

listItem=[]
for i in range(5):
    j = random.randint(0,100)
    listItem.append(j)
print(listItem)

selectionSort(listItem)

#----------------------------------#