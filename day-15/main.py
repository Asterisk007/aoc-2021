import sys
from dijkstar import Graph, find_path

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("Need input file.")
    
    f = open(sys.argv[1])
    lines = f.readlines()
    f.close()
    graph = Graph()

    u, v = 0, 0
    for i in range(len(lines)):
        if i+1 < len(lines):
            line = lines[i].rstrip()
            line2 = lines[i+1].rstrip()
            gl = [int(x) for x in line]
            gl2 = [int(x) for x in line2]
            for j in range(len(gl)):
                v = len(gl)-1+u
                if j+1 < len(gl)-1:
                    graph.add_edge(u, u+1, gl[j+1])
                if j > 0:
                    graph.add_edge(u, u-1, gl[j-1])
                graph.add_edge(u, v, gl2[j])
                graph.add_edge(v, u, gl[j])
                u += 1
    start = 0
    end = v
    path = find_path(graph, start, end)
    print(path)
