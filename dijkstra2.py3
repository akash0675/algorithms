import queue
G = []
D = []

def dijkstra(v):
  Q = queue.PriorityQueue()
  Q.put((D[v],v))
  while not Q.empty():
    (_,v) = Q.get()
    for u in G[v]:
      if D[v]+u[1] < D[u[0]]:
        D[u[0]] = D[v] + u[1]
        Q.put((D[u[0]],u[0]))

  for i in Q:
  	print(*Q[i])      

t = int(input())
for _ in range(t):
  n, m = list(map(int, input().split()))
  G = [[] for _ in range(n+1)]
  D = [10**10]*(n+1)
  for _ in range(m):
    x, y, c = list(map(int, input().split()))
    G[x].append((y,c))
    G[y].append((x,c))
  print(G)
  print(D)
  s = int(input())
  D[s] = 0
  dijkstra(s)
  res = list(D[1:s]+D[(s+1):])
  res = list(map(lambda x : x if x!=10**10 else -1, res))
  print(res)
  print(' '.join(list(map(str, res))))

