def bubble_sort(list1):
    for i in range(0,len(list1)-1):
        for j in range(len(list1)-1):
            if(list1[j] > list1[j+1]):
                temp=list1[j]
                list1[j]=list1[j+1]
                list1[j+1]=temp
    return list1
list1=list()
x=int(input("enter the number"))
for i in range(0,x):
    y=int(input("enter number to append"))
    list1.append(y)
print("the list1 before sorting")
print(list1)
print("the list1 after sorting")
print(bubble_sort(list1))




