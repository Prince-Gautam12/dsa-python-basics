class AdjMatrix:
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



class AdjList:
    def __init__(self, connections, numberOfNodes, bidirectional, isWeighted= False):
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
            self.adjList[source].append([dest, weight])

            if bidirectional :
                if self.adjList[dest] == None:
                    self.adjList[dest] = []
                self.adjList[dest].append([source,weight])

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
        for list in self.adjList:
            print(list)



class GraphDemo:
    def demoAdjMatrix(self):
        print("========== UnWeighted =========")
        adjMatrix = AdjMatrix([[0,1],[1,3],[2,3],[3,4]], 5, False)
        print("============ Bidir =============")
        adjMatrixUni = AdjMatrix([[0,1],[1,3],[2,3],[3,4]], 5, True)

        print("========== Weighted =========")
        adjMatrix = AdjMatrix([[0,1,5],[1,3,6],[2,3,2],[3,4,8]], 5, False, True)
        print("============ BiDir =============")
        adjMatrix = AdjMatrix([[0,1,5],[1,3,6],[2,3,2],[3,4,8]], 5, True, True)
    
    def demoAdjList(self):
        print("========== UnWeighted =========")
        adjList = AdjList([[0,1],[1,3],[2,3],[3,4]], 5, False)
        print("============ BiDir =============")
        adjList = AdjList([[0,1],[1,3],[2,3],[3,4]], 5, True)
        print("========== Weighted =========")
        adjList = AdjList([[0,1,5],[1,3,6],[2,3,2],[3,4,8]], 5, False, True)
        print("============ BiDir =============")
        adjList = AdjList([[0,1,5],[1,3,6],[2,3,2],[3,4,8]], 5, True, True)

        print("====== Add new node=====")
        adjList.addNewNode()
        adjList.print()
        adjList.addPath(5, 3, 12)
        adjList.print()

graphDemo = GraphDemo()
graphDemo.demoAdjList()
