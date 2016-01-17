#include <iostream>
#include <cstdio>
#include <map>
#include <climits>

#define INF INT_MAX

using namespace std;

void floyd(map<int, map<int, int> > graph, int N){
	map<int, map<int, int> > dist;
	for(int i = 1; i <= N; ++i){
		for(int j = 1; j <= N; ++j)
			dist[i][j] = graph[i][j];
	}

	for(int k  = 1; k <= N; ++k){
		for(int i = 1; i <= N; ++i){
			for(int j = 1; j <= N; ++j){
				if(((dist[i][k] + dist[k][j]) < dist[i][j]) && dist[i][k] != INF && dist[k][j] != INF)
					dist[i][j] = dist[i][k] + dist[k][j];
			}
		}
	}

	for(int i = 1; i <= N; ++i){
		for(int j = 1; j <= N; ++j)
			cout << graph[i][j] << "  ";
		cout << endl;
	}

}

int main(){
	int N, M;
	cin >> N >> M;
	map<int, map<int, int> > graph;
	for(int i = 1; i <= N; ++i){
		for(int j = 1; j <= N; ++j)
			graph[i][j] = INF;
	}

	while(M--){
		int X, Y, C;
		scanf("%d %d %d", &X, &Y, &C);
		graph[X][Y] = C;
	}

	for(int i = 1; i <= N; ++i)
		graph[i][i] = 0;

	cout << "size: " << graph.size();

	for(int i = 1; i <= N; ++i){
		for(int j = 1; j <= N; ++j)
			cout << graph[i][j] << "  ";
		cout << endl;
	}

	floyd(graph, N);

	/*int t;
	cin >> t;
	while(t--){
		int a, b;
		cin >> a >> b;
		if(dist[a][b] ==  INF)
			cout << -1 << endl;
		else
			cout << dist[a][b] << endl;
	}*/
	return 0;
}