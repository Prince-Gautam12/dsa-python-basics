class AdjMatrixGraph:
    def __init__(self, connections, numberOfNodes, bidirectional, weighted = False) -> None:
        self.adj = [[0]*numberOfNodes for _ in range(numberOfNodes)]

        for connection in connections:
            source = connection[0]
            dest = connection[1]
            if weighted :
                weight = connection[2]
            else :
                weight = 1

            self.adj[source][dest] = weight
            if bidirectional:
                self.adj[dest][source] = weight
        
        for list in self.adj:
            print(list)



class AdjListGraph:
    def __init__(self, connections, numberOfNodes, bidirectional, isWeighted = False):
        self.bidirectional = bidirectional
        self.isWeighted = isWeighted
        self.adjList = [None]*numberOfNodes
        for connection in connections:
            source = connection[0]
            dest = connection[1]
            if isWeighted:
                weight = connection[2]
            else :
                weight = 1

            if self.adjList[source] == None:
                self.adjList[source] = []
            
            if isWeighted:
                self.adjList[source].append([dest, weight])
            else :
                self.adjList[source].append(dest)

            if bidirectional :
                if self.adjList[dest] == None:
                    self.adjList[dest] = []
                if isWeighted:
                    self.adjList[dest].append([source,weight])
                else :
                    self.adjList[dest].append(source)

    def addNewNode(self):
        self.adjList.append(None)
        

    def addPath(self, source, dest, weight = 1):
        if self.adjList[source] == None:
            self.adjList[source] = []
        self.adjList[source].append([dest,weight])

        if self.bidirectional:
            if self.adjList[dest] == None:
                self.adjList[dest] = []
            self.adjList[dest].append([source,weight])

    def print(self):
        i = 0
        for list in self.adjList:
            print(f'{i}-> {list}')
            i+=1



class GraphDemo:
    def demoAdjMatrix(self):
        print("========== UnWeighted =========")
        adjMatrix = AdjMatrixGraph([[0,1],[1,3],[2,3],[3,4]], 5, False)
        print("============ Bidir =============")
        adjMatrixUni = AdjMatrixGraph([[0,1],[1,3],[2,3],[3,4]], 5, True)

        print("========== Weighted =========")
        adjMatrix = AdjMatrixGraph([[0,1,5],[1,3,6],[2,3,2],[3,4,8]], 5, False, True)
        print("============ BiDir =============")
        adjMatrix = AdjMatrixGraph([[0,1,5],[1,3,6],[2,3,2],[3,4,8]], 5, True, True)
    
    def demoAdjList(self):
        print("========== UnWeighted =========")
        adjList = AdjListGraph([[0,1],[0,3],[1,3],[2,3],[3,4]], 5, True)
        adjList.print()
        print("============ BiDir =============")
        adjList = AdjListGraph([[0,1],[1,3],[2,3],[3,4]], 5, True)
        print("========== Weighted =========")
        adjList = AdjListGraph([[0,1,5],[1,3,6],[2,3,2],[3,4,8]], 5, False, True)
        print("============ BiDir =============")
        adjList = AdjListGraph([[0,1,5],[1,3,6],[2,3,2],[3,4,8]], 5, True, True)

        print("====== Add new node=====")
        adjList.addNewNode()
        adjList.print()
        adjList.addPath(5, 3, 12)
        adjList.print()

graphDemo = GraphDemo()
# graphDemo.demoAdjList()
