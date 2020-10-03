
ex_list = [['고동우', 'IELTS', 6.5, 4.0], ['지석진', 'TOEFL', 97, 3.8], ['김종국', 'TOEFL', 74, 4.3], ['유재석', 'IELTS', 7.0, 4.1], [
    '하동훈', 'IELTS', 5.5, 3.7], ['이광수', 'TOEFL', 79, 2.9], ['송지효', 'IELTS', 6.0, 4.3], ['양세찬', 'TOEFL', 70, 3.3], ['전소민', 'TOEFL', 84, 4.5]]


def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list

    mid = len(unsorted_list)//2
    left = unsorted_list[:mid]
    right = unsorted_list[mid:]

    left1 = merge_sort(left)
    right1 = merge_sort(right)
    return merge(left1, right1)


def merge(left, right):
    i = 0
    j = 0
    sorted_list = []

    while (i < len(left)) and (j < len(right)):
        if left[i][4] >= right[j][4]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    while (i < len(left)):
        sorted_list.append(left[i])
        i += 1

    while (j < len(right)):
        sorted_list.append(right[j])
        j += 1
    return sorted_list


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
print(merge_sort(mean_list))
