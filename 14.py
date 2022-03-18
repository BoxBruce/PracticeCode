#料 = (input('>>>'))
#配料 = []
#配料.insert(-1,料)
#if 配料:
#    for i in 配料:
#        if i == '大葱' :
#            print('我们店的大葱用完了')
#        else :
#            print(f'你想吃{i}馅的馅饼吗')
#else :
#    print('你想吃面饼吗')
#input('>>>')
#print('已下达')
def gcd(a,b):
    if b!=0:
        return gcd(b,a%b)
    else:
        return a

print(gcd(0,123))