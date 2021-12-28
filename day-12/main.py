import sys
from pprint import pprint

class CaveNode:
    def __init__(self) -> None:
        self.edges = []
    def __init__(self, edge) -> None:
        self.edges = [edge]
    def __repr__(self) -> str:
        return f"{self.edges}, {self.visits} visits"
    def __str__(self) -> str:
        return f"{self.edges}, {self.visits} visits"

def bfs(graph, node, paths):
    queue = []
    visited = []

    queue.append(node)
    visited.append(node)

    pathstring = ""

    while queue:
        n = queue.pop()
        pathstring += f"{node}"
        for e in graph[n].edges:
            if e not in visited:
                if e == "end":
                    pathstring += ",end"
                    paths.append(pathstring)
                    continue
                pathstring += ","
                visited.append(e)
                queue.append(e)
    

if __name__ == "__main__":
    f = open(sys.argv[1])
    lines = f.readlines()
    f.close()

    graph = {}

    for i in range(0, len(lines)):
        nodes = lines[i].split("-")
        a = nodes[0].rstrip()
        b = nodes[1].rstrip()

        if a in graph.keys():
            graph[a].edges.append(b)
            if b in graph.keys():
                graph[b].edges.append(a)
            else:
                graph[b] = CaveNode(a)
        else:
            graph[a] = CaveNode(b)
            if b in graph.keys():
                graph[b].edges.append(a)
            else:
                graph[b] = CaveNode(a)

    pprint(graph, indent=4)

    paths = []
    #print(f"start has edges: {graph['start'].edges}")
    bfs(graph, "start", paths)

    pprint(paths, indent=4)