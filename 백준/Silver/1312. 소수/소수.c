#include <stdio.h>
#include <math.h>

int main(){
    int A, B, N;
    int pre;

    scanf("%d %d %d", &A, &B, &N);

    while(1){
        pre = A/B;
        A = A%B;
        if(A == 0){
            printf("0");
            return 0;
        }
        if(A<B) {
            for(int i=0; i<N; i++){
                if (A<B){
                    A *= 10;
                }
                pre = A/B;
                A = A%B;

                if(A == 0 && i<N-1){
                    printf("0");
                    return 0;
                }
            }
            printf("%d", pre);
            return 0;
        }
    }
}