#include <stdio.h>

int ott(int n);

static int dp[20];

int main()
{
    int N, T;
    scanf("%d", &T);

    for (int i = 0; i < 20; i++)
    {
        dp[i] = -1;
    }

    for (int i = 0; i < T; i++)
    {
        scanf("%d", &N);
        printf("%d\n", ott(N));
    }
}

int ott(int n)
{
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 4;

    for (int i = 4; i <= n; i++)
    {
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
    }

    return dp[n];
}