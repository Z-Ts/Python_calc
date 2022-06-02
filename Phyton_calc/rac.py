print ('введите первое число')
a1  = float(input ())
print ('введите второе число')
a2  = float(input ())
print ('введите оператор')
a3  = input ()
res = 0
if a3 == '*':
    res = a1*a2
elif a3 == '/':
    res = a1/a2
elif a3 == '+':
    res = a1+a2
elif a3 == '-':
    res = a1-a2
print (a1,a3,a2, '=' ,res)