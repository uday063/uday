a=[1,23,4,6,89,0]
max=second=a[0]
for i in range(len(a)):
    if(a[i]>max):
        second=max
        max=a[i]
    elif(a[i]>second and a[i]<max):
        second=a[i]
print(second)