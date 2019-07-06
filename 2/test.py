#x = int(input("请输入年龄: "))
#
#if x < 18 :
#    print('未成年')
#elif x < 50 :
#    print("青年")
#else :
#    print("老年")
#
#num = 12
#
#for i in range(4, num) :
#    print(i)
alist = []
for i in range(1, 11) :
    if i%2 == 0 :
        alist.append( i*i  )
print(alist)

blist = [ i*i for i in range(1, 11) if i%2 == 0 ]
print(blist)
