import random
a=[random.randint(-1000,1000) for x in range(1,1001)]
min=a[0]
max=a[0]
m=0
k=0
ma=0
for i in range(len(a)):
    if a[i]<min:
        min=a[i]
        m=i

    if a[i]>max:
        max=a[i]
        ma=i
if ma>m:
    sp=a[m:ma+1]
else:
    sp=a[ma:m+1]
for i in range(len(sp)):
        if sp[i]<0:
            k=k+1
print("сгенерированный список",a)
print("от минимального до макисмального",sp)
print("количество отрицательных",k)
