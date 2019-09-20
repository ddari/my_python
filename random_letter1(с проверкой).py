import random
s=['пирамида','треугольник','овал']
r=random.randint(0,len(s))
print ('Индекс слова:',r); 
if r==len(s): d=s.pop(r-1)
else: d=s.pop(r)
print('Само слово с эти индексом:',d) 

bukva =random.randint(0,len(d))
print('Индекс буквы',bukva) 
print('буква,которую загадали:',d[bukva-1]) 
print (d[+0:(bukva-1)]+"?"+d[+(bukva):])
x=str(input('Введите вашу букву:'))
if x==d[bukva-1]: print ('Вы угадали букву!!')
else: print('В следующий раз получится!')
