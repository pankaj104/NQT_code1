n= int(input("Enter no of integer value:  "))
arr1=[]
arr1= list(map(int,input().strip().split(",")))[:n]

arr2=[]
arr3=[]
for j in range(0,n):
    if(arr1[j] == 0):
        arr3.append(arr1[j])
    else:
        arr2.append(arr1[j])

x=arr2+arr3
print(x)


