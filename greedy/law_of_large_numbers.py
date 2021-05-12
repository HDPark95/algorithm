"""

해당 문제의 대수의 법칙은 통계학에서 나오는 대수의 법칙과는 다름.
해당 대수의 법칙은 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.

입력 조건

* 첫째 줄에 N, M, K의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.

* 둘재 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10,000이하의 수로 주어진다.

* 입력으로 주어지는 K는 항상 M보다 작거나 같다.

출력 조건

* 첫째 줄에 동빈이의 큰수의 법칙에 따라 더해진 답을 출력한다.

"""


n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)

#더 나은 답안

n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

count = int(m/ (k+1))*k
count += m % (k+1)

result = 0
result += (count)*first
result += (m-count)*second

print(result)
