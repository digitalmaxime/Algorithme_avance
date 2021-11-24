graph = { 0 : [1, 2],
          1 : [3, 6, 0],
          2 : [4, 5, 0],
          3 : [1],
          4 : [6, 2, 7],
          5 : [6, 2],
          6 : [1, 4, 5],
          7: [4]}


def findAllPaths(graph, v):
    """Generate the maximal cycle-free paths in graph starting at v.
    graph must be a mapping from vertices to collections of
    neighbouring vertices.
    """
    path = [v]                  # path traversed so far
    seen = {v}                  # set of vertices in path
    def search():
        dead_end = True
        for neighbour in graph[path[-1]]:
            if neighbour not in seen:
                dead_end = False
                seen.add(neighbour)
                path.append(neighbour)
                yield from search()
                path.pop()
                seen.remove(neighbour)
        if dead_end and len(path) == len(graph):
            print(path)
            yield list(path)
    yield from search()


if __name__ == '__main__':
    allPaths = []
    for vertice in graph: 
        result = sorted(findAllPaths(graph, vertice))
        for path in result:
            allPaths.append(path)
        

