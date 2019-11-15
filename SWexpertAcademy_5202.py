T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
	N= int(input())
	truck=[]
	result=0
	e=0
	for n in range(N):
		truck.append(list(map(int,input().split())))
	truck.sort(key=lambda x:x[1])
	for t in truck:
		if t[0]>=e:
			result+=1
			e=t[1]
	print("#%d %d"%(test_case,result))
