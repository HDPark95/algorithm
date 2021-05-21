"""

기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸면 어떨까?
* 이해하긴 어렵지만, 이해하고나면 다른 병합 정렬, 힙 정렬 등 다른 고급 정렬 기법에 비해 쉽게 소스코드를 작성할 수 있다.
퀵 정렬에서는 피벗이 사용된다. 위의 기준을 의미함.
호어 분할 방식을 기준으로 퀵정렬을 설명

반 잘라서 기준보다 작으면 왼쪽으로 이동 크면 오른쪽으로 이동을 반복함
종료 시점은 리스트의 길이가 한개가 될 경우 종료

"""

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right - 1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)
