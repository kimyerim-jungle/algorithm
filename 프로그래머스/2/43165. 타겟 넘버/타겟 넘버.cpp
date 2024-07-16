#include <string>
#include <vector>

using namespace std;

int answer = 0;

void dfs(vector<int> numbers, int c, int t, int sum, bool plus){
    if(plus){
        sum += numbers[c++];
    }
    else{
        sum -= numbers[c++];
    }
    if(c >= numbers.size()){
        if(sum == t){
            answer++; return;
        }
        else{
            return;
        }
    }
    else{
        dfs(numbers, c, t, sum, true);
        dfs(numbers, c, t, sum, false);
    }
}

int solution(vector<int> numbers, int target) {
    int sum = 0;
    int count = 0;
    
    dfs(numbers, count, target, sum, true);
    dfs(numbers, count, target, sum, false);
    
    return answer;
}