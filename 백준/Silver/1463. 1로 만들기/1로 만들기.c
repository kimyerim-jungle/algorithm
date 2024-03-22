#include <stdio.h>

int one(int n);
int min(int a, int b);

static int dp[1000005];

int main()
{
    int N;
    scanf("%d", &N);

    for (int i = 0; i < 1000005; i++)
    {
        dp[i] = -1;
    }

    printf("%d", one(N));
}

int one(int n)
{
    if (dp[n] != -1)
        return dp[n];

    if (n == 1)
        return 0;

    dp[n] = 1 + one(n - 1);

    if (n % 3 == 0)
        dp[n] = min(dp[n], 1 + one(n / 3));
    if (n % 2 == 0)
        dp[n] = min(dp[n], 1 + one(n / 2));

    return dp[n];
}

int min(int a, int b)
{
    if (a > b)
        return b;
    else
        return a;
}