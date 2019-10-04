import random
import sys
n=int(input('Введите нижнюю границу'))
v=int(input('Введите верхнюю границу'))
a=random.randint(n,v)
k=5
while k>0:
    b=input('Введите число от 1 до 1000 ')
    if b=="Выход":
                print("Выход из игры")
                sys.exit()
    elif int(b)!=a:
                if int(b)>a:
                    print("Загаданное число меньше")
                elif int(b)<a:
                    print("Загаданное число больше")
    elif int(b) == a:
                print("Вы угадали")
                sys.exit()
            
    k-=1
