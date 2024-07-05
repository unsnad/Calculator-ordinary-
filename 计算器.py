'''
bilibili:1317826718
mail:unsnad1107@gamil.com
2923865644@qq.com
'''
a=eval(input('请输入第一个数字'))
op=input('请输入运算符')
b=eval(input('请输入第一个数字'))
if op=='+': # 检测运算符
    print(a+b)
elif op=='-':
    print(a-b)
elif op=='*':
    print(a*b)
elif op=='^':
    print(a**b)
elif op=='/':
    if b==0: # 检测除数是否为零
        print('除数不能为零')
    else:
        print(a+b)
else:
    print('非法的运算符')
