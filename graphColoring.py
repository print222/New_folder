def insertEdge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)
    return graph

def greedyColoring(graph, v):
    colorArray = [-1] * v
    colorArray[0] = 0
    for u in range(1, v):
        temp = [False] * v
        for i in graph[u]:
            if colorArray[i] != -1:
                temp[colorArray[i]] = True
        j = 0
        while j < v:
            if not temp[j]:
                break
            j += 1
        colorArray[u] = j
    
    for i in range(v):
        print("Vertex:", i, "Color:", colorArray[i])

if __name__ == '__main__':
    num_vertices = 5
    g = [[] for _ in range(num_vertices)]
    g = insertEdge(g, 0, 1)
    g = insertEdge(g, 0, 2)
    g = insertEdge(g, 1, 2)
    g = insertEdge(g, 1, 3)
    g = insertEdge(g, 2, 3)
    g = insertEdge(g, 3, 4)
    print("The assigned colors of the graph are:")
    greedyColoring(g, num_vertices)
