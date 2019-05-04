
f=open("file",'r') #使用file文件
shopping=[]
for line in f:
    temp1 = line.strip( '\n' )  # 去掉每行最后的换行符'\n'
    temp2 = temp1.split( ',' )  # 以','为标志，将每行分割成列表
    shopping.append( temp2 )         #将上一步得到的列表添加到new中
while True:
    print( '----------welcome to Shopping System-------------' )
    for i in range( shopping.__len__( ) ) :
        print( "       " + str( i ) + "  " + shopping[ i ][ 0 ] + "  " + str( shopping[ i ][ 1 ] ) )
    choice=input("修改商品价格c，添加新的商品i或退出q:")
    if choice=='c':
        id=input("输入商品id：")
        newPrice=input("新的商品价格：")
        shopping[int(id)][1]=newPrice
    elif choice=='i':
        name=input("输入商品名称：")
        price=input("输入商品价格：")
        shopping.append([name,price])
    elif choice=='q':
        break
    else:
        print("无效输出")
f.close()
f=open('file','w')
for i in shopping :
    f.write(i[0]+','+i[1]+"\n")
f.close()

