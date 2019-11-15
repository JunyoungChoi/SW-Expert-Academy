T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

def path_ (i,j,N,arr,path_sum):
	global sum
	if i>=N or j>=N:
		return
	elif i==N-1 and j==N-1:
		path_sum+=arr[i][j]
		if path_sum<sum:
			sum=path_sum
		return
	path_sum+=arr[i][j]
	path_(i+1,j,N,arr,path_sum)
	path_(i,j+1,N,arr,path_sum)
    
for test_case in range(1, T + 1):
	sum=float('inf')
	N=int(input())
	arr=[list(map(int,input().split())) for _ in range(N)]
	path_(0,0,N,arr,0)
	print("#{}".format(test_case), sum)
