film=str(input('Введите название фильма:'));
date=str(input('Введите день(сегодня/завтра):'));
tim=int(input('Введите время сеанса:'));
k=int(input('Укажите количество билетов:'));
s=1
if date=='завтра':s=0.95
if k>=20: s=0.8
if k>=20 and date=='завтра':s=0.75;
      
if film=='Пятница':
                     if tim==12:
                              print ('Стоимость ваших билетов:',250*k*s)
                                            
                     elif tim ==16:
                              print ('Стоимость ваших билетов:',350*k*s)
                     elif tim==20:
                              print ('Стоимость ваших билетов:',450*k*s)
                     else:  print ('Такого сеанса нет')
elif film=='Чемпионы':
                     if tim==10:
                              print ('Стоимость ваших билетов:',250*k*s)
                                            
                     elif tim ==13:
                              print ('Стоимость ваших билетов:',350*k*s)
                     elif tim==16:
                              print ('Стоимость ваших билетов:',350*k*s)
                     else: print ('Такого сеанса нет')         
elif film=='Пернатая банда':
                     if tim==10:
                              print ('Стоимость ваших билетов:',350*k*s)
                                            
                     elif tim ==14:
                              print ('Стоимость ваших билетов:',450*k*s)
                     elif tim==18:
                              print ('Стоимость ваших билетов:',450*k*s)
                     else: print ('Такого сеанса нет') 
                              
else: print ('Такого фильма нет')


'''SyntaxError: Non-ASCII character '\xd0' in file main.py on line 1, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details'''
        
                                         
                     
                                    
                                     
                                            
                                        
            

