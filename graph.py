#!/usr/bin/python
Graph = {
    'A': set(['B', 'F', 'D']),
    'B': set(['A', 'C']),
    'C': set(['B','F', 'G', 'H']),
    'D': set(['A', 'F', 'E']),
    'E': set(['D', 'G', 'I']),
    'F': set(['A', 'C', 'D', 'G']),
    'G': set(['E', 'F', 'C']),
    'H': set(['C', 'I']),
    'I': set(['E', 'H'])
}
visitedd, stack = [], []

def dfs(Graph, start = '', end = ''):
    while stack and len(visitedd) < len(Graph) and end not in visitedd:
        vertex = stack.pop()
        visitedd.append(vertex)

        for item in Graph[vertex]:
            if item not in visitedd:
                stack.append(item)
                #print "Before recursion, stack is: " + str(stack)
                #print "Before Recursion, visitedd is: " + str(visitedd)
                return dfs(Graph, start = item, end = end)

    return visitedd


# def bfs(Graph, start = '', end = ''):
#     path = []
#
#     while q and len(visitedb) < len(Graph) and end not in path:
#         #print "end: {}; visted: {}".format(end, end in visitedb)
#         vertex = q.popleft()
#         visitedb.append(vertex)
#         path.append(vertex)
#
#         ritem = ''
#         for item in Graph[vertex]:
#             if item not in visitedb and item not in q:
#                 q.append(item)
#                 ritem = item
#         print "Before iteration, visitedb: " + str(visitedb)
#         print "Before iteration, q: " + str(q)
#         return bfs(Graph, start = ritem, end = end)
#     return visitedb

def bfs(Graph, start = '', end = ''):
    queue = [[start]]
    visitedb = []

    while queue:
        path = queue.pop(0)
        vertex = path[-1]

        if vertex == end:
            return path
        elif vertex not in visitedb:
            for neighbour in Graph.get(vertex, []):
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
            visitedb.append(vertex)
            #print "Before iteration, path: " + str(path)
            #print "Before interation, queue: " + str(queue)
    return visitedb

def main():
    s = 'A'
    e = 'H'

    print "DFS: Path from {} to {}".format(s, e)
    stack.append(s)
    print dfs(Graph, start = s, end = e)

    print "\n"
    print "BFS: Path from {} to {}".format(s, e)
    print bfs(Graph, start = s, end = e)


if __name__ == '__main__':
    main()
