s='У лукоморья 123 дуб зеленый 456'
ya=s.find('я')
if ya>0:
       print ('Индекс буквы "я":',ya)
else: print('Такой буквы нет');
ch=s.count('у')
print ('Буква "у" встречается', ch,'раз');
if s.isalpha()!=True: print (s.upper());
if len(s)>4: print (s.lower());
'''1 вариант''' 
s=s[:0]+"О "+s[2:]
print (s)
'''2 вариант''' 
d=list(s)
d[0]="О"
s=''.join(d)
print (s)


