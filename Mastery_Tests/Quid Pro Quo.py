# def trade(trade_to_char_i, receive_from_char_i, char_num):
#     print(surp, need)
#     h[trade_to_char_i] -= 1
#     r[trade_to_char_i][char_num] += 1
#     h[receive_from_char_i] += 1
#     r[receive_from_char_i][char_num] -=1
#     new_need = [i for i in need if i != receive_from_char_i]
#     print(trade_to_char_i, h[trade_to_char_i])
#     if h[trade_to_char_i] == 1:
#         new_surp = [i for i in surp if h[i] > 1]
#         print("wtf")
#         print("new surp:", new_surp, "new need:", new_need)
#         return (new_surp, new_need)
#     else:
#         return (surp, new_need)


# def trade_check():
#     global surp 
#     global need

#     traded = False

#     while need:
#         for i in range(n):
#             for j in range(m):
#                 for k in range(len(surp)):
#                     for l in range(len(need)):
#                         print("l", l)
#                         print(need)
#                         print("need[l]:", need[l])
#                         print("j:", j)
#                         if h[surp[k]] > 1 and w[surp[k]][j] > r[surp[k]][j] and w[need[l]][j] < r[need[l]][j]:
#                             (surp, need) = trade(surp[k], need[l], j)
#                             traded = True
#                             if not need:
#                                 return True

#         if not traded:
#             break


#     for i in h:
#         if i < 1:
#             return False

#     return True


# r = [
#     [1,  0, 0],
#     [0, 10, 0],
#     [1,  0, 0],
#     [0,  0, 1],
# ]

# w = [
#     [3,  0, 0],
#     [0,  0, 0],
#     [0, 20, 1],
#     [0,  0, 0],
# ]

# h = [15, 1, 2, 0]

# r = [
#     [1,  0,  0, 0],
#     [0, 10,  0, 0],
#     [1,  0,  0, 0],
#     [0,  0,  1, 0],
#     [0,  1,  0, 0],
#     [0,  0,  0, 1]
# ]

# w = [
#     [3,  0,  0, 0],
#     [0,  0,  0, 0],
#     [0, 20,  1, 0],
#     [0,  0,  0, 0],
#     [0,  0,  0, 1],
#     [0,  0,  0, 0]
# ]

# h = [15, 1, 0, 0, 2, 1]

# n = len(r)

# m = len(r[0])

# print(n,m)

# need = [i for i, v in enumerate(h) if v < 1]
# surp = [i for i, v in enumerate(h) if v > 1]

# print(f"Surplus: {surp}, Need: {need}")


# print(trade_check())


# Transpose inputs r and w 
# r1 = [[r[j][i] for i in range(len(r))] for j in range(len(r[0]))]
# w1 = [[w[j][i] for i in range(len(w))] for j in range(len(w[0]))]

# print(r1, w1)

# r1c = r1[:]
# w2c = w1[:]

# while not Flag:
#     for i in h:
#         for j in range(r1c):
#             need_jk = [i for i, v in enumerate(w1) if v < 1]
#             for k in range(r1c[0]):

#                 if i in need:


# sources = [i for i in h if i>1] 
# sinks = [j for j in h if j<=1]l

# ---------------------------------------------------------------------------------------

# This class represents a directed graph
# using adjacency matrix representation
class Graph:

    def __init__(self, graph):
        self.graph = graph  # residual graph
        self.ROW = len(graph)
        # self.COL = len(gr[0])

    '''Returns true if there is a path from source 's' to sink 't' in
    residual graph. Also fills parent[] to store the path '''

    def BFS(self, s, t, parent):

        # Mark all the vertices as not visited
        visited = [False] * self.ROW

        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        # Standard BFS Loop
        while queue:

            # Dequeue a vertex from queue and print it
            u = queue.pop(0)

            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    # If we find a connection to the sink node,
                    # then there is no point in BFS anymore
                    # We just have to set its parent and can return true
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True

        # We didn't reach sink in BFS starting 
        # from source, so return false
        return False

    # Returns the maximum flow from s to t in the given graph
    def FordFulkerson(self, source, sink):

        # This array is filled by BFS and to store path
        parent = [-1] * self.ROW

        max_flow = 0  # There is no flow initially

        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent):

            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Add path flow to overall flow
            max_flow += path_flow

            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


def resource_trade(h, w, r):
    n = len(r)
    m = len(r[0])

    vertices = 2 + n + m

    graph = [[0 for _ in range(vertices)] for _ in range(vertices)]
    # graph[0] = [0] + h + [0] * (vertices - n - 1)
    for i in range(1, n + 1):
        graph[0][i] = h[i-1]
    for i in range(1, n + 1):
        graph[i][vertices - 1] = 1

    for i in range(n):
        for j in range(m):
            capacity = w[i][j] - r[i][j]
            if capacity != 0:
                if capacity > 0:
                    graph[i + 1][j + n + 1] = capacity
                else:
                    graph[j + n + 1][i + 1] = -capacity

    g = Graph(graph)

    source = 0
    sink = 8
    max_flow = g.FordFulkerson(source, sink)

    return max_flow == n, max_flow
    # print(f"Is this trade possible for this input(True/False)? {max_flow == n}; Max Flow: {max_flow} ")


r = [
    [1, 0, 0],
    [0, 10, 0],
    [1, 0, 0],
    [0, 0, 1],
]

w = [
    [3, 0, 0],
    [0, 0, 0],
    [0, 20, 1],
    [0, 0, 0],
]

h = [15, 1, 1, 0]

print(resource_trade(h, w, r))


# graph = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
# ]

# graph1 = [
#     [0, 15, 1, 1, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 2, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0, 20, 1, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 1, 0, 0, 0, 0, 0],
#     [0, 0, 10, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 1, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
# ]

# print(graph == graph1)
# print(graph)
# print(graph1)
