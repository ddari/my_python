import random
s=['пирамида','треугольник','овал']
r=random.randint(0,len(s))                
if r==len(s): d=s.pop(r-1)
else: d=s.pop(r)                  
bukva =random.randint(0,len(d))
if bukva==0: m=bukva+1
else: m=bukva;
print (d[+0:(m-1)]+"?"+d[+m:])
x=str(input('Введите вашу букву:'))
if x==d[bukva-1]: print ('Вы угадали букву!!')
else: print('В следующий раз получится!')


