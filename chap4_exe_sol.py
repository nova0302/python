#n    1 2 3 4 5 6  7  8
#f(n) 1 1 2 3 5 8 13 21
def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-1) + fib(n-2)

print('fib(8): ', fib(8))
'''
 sample.txt
   70 
   60 
   55 
   75 
   95 
   90 
   80 
   80 
   85 
  100 
'''

f = open('sample.txt')
lines = f.readlines()
f.close()

total = 0
for line  in lines:
    score = int(line) 
    total += score

average = total / len(lines)
f = open('result.txt', 'w')
f.write('평균: ')
f.write(str(average))
f.close()
