import sys
zad=[]
kat=[]
sr=[]
obsh=[]
while True:
    a=str(input("введите задачу или <стоп> "))
    if a=='стоп':
        print(obsh)
        print(spisok1)
        print("до свидания!")
        sys.exit()
    else:
        zad.append(a)
        obsh.append(a)
        b=str(input("Введите категорию"))
        kat.append(b)
        obsh.append(b)
        c=int(input("Введите срок выполнения в днях"))
        obsh.append(c)
        sr.append(c)
        spisok = dict(zip(zad, kat))
        spisok2=dict(zip(spisok,zip(kat,sr)))
