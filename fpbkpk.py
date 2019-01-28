x1 = int(input('Ketik angka pertama: '))
x2 = int(input('Ketik angka kedua: '))

def factor(a):
    list1=[]
    for i in range(1,a+1):
        if a%i == 0:
            list1.append(i)
    return list1

def fpb(x,y):
    return max(list(set(factor(x)) & set(factor(y))))
def kpk(x,y):
    if x>y:
        z=x
    else:
        z=y
    while(True):
        if z%x==0 and z %y ==0:
            kpk = z
            break
        z +=1
    return kpk

print('fpb dari',x1,'dan',x2,'adalah = ',fpb(x1,x2))
print('kpk dari',x1,'dan',x2,'adalah = ',kpk(x1,x2))
    
