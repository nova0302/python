pin = "881120-1068234"
yymmdd = pin[0:6]
num = pin[7:]
print(yymmdd)
print(num)
print(pin[7])

a  = [1,3,5,4,2]
print('a: ', a)
a.sort()
print('a.sort(): ', a)
a.reverse()
print('a.reverse(): ', a)

a=['Life', 'is', 'too', 'short']
print('a:', a)
a.reverse()
print('a:', a)
str=''
while a:
    str+= a.pop() + ' '
print(str)

a=['Life', 'is', 'too', 'short']
print('a:', a)
i = 0
str= ''
while  i < len(a):
    str+= a[i] + ' '
    i += 1
print(str)

a=(1,2,3)
print(a)
a = a + (4,)
print(a)

a = {'A':90, 'B':80, 'C':70}
print(a['B'])
del a['B']
print(a)

a = [1,1,1,2,2,3,3,3,4,4,5]
print('a:', a)
aSet =set(a)
print('aSet:', aSet)

