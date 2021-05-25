"""

N명의 학생 정보가 있다. 학생 정보는 학생의 이름과 학생의 성적으로 구분된다. 각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오.

"""

n = int(input())
input_list = []

for i in range(n):
    input_data = input().split()
    input_list.append((input_data[0], int(input_data[1])))

input_list = sorted(input_list, key= lambda x: x[1])

for i in input_list:
    print(i[0], end= " ")

