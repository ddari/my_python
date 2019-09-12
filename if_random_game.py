import random
run=random.randint(1,4);
my = int(input("Ты думаешь, что я загадал число:"))
if run==my : print ("Ты угадал!");
elif run>my: print ("Мое число больше!");
elif run< my: print("Мое число меньше!");

