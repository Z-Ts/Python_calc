print ('введите первое число')
a1  =input()
a2 = complex (a1)
print (a2)
print ('введите второе число')
b1  =input()
b2 = complex (b1)
print (b2)
print ('введите оператор')
a3  = input ()
res = 0
if a3 == '*':
    res = a2*b2
elif a3 == '/':
    res = a2/b2
elif a3 == '+':
    res = a2+b2
elif a3 == '-':
    res = a2-b2

print ( a2 , a3 , b2 ,'=' ,  res)