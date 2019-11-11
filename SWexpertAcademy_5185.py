T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N=input().split()
    result = '0'
    for i in N[1]:
        temp=bin(int(i,16))
        result+='0'*(6-len(temp))+temp[2:]
    print("#{}".format(test_case),result)
