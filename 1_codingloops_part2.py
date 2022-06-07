lst1=[]
lst2=[]
num=int(input("How many numbers does the range include?"))
for i in range(num):
    num1=int(input("Enter number within range: "))
    lst1.append(num1)
for i in lst1:
    if(i>0):
        lst2.append(i)
lst1=lst2
print(lst1)