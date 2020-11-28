# 문제 : 아래 그림과 같은 그래프에서 어떤 한 Node에서 출발하여 그래프 상의 각 정점을
# 한번씩 만 경유하여 다시 출발한 정점으로 돌아오는 경로를 구하는 유사코드와 프로그
# 램을 작성하세요. (아래의 한정조건을 이용하고 백트래킹 방법론 사용(txt파일제출))
#  실습내용
# 백트래킹에 대한 개념이해를 바탕으로 한정조건문제를 풀기 위한 효율성 증대방
# 법을 생각해 보고, 백트래킹 알고리즘의 구현과 활용을 이해한다. 유사코드를 사
# 용하여 알고리즘 코드를 작성해 보고 그것의 프로그램 구현코드를 작성해서 실
# 행해 본다.
# 한정조건 : 경로 상의 i번째 정점은 그 경로 상의
# (i - 1)번째 정점과 반드시 이웃 해야 하며, (n - 1)번
# 째 정점은 반드시 0번째 정점(출발점)과 이웃해야
# 하고, i번째 정점은 그 앞에 오는 i - 1개의 정점이
# 될 수 없음.


def hamiltonian(i, W, vindex):
    n = len(W) - 1
    if (promising(i, W, vindex)):
        if (i == (n-1)):
            print(vindex[0:n])
        else:
            for j in range(2, n+1):
                vindex[i+1] = j
                hamiltonian(i+1, W, vindex)


def promising(i, W, vindex):
    flag = True
    if((i == (n-1)) and not W[vindex[n-1]][vindex[0]]):
        flag = False
    elif((i > 0) and not W[vindex[i-1]][vindex[i]]):
        flag = False
    else:
        j = 1
        while(j < i and flag):
            if(vindex[i] == vindex[j]):
                flag = False
            j += 1
    return flag


n = 8
edges = [[1, 2], [1, 3], [1, 7], [1, 8], [2, 3], [2, 7], [
    2, 8], [3, 4], [3, 6], [4, 5], [5, 6], [6, 7], [7, 8]]

W = [[False]*(n+1) for _ in range(n+1)]
for e in edges:
    W[e[0]][e[1]] = W[e[1]][e[0]] = True
vindex = [-1] * (n+1)
vindex[0] = 1
hamiltonian(0, W, vindex)
