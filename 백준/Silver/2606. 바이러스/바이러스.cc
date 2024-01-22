#include <iostream>
#include <vector>
using namespace std;

bool visited[101];
vector<int> graph[101];
int virus = 0;

void dfs(int n) {
    visited[n] = true; // 방문한 노드 체크
    for (int i = 0; i < graph[n].size(); i++) {
        int x = graph[n][i];
        if (!visited[x]) { //새로 접근한 노드가 방문하지 않은 경우
            dfs(x); virus++;
        }
    }
}

int main() {
    int computer;
    int node;
    int num1, num2;

    cin >> computer;
    cin >> node;

    for (int i = 1; i <= node; i++) {
        cin >> num1 >> num2;

        graph[num1].push_back(num2);
        graph[num2].push_back(num1);
    }

    dfs(1);

    cout << virus;
}