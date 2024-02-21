#include <stdio.h>

int main(){
    int num[100] = {0};
    int N, a;
    int c = 0, sum = 0;

    scanf("%d", &N);

    for (int i=0; i < N; i++){
        scanf("%d", &a);

        if (a == 1)
            c++;
        else if (a == 0)
            c = 0;
    
        num[i] = c;
    }

    for (int i=0; i<N; i++){
        sum += num[i];
    }
    printf("%d", sum);

    return 0;
}