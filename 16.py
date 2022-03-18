while True :
    print("请输入q退出")
    fn = input("> 第一个数：")
    if fn=='q' :
        break

    ysf = input("\n> 运算符：")
    if ysf=='q'  :
        break

    ln = input("\n> 第二个数")
    if ln=='q':
        break

    ds = 0
    ##“ds”的意思是得数

    if ysf == '+':
        ds = int(fn) + int(ln)
        print(f"得数是{str(ds)}\n\n")
    elif ysf == '-':
        ds = int(fn) - int(ln)
        print(f"得数是{str(ds)}\n\n")
    elif ysf == '*':
        ds = int(fn) * int(ln)
        print(f"得数是{str(ds)}\n\n")
    elif ysf == '/':
        try:
            ds = int(fn) / int(ln)
        except ZeroDivisionError:
            print("除数不能为零")
        else:
            print(f"得数是{str(ds)}\n\n")
    else :
        print("请输入正确的数或符号\n\n")