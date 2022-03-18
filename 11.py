import random
#这是一个猜数字的小游戏
oldnb = random.randint(1,1000)
print('猜一个数字，在1~1000之间')

newnb = input('猜吧：')
int(newnb)
while True :
    while oldnb != newnb :
        if int(newnb) > oldnb :
            print('大了')
            newnb = input('再猜：')
        elif int(newnb) < oldnb :
            print('小了')
            newnb = input('再猜：')
            int(newnb)
        elif newnb == "q" :
            break
        else:
            print('你猜对啦')
            break
