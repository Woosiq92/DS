# 여러 숫자중 가장 높은 카드가 쓰인 카드 한장을 뽑는 게임 
# 숫자가 쓰인 카드들이 N *M 형태로 놓여 있다. (행, 열 형태) 
# 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
# 그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다. 
#다음 행에서 가장 낮은 카드를 뽑을 것을 대비해 최종적으로 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다. 

# min 함수 사용 예시 

n, m = map(int, input().split()) # n, m 을 공백으로 구분하여 입력 받기 
result = 0 
for i in range(n):
	data = list(map(int, input().split())
	min_value = min(data) # 현재줄에서 가장 작은 수 찾기 
	result = max(result, min_value) #' 가장 작은 수'들 중에서 가장 큰 수 찾기 
print(result) 

# py 2중 반복문 구조를 이용하는 답안 예시 
n, m = map(int, input().split()) # n, m 을 공백으로 구분하여 입력 받기 
result = 0 
for i in range(n):
	data = list(map(int, input().split())
	min_value = 10001
	for a in data: 
		min_value = min(min_value, a)  
	result = max(result, min_value) 
print(result) 