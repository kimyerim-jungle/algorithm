#include <iostream>

using namespace std;

int main() {
    int kg;
    int dp[5001] = {0};
    
    cin >> kg;

    for (int i=0; i<=5000; i++){
        dp[i] = 5001;
    }

    dp[3] = 1;
    dp[5] = 1;

    for(int i=6; i<=kg; i++){
        if (dp[i-3] > dp[i-5]){
            dp[i] = dp[i-5] + 1;
        }
        else{
            dp[i] = dp[i-3] + 1;
        }
    }

    if (dp[kg] >= 5001)
        cout << -1;
    else
        cout << dp[kg] << endl;
}