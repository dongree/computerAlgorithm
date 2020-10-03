ex_list = [['고동우', 'IELTS', 6.5, 4.0], ['지석진', 'TOEFL', 97, 3.8], ['김종국', 'TOEFL', 74, 4.3], ['유재석', 'IELTS', 7.0, 4.1], [
    '하동훈', 'IELTS', 5.5, 3.7], ['이광수', 'TOEFL', 79, 2.9], ['송지효', 'IELTS', 6.0, 4.3], ['양세찬', 'TOEFL', 70, 3.3], ['전소민', 'TOEFL', 84, 4.5]]


def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j][4] > arr[min_idx][4]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def conversion_score(list):
    new_list = []
    for i in range(len(list)):
        if list[i][1] == 'IELTS':
            if list[i][2] >= 6.0:
                list[i][2] = ielts(list[i][2])
                list[i][3] = grade(list[i][3])

                new_list.append(list[i])
        elif list[i][1] == 'TOEFL':
            if list[i][2] >= 80:
                list[i][2] = toefl(list[i][2])
                list[i][3] = grade(list[i][3])
                new_list.append(list[i])
    return new_list


def ielts(score):
    if score == 6.0:
        score = 70
    elif score == 6.5:
        score = 80
    elif score == 7.0:
        score = 90
    else:
        score = 100
    return score


def toefl(score):
    if (score >= 80 and score < 90):
        score = 70
    elif (score >= 90 and score < 100):
        score = 80
    elif (score >= 100 and score < 110):
        score = 90
    else:
        score = 100
    return score


def grade(score):
    conversion_score = score * 200 / 9
    return round(conversion_score, 2)


def mean_score(list):
    for i in range(len(list)):
        mean = (list[i][2] + list[i][3]) / 2
        list[i].append(mean)
    return list


conversion_list = conversion_score(ex_list)
mean_list = mean_score(conversion_list)
sorted_list = selection_sort(mean_list)

print('셰필드 대학교 교환학생 모집인원 : 4명\n')
print('<결과>')
for i in range(len(sorted_list)):
    if i < 4:
        print(i+1, '등:', sorted_list[i][0], '합격')
    else:
        print(i+1, '등:', sorted_list[i][0], '불합격')
