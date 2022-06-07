#Coding Loops Program- Ujwal Jain
n=int(input("How many numbers do you want to see?"))
n1 = 0
n2 = 1
sum1 = 0
for i in range(n):
    print(sum1, end=' ')
    n1 = n2
    n2 = sum1
    sum1 = n1 + n2