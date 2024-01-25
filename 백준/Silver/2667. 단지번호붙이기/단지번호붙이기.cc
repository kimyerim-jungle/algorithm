#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>
using namespace std;

struct pos {
	int x;
	int y;
	pos(int _x, int _y) {
		x = _x;
		y = _y;
	}
};

bool visited[25][25];
int graph[25][25];
queue<pos> q;

int num;
int nextX[4] = { -1, 1, 0, 0 };
int nextY[4] = { 0, 0, -1, 1 };

vector<int> home;
int Nhome = 0;

void bfs(int x, int y) {
	if (graph[x][y] == 0 || visited[x][y] == true)
		return;
	q.push(pos(x, y));
	visited[x][y] = true;
	Nhome = 0;

	while (!q.empty()) {
		pos p = q.front();
		q.pop();
		int curX = p.x;
		int curY = p.y;
		Nhome++;

		for (int i = 0; i < 4; i++) {
			int nx = curX + nextX[i];
			int ny = curY + nextY[i];

			if (nx < 0 || nx >= num || ny < 0 || ny >= num)
				continue;
			if (graph[nx][ny] == 0)
				continue;
			if (visited[nx][ny])
				continue;

			q.push(pos(nx, ny));
			visited[nx][ny] = true;
		}
	}
	home.push_back(Nhome);
}

int main() {

	cin >> num;

	string x;

	for (int i = 0; i < num; i++) { //입력
		cin >> x;
		for (int j = 0; j < num; j++) {
			char a = x[j];
			int b = a - '0';

			visited[i][j] = false;
			graph[i][j] = b;
		}
	}

	for (int i = 0; i < num; i++) {
		for (int j = 0; j < num; j++) {
			bfs(i, j);
		}
	}

	sort(home.begin(), home.end());

	int h = home.size();
	cout << h << endl;
	for (int i = 0; i < h; i++)
		cout << home[i] << endl;
}