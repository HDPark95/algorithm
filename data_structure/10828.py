"""

#스택 자료형

"""

n = input()
result_list = []

for i in range(n):
    commend = input()
    if commend.find("push") != -1 :
        commend, number = commend.split(" ")
        result_list.append(number)
    elif commend.find("pop") != -1 :
        print(result_list.pop())
    elif commend.find("size") != -1:
        print(len(result_list))
    elif commend.find("empty") != -1:
        if len(result_list) != 0:
            print(1)
        else:
            print(0)
    elif commend.find("size") != -1:
        if len(result_list) == 0:
            print(-1)


