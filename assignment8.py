# 문제 : 여러분이 미국에 여행을 가서 상점에서 물건을 사고 거스름돈을 동전으로 받아
# 야 할 때, 보통 여행 할 때 주머니에 넣고 다니기 불편해서 최소한 적은 수의 동전으로
# 거스름돈을 받기를 원한다. 참고로 미국에는 동전이 1 cent(penny), 5 cent(nickle),
# 10cent(dime), 25 cent(quarter), 50 cent(half dollar), 100 Cent(silver dollar)이 있다.
# 이 때 거스름 받을 돈을 Cent 단위로 X 로 입력 받아서, 거슬러 받을 동전의 최소갯수
# Y를 출력하는 유사코드와 프로그래밍 코드를 작성하세요.

X = int(input())
Y = 0

while(1):
    if X >= 100:
        Y += X // 100
        X = X % 100
    elif X >= 50:
        Y += X // 50
        X = X % 50
    elif X >= 25:
        Y += X // 25
        X = X % 25
    elif X >= 10:
        Y += X // 10
        X = X % 10
    elif X >= 5:
        Y += X // 5
        X = X % 5
    else:
        Y += X
        break

print(Y)
