import queue

def dijkstra(s):
	Q = queue.PriorityQueue()
	Q.put((D[s], s))
	while not Q.empty():
		(_,s) = Q.get()
		for u in G[s]:
			if D[s] + u[1] < D[u[0]]:
				D[u[0]] = D[s] + u[1]
				Q.put((D[u[0]], u[0]))

G = []
D = []
t = int(input())
for i in range(t):
	n, m = input().split()
	n, m = int(n), int(m)
	G = [[] for i in range(n+1)]
	D = [10 ** 10] * (n + 1)
	for i in range(m):
		x, y, c = input().split()
		x, y, c = int(x), int(y), int(c)
		G[x].append((y, c))
		G[y].append((x, c))
	
	s = int(input())	
	D[s] = 0
	dijkstra(s)
	res = list(D[1:s] + D[(s + 1):])
	res = list(map(lambda x : x if x != 10 ** 10 else -1, res))
	print(*res)