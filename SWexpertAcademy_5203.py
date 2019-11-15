T = int(input())
def triplet(value):
	if 3 in value :
		return True
	else:
		return False

def run_(value):
	check=0
	for v in value:
		if v >=1:
			check+=1
		else:
			check=0
		if check >=3:
			return True
	return False
    
for test_case in range(1, T + 1):
	card=list(map(int,input().split()))
	p1={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0} 
	p2={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
	win1,win2=False,False
	answer=''
	for c in enumerate(card):
		if c[0] %2:
			p2[c[1]]+=1
		else :
			p1[c[1]]+=1
		win1=triplet(list(p1.values())) or run_(list(p1.values()))
		win2=triplet(list(p2.values())) or run_(list(p2.values()))
		if win1 and win2:
			answer="#%d %d"%(test_case,0)
			break
		elif win1 or win2:
			if win1:
				answer ="#%d %d"%(test_case,1)
			else:
				answer = "#%d %d"%(test_case,2)
			break
		else :
			answer="#%d %d"%(test_case,0)
	print(answer)
