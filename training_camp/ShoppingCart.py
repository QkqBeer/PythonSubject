#Shopping cart
#里面包含的元素应该是元组不能被修改用（）
f=open("file",'r')
shopping=[]
for line in f:
    temp1 = line.strip( '\n' )  # 去掉每行最后的换行符'\n'
    temp2 = temp1.split( ',' )  # 以','为标志，将每行分割成列表
    shopping.append( temp2 )         #将上一步得到的列表添加到new中
f.close()
#shopping=[['iphone',10000],['MacBook',12000],['coffee',31],['Book',50]]
salary=input("enter your salary:")
cart=[]
money=int(salary)
while True:
    print( '----------welcome to Shopping-------------' )
    for i in range( shopping.__len__( ) ) :
        print( '         '+ str(i)+"   " + shopping[ i ][ 0 ] + "  " + str( shopping[ i ][ 1 ] ) )
    xuhao=input("enter the shopping num or quit:")
    if xuhao=='q':
        print("退出超市系统")
        break
    elif int(shopping[int(xuhao)][1])<=money:
        cart.append(int(xuhao))
        money=money-int(shopping[int(xuhao)][1])
#没有考虑到用户的违规输入 :xuhao.isdigit()该方法进行判断输入的xuhao是否为数字。
    else :
        print("你的余额不足")
print("你的购物车有以下物品:")
for i in range (cart.__len__()):
    print(shopping[int(cart[i])][0]+"  "+shopping[int(cart[i])][1])
print("你的余额还剩："+str(money))
