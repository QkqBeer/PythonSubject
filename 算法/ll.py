__author__ = "那位先生Beer"
def solution(N,M,list):
    total = 1;
    count = 1;
    flag = 1;
    for i in range(N-1):
        for j in range(flag , N):
            if list[2*i + 1] <= list[2*j]:
                count += 1
                flag += 1
                break;
        if count > total:
            total = count

    return total
def inputcc():
    list=[]
    str1 = input("请输入N：");
    N=int(str1)
    str2= input("请输入M：");
    M=int(str2)
    str3=input("请输入：");
    x=str3.split()
    for i in x:
        m=int(i)
        list.append(m)
    print(solution(N,M,list))
inputcc()
