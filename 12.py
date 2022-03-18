
import random , sys
rz = random.randint(1,3)

hand = 'q'

def phand() :
    if hand == 'r':
        print('剪刀')
    elif hand == 's':
        print('石头')
    elif hand == 'p':
        print('布')
    else :
        print('')
print('现在我们进行剪刀石头布的游戏吧 \n 剪刀为r 石头为s 布为p 退出为q')
u_hand = input('出手：')


if rz == 1:
    hand = 'r'
elif rz == 2:
    hand = 'p'
elif rz == 3:
    hand = 's'

   
#print(rz)
#print(hand)
    if u_hand == 'r' :
        if hand == 'p' :
            phand()
            print('你赢了')            
        elif hand == 's':
            phand()
            print('你输了')                    
        else :
            phand()
            print('你打了平手')                    
    elif u_hand == 's':
        if hand == 'r' :
            phand()
            print('你赢了')            
        elif hand == 'p':
            phand()
            print('你输了')            
        else :
            phand()
            print('你打了平手')                    
    elif u_hand == 'p':
        if hand == 'S' :
            phand()
            print('你赢了')            
        elif hand == 'R':
            phand()
            print('你输了')            
        else :
            phand()
            print('你打了平手')
    else :
        sys.exit()
print('过的开心')