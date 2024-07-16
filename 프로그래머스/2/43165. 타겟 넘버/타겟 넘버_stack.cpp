#include <string>
#include <vector>
#include <stack>
#include <tuple>

using namespace std;

int solution(vector<int> numbers, int target) {
    int answer = 0;
    tuple<int, int> tup;
    stack<tuple<int, int>> st;
    int index, sum;
    
    tup = make_tuple(-1, 0);
    st.push(tup);
    while (!st.empty()){
        tuple<int, int> tp = st.top();
        tie(index, sum) = tp;
        st.pop();
        
        if(index+1 < numbers.size()){
            tup = make_tuple(index+1, sum+numbers[index+1]);
            st.push(tup);
            tup = make_tuple(index+1, sum-numbers[index+1]);
            st.push(tup);
        }
        else if(index+1 == numbers.size()){
            if(sum == target)
                answer++;
        }
    }
    
    return answer;
}
