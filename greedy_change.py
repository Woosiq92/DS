## 카운터에는 거스름돈으로 500, 100, 50, 10원 짜리 동전이 무한히 존재한다. 
## 손님에게 거슬러줘야 할 동전의 최소 개수를 구하라. 
## 단 거슬러 줘야 할 돈 N은 항상 10의 배수이다. 

n = 1260 
count = 0 

coin_types = [500, 100, 50, 10] 

for coin in coin_types:
	count += n // coin # 몫구하기 
	n %= coin 
print(count) 