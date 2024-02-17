"""
Linear Seacrh
Aranacak eleman, listenin ilk indexinden itibaren aranmaya başlanır.
Aranan eleman listenin içinde var ise arama olumlu sonlanır.
Aranan eleman listenin içinde yok ise arama olumsuz sonuçlanır
"""
#------------------------Linear Search------------------------#
def linearSearch(list,target):
    for x in list:
        if (x!=target):
            continue
        elif (x==target):
            return True

#----------------Linear Search & Return Index----------------#

def linearSearchAndIndex(list,target):
    n=len(list)
    for i in range(0,n):
        if (list[i] != target):
            continue
        if (list[i]==target):
            return i
        
#------------------------------------------------------------#

array=[10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
searching=5

answer=linearSearch(array,searching)
if(answer):
    print(searching," is included in the array.")
else:
    print(searching," is not included in the array.")

#------------------------------------------------------------#
searching=5
answer_i=linearSearchAndIndex(array,searching)
if(answer_i>=0):
    print(searching," is included in the array. Index number: ",answer_i)
else:
    print(searching," is not included in the array. Result: ",answer_i)


#------------------------------------------------------------#