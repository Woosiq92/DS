# N이 1일 될 때까지 둘 중 하나를 반복적으로 선택하여 수행하려고 한다. 
# N에서 1을 뺀다. / N을 K로 나눈다. 
# N 이 1이 되는 최소 횟수를 구하시오. 

#핵심 아이디어 => 최대한 나누기를 많이 수행하면 된다. 

n, k = map(int, input().split())
count = 0 

#N이 K 이상이라면 K로 계속 나누고 아니면 1빼기  

while n>= k:
	while n % k !=0:
		n -= 1 
		count += 1 
	n //= k
	count += 1 

#마지막으로 남은 수에 대하여 1씩 빼기 
while n > 1:
	n -= 1
	count += 1

print(count) 

#두번째 코드 

n, k = map(int, input().split())
count = 0 

#N이 K 이상이라면 K로 계속 나누고 아니면 1빼기  

while True:
	target = (n // k ) * k 
	count += ( n - target)
 	n = target 
	N이 K보다 더 작을 때( 더이상 나눌수 없을 때 반복문 탈출) 
	if n < k:
		break
	#k로 나누기 
	count += 1
	n //= k 

#마지막으로 남은 수에 대하여 1씩 빼기 
count += (n -1) 
print(count) 
