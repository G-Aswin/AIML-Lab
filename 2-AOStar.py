class Graph:
    def __init__(self, graph, heuristicNL, start):  
        
        self.graph = graph
        self.H=heuristicNL
        self.start=start
        self.parent={}
        self.status={}
        self.solutionGraph={}
     
    def applyAOStar(self):        
        self.aoStar(self.start, False)

    def printSolution(self):
        print("FOR GRAPH SOLUTION, TRAVERSE THE GRAPH FROM THE START NODE:",self.start)
        print("------------------------------------------------------------")
        print(self.solutionGraph)
        print("------------------------------------------------------------")
    
    def minChild(self, v):
        minimumCost=0
        mincostNL = []
        flag=True
        for neighbor in self.graph.get(v,''): 
            cost=0
            nodeList=[]
            for c, weight in neighbor:
                cost+=self.H.get(c, 0)+weight
                nodeList.append(c)
            
            if flag==True or minimumCost > cost:                     
                minimumCost=cost
                mincostNL=nodeList.copy()
                flag=False
              
        return minimumCost, mincostNL  
                     
    
    def aoStar(self, v, backTracking):  
        
        print("HEURISTIC VALUES  :", self.H)
        print("SOLUTION GRAPH    :", self.solutionGraph)
        print("PROCESSING NODE   :", v)
        print("-----------------------------------------------------------------------------------------")
        
        if self.getStatus(v) >= 0:    
            # update heuristic  
            minCost, childNL = self.minChild(v)
            self.H[v] = minCost
            self.status[v] = len(childNL)
            
            # Check for solved node
            solved=True                    
            for childNode in childNL:
                self.parent[childNode]=v
                if self.status.get(childNode, 0) != -1:
                    solved=False
            if solved==True:           
                self.status[v] = -1   
                self.solutionGraph[v]=childNL 
            
            # Backtrack
            if v!=self.start:          
                self.aoStar(self.parent[v], True) 
                
            # Forward movement
            if backTracking==False:   
                for childNode in childNL:  
                    self.status[childNode] = 0  
                    self.aoStar(childNode, False)
        
                                       
h1 = {'A': 1, 'B': 6, 'C': 2, 'D': 12, 'E': 2, 'F': 1, 'G': 5, 'H': 7, 'I': 7, 'J': 1, 'T': 3}
graph1 = {
    'A': [[('B', 1), ('C', 1)], [('D', 1)]],
    'B': [[('G', 1)], [('H', 1)]],
    'C': [[('J', 1)]],
    'D': [[('E', 1), ('F', 1)]],
    'G': [[('I', 1)]]  
}
G1= Graph(graph1, h1, 'A')
G1.applyAOStar() 
G1.printSolution()

# h2 = {'A': 1, 'B': 6, 'C': 12, 'D': 10, 'E': 4, 'F': 4, 'G': 5, 'H': 7}  
# graph2 = {                                        
#     'A': [[('B', 1), ('C', 1)], [('D', 1)]],     
#     'B': [[('G', 1)], [('H', 1)]],               
#     'D': [[('E', 1), ('F', 1)]]                  
# }

# G2 = Graph(graph2, h2, 'A')                     
# G2.applyAOStar()                                
# G2.printSolution()                              