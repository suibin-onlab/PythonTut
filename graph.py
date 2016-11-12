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
visitedb =[]
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

from collections import deque
q = deque()
def bfs(Graph, start = '', end = ''):

    while q and len(visitedb) < len(Graph) and end not in visitedb:
        #print "end: {}; visted: {}".format(end, end in visitedb)
        vertex = q.popleft()
        visitedb.append(vertex)

        ritem = ''
        for item in Graph[vertex]:
            if item not in visitedb and item not in q:
                q.append(item)
                ritem = item
        #print "Before iteration, visitedb: " + str(visitedb)
        #print "Before iteration, q: " + str(q)
        return bfs(Graph, start = ritem, end = end)
    return visitedb


def main():
    s = 'I'
    e = 'B'

    print "DFS: Path from {} to {}".format(s, e)
    stack.append(s)
    print dfs(Graph, start = s, end = e)

    print "\n"
    print "BFS: Path from {} to {}".format(s, e)
    q.append(s)
    print bfs(Graph, start = s, end = e)


if __name__ == '__main__':
    main()
