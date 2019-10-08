a=input('Введите число')
b=list(a)
sum=0
for i in range(len(b)):
    if int(b[i])%2!=0:
            sum=sum+int(b[i])**2
print(sum)
