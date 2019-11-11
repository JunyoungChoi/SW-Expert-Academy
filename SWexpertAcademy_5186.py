T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
	N=float(input())
	cnt=0
	divNum=0.5
	result=""
	while N>0:
		if cnt>=13:
			break
		if N//divNum:
			result+='1'
			N-=divNum
		else :
			result+='0'
		cnt+=1
		divNum/=2
	if cnt>=13:
		print("#{} overflow".format(test_case))
	else:
		print("#{}".format(test_case),result)
