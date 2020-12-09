#다양한 수로 이루어진 배열이 있을 때, 주어진 수들을 M 번 더하여 가장 큰 수를 만드는 법칙
#단, 특정 인덱스에 해당하는 수가 연속으로 K번을 초과하여 더해질 수 없다. 

#N, M, K를 공백으로 구분하여 입력받기 

n, m, k = map(int, input().split()) 

#N개의 수를 공백으로 구분하여 입력받기  
data = list(map(int, input().split()))

data.sort()
first = data[n-1] # 가장 큰수 
second = data[n-2] # 두 번째로 큰수 

# 가장 큰수가 더해지는 횟수 계산
count = int(m/(k+1))*k # 가장 큰 수가 등장하는 횟수
count += m %(k+1)  # (K+1) = 반복되는 수열의 길이 (k - 첫번째로 큰수 , 1 - 두번째로 큰수)

result = 0 
result +=(count) * first # 가장 큰 수 더하기 
result += (m - count) * second # 두번째로 큰 수 더하기 

print(result) #최종답안 출력 