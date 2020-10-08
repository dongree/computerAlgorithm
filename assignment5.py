def quick_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    pivot = input_list[0]
    left_arr, equal_err, right_arr = [], [], []
    for i in input_list:
        if i < pivot:
            left_arr.append(i)
        elif i > pivot:
            right_arr.append(i)
        else:
            equal_err.append(i)
    return quick_sort(left_arr) + equal_err + quick_sort(right_arr)


def calc(input_list):
    result = 0
    for i in range(len(input_list)):
        if i % 2 == 0:
            result += input_list[i]
        else:
            result -= input_list[i]
    return result


print("정수의 개수를 입력하세요")
n = int(input())

input_list = []
print(str(n) + "개의 정수를 입력하세요")
for i in range(n):
    input_list.append(int(input()))

input_list = quick_sort(input_list)
print("\n다음과 같이 정렬되었습니다")
print(input_list, "\n")

result = calc(input_list)
print("특정 연산을 수행한 후에 결과 값입니다.")
print(result)
