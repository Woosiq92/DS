## A는 1*1크기의 정사각형으로 나누어진 N*M 크기의 정사각형 위에 서있다.
## 가장 왼쪽 위 좌표는(1,1), 가장 오른쪽 아래 좌표는 (N, M) 
## A는 (N,M) 안에서 상(U)하(D)좌(L)우(R)로만 이동할 수 있으며, 시작 좌표는 항상 (1,1) 이다.
 
#첫째줄에 공간의 크기를 나타내는 N이 주어진다.  ( 1 <= N <=100)
# 둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다. ( 1 <= 이동횟수 <=100) 

n = int(input())
x, y = 1, 1
plans = input().split()

#이동 방향 
dx = [0, 0, -1, 1]
dy =[-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']


#이동 계획을 하나씩 확인 
for plan in plans: 
	#이동 후 좌표 구하기 
	for i in range(len(move_types)):
		if plan == move_types[i]:
			nx = x + dx[i]
			ny = y + dy[i]
	#공간을 벗어나는 경우 
	if nx < 1 or ny < 1 or nx > n or ny > n:
		continue
	x, y = nx, ny 
print(x, y)  
  