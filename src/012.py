

def bfs(adj, src, dest, v, pred, dist): 
    queue = []
    visited = [False for _ in range(v)]
    for i in range(v):
        dist[i] = 100000
        pred[i] = -1

    visited[src] = True 
    dist[src] = 0 
    queue.append(src)

    while (len(queue) != 0): 
        u = queue[0]
        queue.pop(0)

        for i in range(len(adj[u])):
            if (visited[adj[u][i]] == False): 
                visited[adj[u][i]] = True 
                dist[adj[u][i]] = dist[u] + 1 
                pred[adj[u][i]] = u 
                queue.append(adj[u][i])

                if (adj[u][i] == dest): 
                    return True 

    return False 

def shortest_distance(adj, s, dest, v): 
    pred = [0 for _ in range(v)]
    dist = [0 for _ in range(v)]

    if not bfs(adj, s, dest, v, pred, dist): 
        #print("Destination not reachable")
        return dist[dest] 
    
    path = []
    crawl = dest 
    path.append(crawl)

    while pred[crawl] != -1: 
        path.append(pred[crawl])
        crawl = pred[crawl]
    
    """
    for i in range(len(path) - 1, -1, -1): 
        print(path[i], end=' ')
    """ 
    return dist[dest]


def main(): 
    with open("../inputs/012.txt", 'r') as fp: 
        data = [el.strip() for el in fp.readlines()]

    adjs = {}
    heights = 'abcdefghijklmnopqrstuvwxyz'
    start_idx = -1
    end_idx = -1

    for i, row in enumerate(data): 
        for j, el in enumerate(row):
            idx = i * len(row) + j 
            
            if el == 'S': 
                start_idx = idx 
            if el == 'E':
                end_idx = idx
    
    ndata = [] 
    for row in data: 
        row = row.replace('S', 'a')
        row = row.replace('E', 'z')
        ndata.append(row)
    
    a_idxs = []
    for i, row in enumerate(ndata): 
        for j, el in enumerate(row):
            idx = i * len(row) + j
            if el == 'a': 
                a_idxs.append(idx) 

    for i, row in enumerate(ndata): 
        for j, el in enumerate(row):
            idx = i * len(row) + j 
            adjs[idx] = []
            
            if el == 'S': 
                el = 'a'
                start_idx = idx 
            if el == 'E':
                el = 'z'
                end_idx = idx

            # up 
            if i - 1 >= 0: 
                up = ndata[i - 1][j]
                up_idx = (i - 1) * len(row) + j 
                if heights.index(up) <= heights.index(el) + 1: 
                    adjs[idx].append(up_idx) 
            # down 
            if i + 1 <= (len(ndata) - 1):
                down = ndata[i + 1][j] 
                down_idx = (i + 1) * len(row) + j
                if heights.index(down) <= heights.index(el) + 1:
                    adjs[idx].append(down_idx) 
            # left 
            if j - 1 >= 0:
                left = ndata[i][j - 1] 
                left_idx = i * len(row) + (j - 1)
                if heights.index(left) <= heights.index(el) + 1: 
                    adjs[idx].append(left_idx) 
            # right 
            if j + 1 <= (len(row) - 1): 
                right = ndata[i][j + 1] 
                right_idx = i * len(row) + (j + 1)
                if heights.index(right) <= heights.index(el) + 1: 
                    adjs[idx].append(right_idx)


    d = shortest_distance(adjs, start_idx, end_idx, len(adjs))
    print(f"Solution Part 1: {d}")
    
    path_lengths = []
    for idx in a_idxs: 
        dist = shortest_distance(adjs, idx, end_idx, len(adjs)) 
        path_lengths.append(dist)

    print(f"Solution Part 2: {min(path_lengths)}")


if __name__ == "__main__":
    main()