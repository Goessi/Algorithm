BFS Breadth First Search
广度优先可以找出是否有A到B的路径已经A到B的最短路径，指的是段数最少。适用于非加权图。
队列是先进先出的，而栈是后进后出的
所以搜索列表必须是队列

Dijkstra algorithm
在迪克斯特拉算法中，可以找出A到B的最短路径，指的是总权重最小。适用于加权无环图且图中没有负权重。

Bellman-ford algorithm
适用于有负权重的图

def shortest_path(M,start,goal):
    open_nodes = {}
    closed_nodes = []
    open_g = {}
    open_h = {}
    L = []
    father_node = {}
    
    # initialization
    L.append(start)    
    keys = M.intersections.keys()
    for k in keys:
        open_h[k] = distance(M,k,goal)
    closed_nodes.append(start)
    connected_nodes = M.roads[start]
    for node in connected_nodes:
        open_g[node] = distance(M,start,node) #G
        open_nodes[node] = open_g[node] + open_h[node] #F
        father_node[node] = start
    
    # while loop
    while open_nodes:
        node = min(open_nodes, key=lambda x: open_nodes[x])
        
        # while we catch goal
        if node == goal:
            # delete in open
            del open_nodes[node]
            closed_nodes.append(node)
            break
        
        #while we don't catch goal
        connected_nodes = M.roads[node]
        for x in connected_nodes:
            if x in open_nodes.keys():
                new_f =  open_g[node] + distance(M,node,x) + open_h[x]
                if new_f < open_nodes[x]:
                    open_nodes[x] = new_f
                    open_g[x] = open_g[node] + distance(M,node,x)
                    father_node[x] = node
            if x in closed_nodes:
                continue
            if x not in open_nodes.keys() and x not in closed_nodes:
                father_node[x] = node
                open_nodes[x] = open_g[node] + distance(M,node,x) + distance(M,x,goal)
                open_g[x] = open_g[node] + distance(M,node,x)
        del open_nodes[node]
        closed_nodes.append(node)
    
    haha = find_way(father_node,start,goal)   
    print("shortest path called")
    print(haha)
    return haha

# calculate distance between start and connected,G
# calculate distance between connected and distination,H
# calculate F,choose smallest one
# set this one to father point, recalculate G&F
# choose smallest one

def distance(M,p1,p2):
    x1 = M.intersections[p1][0]
    y1 = M.intersections[p1][1]
    x2 = M.intersections[p2][0]
    y2 = M.intersections[p2][1]
    dis = ((x1-x2)**2+(y1-y2)**2)**0.5
    return dis
def find_way(D,start,goal):
    reverse_way = []
    reverse_way.append(goal)
    if start != goal:
        father = D[goal]       
        while father != start:
            reverse_way.append(father)
            father = D[father]
        reverse_way.append(start)
    return reverse_way[::-1]
