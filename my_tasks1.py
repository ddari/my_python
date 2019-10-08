import sys
zad=[]
kat=[]
sr=[]
obsh=[]
while True:
    a=str(input("введите задачу или напишите 'стоп' "))
    if a=='стоп':
        print(spisok)
        print(spisok1)
        print(obsh)
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
        m=[x for x in zad]
        spisok = dict(zip(zad, kat))
        spisok1=dict(zip(spisok,sr))
