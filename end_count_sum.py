sum=0
while True:
    b=input('Введите число или Стоп')
    if str(b)=="Стоп":
        print("Выход из программы")
        break
    elif b.isdigit():
        sum=sum+int(b)
    else:
        print("Не понимаю...Повторите попытку")
print(sum)
