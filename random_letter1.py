import random
s=['пирамида','треугольник','овал']
r=random.randint(0,len(s))                
if r==len(s): d=s.pop(r-1)
else: d=s.pop(r)                  
bukva =random.randint(0,len(d))           
                                          
print (d[+0:(bukva-1)]+"?"+d[+(bukva):])
x=str(input('Введите вашу букву:'))
if x==d[bukva-1]: print ('Вы угадали букву!!')
else: print('В следующий раз получится!')


