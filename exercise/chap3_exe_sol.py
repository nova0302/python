i=0
while i<6:
    print('*' * i)
    i += 1


A= [70,60,55,75,95,90,80,80,85,100]
total =  0
for  i in  A:
    total += i 
average = total/len(A)
print('평균: ', average)

print('평균: ', sum(A)/len(A))
