def getAdjList(numberOfNodes, connections):
    adjList = [None]*(numberOfNodes + 1)
    for connection in connections:
        source = connection[0]
        dest = connection[1]
        if adjList[source] == None:
            adjList[source] = []
        adjList[source].append(dest)
    return adjList
