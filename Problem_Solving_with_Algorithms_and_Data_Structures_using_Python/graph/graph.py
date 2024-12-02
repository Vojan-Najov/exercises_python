#run --> PYTHONPATH = $PYTHONPATH:queue python3 graph/graph.py

from queue import Queue

class Vertex:

    def __init__(self, key):
        self.id = key
        self.distance = 0
        self.pred = None
        self.color = 'white'
        self.connectedTo = {}
        self.discovery = 0
        self.finish = 0

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return f'{self.id} connectedTo: {self.connectedTo.keys()}'

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo(nbr)

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getDistance(self):
        return self.distance

    def setDistance(self, dst):
        self.distance = dst

    def getPred(self):
        return self.pred

    def setPred(self, pred):
        self.pred = pred

    def getDiscovery(self):
        return self.discovery

    def setDiscovery(self, dsc):
        self.discovery = dsc

    def getFinish(self):
        return self.finish

    def setFinish(self, fnsh):
        self.finish = fnsh


class Graph:
    
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        return self.vertList.get(n, None)

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while vertQueue.size() > 0:
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if nbr.getColor() == 'white':
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')


def traverse(y):
    x = y
    while x.getPred():
        print(x.getId())
        x = x.getPred()
    print(x.getId())


class DFSGraph(Graph):

    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)

    def dfsVisit(self, startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)


def main():
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    g.vertList
#   {0: <adjGraph.Vertex instance at 0x41e18>,
#    1: <adjGraph.Vertex instance at 0x7f2b0>,
#    2: <adjGraph.Vertex instance at 0x7f288>,
#    3: <adjGraph.Vertex instance at 0x7f350>,
#    4: <adjGraph.Vertex instance at 0x7f328>,
#    5: <adjGraph.Vertex instance at 0x7f300>}
    g.addEdge(0,1,5)
    g.addEdge(0,5,2)
    g.addEdge(1,2,4)
    g.addEdge(2,3,9)
    g.addEdge(3,4,7)
    g.addEdge(3,5,3)
    g.addEdge(4,0,1)
    g.addEdge(5,4,8)
    g.addEdge(5,2,1)
    for v in g:
        for w in v.getConnections():
            print("( %s , %s )" % (v.getId(), w.getId()))

#   ( 0 , 5 )
#   ( 0 , 1 )
#   ( 1 , 2 )
#   ( 2 , 3 )
#   ( 3 , 4 )
#   ( 3 , 5 )
#   ( 4 , 0 )
#   ( 5 , 4 )
#   ( 5 , 2 )


if __name__ == '__main__':
    main()
