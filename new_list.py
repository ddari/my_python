import math
l=[2,4,9,16,25]
res=[]
''' 1 способ '''
def new1(l):
    for i in l: res.append (math.sqrt(i))
    return res
print (new1(l))
''' 2 способ  '''
def new2(l):
    def f(x):
        return math.sqrt(x)
    res1=list(map(f,l))
    return res1
print (new2(l))
'''     3 способ    '''
def new(l):
    res2=[math.sqrt(i) for i in l]
    return res2
print (new(l))
