# 체스판은 (8,8) 나이트는 L 자 형태로 이동 
#1) 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기 
#2) 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기 

#나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램 작성하기 
#행위치 ( 1 ~ 8) , 열위치 (a ~ h) 

while True:

#현재 나이트의 위치 입력 받기 
  input_data = input()
  row = int(input_data[1])
  column = int(ord(input_data[0])) - int(ord('a')) + 1 

  #나이트가 이동할 수 있는 8가지 방향 정의  
  steps = [ (-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2) , (-2, 1) ]

  result = 0 
  for step in steps:
	#이동하고자 하는 위치 확인 
	  next_row = row + step[0]
	  next_column = column + step[1]
	  #해당 위치로 이동이 가능하다면 카운트 증가 
	  if next_row >= 1 and next_row <=8 and next_column >=1 and next_column <=8:
		  result += 1
  print(result) 