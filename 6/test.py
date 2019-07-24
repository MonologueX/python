#x = input('请输入一个整数>')
#length = len(x)
#for i in range (length-1, -1, -1):
#    print(x[i])
#for i in range(5):
#    if i == 0 or i == 5-1 :
#        print("*****")
#    else :
#        print("*   *")
#sum = 0
#for i in range(1, 100, 2):
#    sum += 2
#print(sum)

#a = input("first")
#b = input("second")
#print(1, 2, sep=' ', end=' ')
#for i in range(1, 10):
#    for j in range(1, i+1):
#        print(str(i)+'*'+str(j)+'='+str(i*j), end='\t')
#    print()
#print("a={:2}".format(12))
#print("a={:2}".format(9))
#for i in range(1, 10):
#    for j in range(i, 10):
#        print(i, '*', j, '=', i*j, sep='', end='\t')
#    print()
import datetime
start = datetime.datetime.now()
for i in range(1, 10):
    for j in range(i, 10):
        print('{}*{}*={}'.format(i, j, i*j), sep='', end='\t')
    print()
delta = (datetime.datetime.now()-start).total_seconds()
print(delta)
