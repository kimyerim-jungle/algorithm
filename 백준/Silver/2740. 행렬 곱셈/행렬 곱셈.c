#include <stdio.h>
#include <stdlib.h>

int main(){
    int N, M, K, a, sum=0;
    int **result;
    int **arr1, **arr2;

    scanf("%d %d", &N, &M);
    arr1 = (int **)malloc(N*sizeof(int *));
    arr2 = (int **)malloc(M*sizeof(int *));
    result = (int **)malloc(N*sizeof(int *));

    for(int i=0; i<N; i++){
        arr1[i] = (int *)malloc(M*sizeof(int));
        for (int j=0; j<M; j++){
            scanf("%d", &a);
            arr1[i][j] = a;
        }
    }

    scanf("%d %d", &M, &K);
    
    for(int i=0; i<N; i++)
        result[i] = (int *)calloc(K, sizeof(int));

    for(int i=0; i<M; i++){
        arr2[i] = (int *)malloc(K*sizeof(int));

        for (int j=0; j<K; j++){
            scanf("%d", &a);
            arr2[i][j] = a;
        }
    }

    for(int i=0; i<N; i++){
        for (int j=0; j<K; j++){
            for(int k=0; k<M; k++){
                sum += arr1[i][k] * arr2[k][j];
            }
            result[i][j] = sum;
            sum = 0;
        }   
    }
    for(int i=0; i<N; i++){
        for(int j=0; j<K; j++)
            printf("%d ", result[i][j]);
        printf("\n");
    }
}