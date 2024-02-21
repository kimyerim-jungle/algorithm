#include <stdio.h>

int main()
{
    int a, b;
    int N;
    
    scanf("%d", &N);
    
    for (int i=0; i<N; i++){
        scanf("%d %d", &a, &b);
        printf("%d\n", a+b);
    }
}