import random
s=['пирамида','треугольник','овал']
r=random.randint(0,len(s))
print ('Индекс слова:',r); 
if r==len(s): d=s.pop(r-1)
else: d=s.pop(r)
print('Само слово с эти индексом:',d) 

bukva =random.randint(0,len(d))
print('Индекс буквы',bukva)
if bukva==0: m=bukva+1
else: m=bukva;
print('буква,которую загадали:',d[m-1]) 
print (d[+0:m-1]+"?"+d[+m:])
x=str(input('Введите вашу букву:'))
if x==d[m-1]: print ('Вы угадали букву!!')
else: print('В следующий раз получится!')
