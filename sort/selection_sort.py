"""
 배열에서 가장 작은 수를 맨앞의 원소와 바꾸는 과정을 반복하여 정렬을 진행하는 것
"""

# 선택정렬 소스 코드

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        #가장 작은 수 찾기
        if array[min_index] > array[j]:
            min_index = j
        #스왑
        array[i], array[min_index] = array[min_index], array[i]

#선택 정렬의 시간 복잡도
# O(N**2) = (N + 1) * N  / 2
# 직관적으로 이중 포문이므로 이렇게 진행된다.
# 과연 효율적일까? 이런 시간 복잡도를 가지는 선택정렬은 효율적인가?
# 특정 리스트에서 가장 작은 데이터를 찾는 일이 코딩 테스트에서 잦으므로 선택 정렬 소스코드 형태에 익숙해질 필요가 있다.
