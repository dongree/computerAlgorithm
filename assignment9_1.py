# 문제 : 어떤 도둑이 금은방에서 배낭을 매고 침입했다. 훔칠 보석의 총 중량이 X(kg)를
# 초과(이하까지 가능)하면 배낭을 쓸 수가 없다. 도둑은 각 보석의 중량과 그것에 대한
# 돈 환산가치를 잘 알고 있다. 이 도둑은 총 무게가 X(kg)을 초과하지 않으면서 보석들
# 의 총 돈 환산치가 최대가 되도록 보석을 배낭에 담고자 한다. 훔치는 모든 보석들을
# 쪼갤 수 있다고 가정 했을 때와 쪼갤 수 없다고 가정 했을 때 두 가지 경우에 대하여
# 돈 환산 가치로 최대치를 배낭에 담을 수 있는 유사코드와 프로그래밍 코드를 작성하
# 세요.


items = [(1, 60, 10), (2, 100, 20), (3, 120, 30)]

items_sorted = sorted(items, key=lambda item: item[2]/item[1])


def fractionalKnapsack(item, x):
    limit = x
    result = 0
    for i in range(len(items_sorted)):
        cur = items_sorted[i]
        if(limit > 0):
            if(limit > cur[2]):
                limit -= cur[2]
                result += cur[1]
            else:
                result += cur[1]/cur[2]*limit
                limit = 0
        else:
            break
    return result


print(fractionalKnapsack(items, 30))
