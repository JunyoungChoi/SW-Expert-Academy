#include <stdio.h>
#include<malloc.h>
int my_mult(int x);
int solve(int num, int arr[]);
int main(void)
{
	int test_case;
	int T;
	scanf("%d", &T);
	for (test_case = 1; test_case <= T; ++test_case)
	{

		int k;
		scanf("%d", &k);
		int tem = my_mult(k);
		int tem2 = 0;
		int *A = (int *)malloc(sizeof(int)*tem);
		for (int t = 0; t<tem; t++) {
			scanf("%d", &A[t]);

		}

		printf("#%d %d\n", test_case, solve(tem, &A[0]));
		free(A);
	}
	return 0; //정상종료시 반드시 0을 리턴해야 합니다.
}
int solve(int num, int arr[]) {
	if (num == 1) {
		return 0;
	}
	int *next_arr = (int*)malloc(sizeof(int)*num / 2);
	int sum = 0;
	for (int i = 0; i<num; i += 2) {
		if (arr[i] >= arr[i + 1]) {
			sum += arr[i] - arr[i + 1];
			next_arr[i / 2] = arr[i];

		}
		else {
			sum += arr[i + 1] - arr[i];
			next_arr[i / 2] = arr[i + 1];
		}
	}
	return sum + solve(num / 2, next_arr);
}
int my_mult(int x) {
	int ans = 1;
	for (int i = 0; i<x; i++) {
		ans *= 2;
	}
	return ans;
}