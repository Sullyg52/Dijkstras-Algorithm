from calendar import c


class edge:
    def __init__(self, v1, v2, weight) -> None:
        self.v1 = v1
        self.v2 = v2
        self.weight = weight

class vertex:
    edges = []
    adj_vertices = []
    def __init__(self) -> None:
        pass
    def add_edge(self, edge):
        self.edges.append(edge)
        if (edge.v1 == self):
            self.adj_vertices.append(edge.v2)
        else:
            self.adj_vertices.append(edge.v1)

def dijkstra(v_names, adj_matrix, source, dest = None):
    dist = {}
    paths = {}
    done = [source]
    num_vert = len(v_names)
    for v in v_names:
        dist[v] = -1
        paths[v] = [source]
    dist[source] = 0
    curr_vert = source
    while (len(done) < num_vert):
        next_vert = -1
        adjacent_weights = adj_matrix[v_names.index(curr_vert)]
        for i in range(num_vert):
            v = v_names[i]
            if v not in done:
                weight = adjacent_weights[i]
                if weight != 0:
                    adj_dist = dist[curr_vert] + weight
                    if dist[v] == -1 or adj_dist < dist[v]:
                        dist[v] = adj_dist
                        paths[v] = paths[curr_vert] + [v]
                    if next_vert == -1 or adj_dist < dist[next_vert]:
                        next_vert = v
                elif dist[v] != -1 and (next_vert == -1 or dist[v] < dist[next_vert]):
                    next_vert = v
        done.append(next_vert)
        curr_vert = next_vert

    if dest == None:
        print('Shortest paths:', paths)
        print('Distances:', dist)
    else:
        print('Shortest path:', paths[dest])
        print('Distance:', dist[dest])

vertex_names = ['clt', 'nyc', 'lax', 'dal', 'mia']
matrix = [[0, 3, 0, 7, 8],
          [3, 0, 1, 4, 0],
          [0, 1, 0, 2, 0],
          [7, 4, 2, 0, 3],
          [8, 0, 0, 3, 0]]
dijkstra(vertex_names, matrix, 'clt', 'dal')
            

        


