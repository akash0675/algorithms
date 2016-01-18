import  queue
def bfs(graph,s,v,path):
    q=queue.Queue()
    q.put(s)
    v[s]=1
    while q.empty()==False:
        j=q.get()
        for i in graph[j]:
            if(v[i]==0):
                v[i]=1
                path[i]=path[j]+6
                q.put(i)

def main():
    for i in range(int(input())):
        n,e=input().split()
        n,e=int(n),int(e)
        graph=[]
        for k in range(n):
            graph.append([])

        for j in range(e):
            a,b=input().split()
            a,b=int(a),int(b)
            graph[a-1].append(b-1)
            graph[b-1].append(a-1)

        s=int(input())

        v=[0]*n
        path=[0]*n
        bfs(graph,s-1,v,path)
        o=""
        for x in range(len(path)):
            if(x==s-1):
                continue
            if(path[x]==0):
                o+=str(-1)+" "
            else:
                o+=str(path[x])+" "
        print(o)
        
main()        