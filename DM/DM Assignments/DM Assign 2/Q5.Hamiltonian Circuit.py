#program to check Hamiltonian circuit

#class to create graph/adjacency list
class Graph:
    def __init__(self,nodes):
        self.nodes=nodes            #list conating all vertex
        self.adj_List=dict()        #dict/ adjacency list

        for vertex in nodes:    
            self.adj_List[vertex]=list()
    
    #adding edge to verties
    def addEdge(self,vertex,edges):

        #irritating in enges
        for edge in edges:

            #when eged is not present in vertex list
            if edge not in self.adj_List[vertex]:
                self.adj_List[vertex].append(edge)

            #when edge is not present vertex list
            if vertex not in self.adj_List[edge]:
                self.adj_List[edge].append(vertex)

        return self.adj_List    #return Adjacency list

    def printGraph(self):
        print('\nVertex\t:\tEdeges')
        for vertex,edge in self.adj_List.items():
            print(vertex,'\t:\t',edge)

#funtion to check if graph have Hamiltonian circuit or not
def CheckHamiltonian(start):

    #when lenght of path is equal to number of vertex
    if len(path)==len(graph_dict):

        #when start vertex to end vertex return True else return false
        if path[-1] in graph_dict[path[0]]:
            return True
        else:
            return False

    else:

        #iterating to visit neighbour vertex
        for neighbour in graph_dict[start]:

            #when  neighbour not visited
            if visited[neighbour]==False:
                #visit the neihbour
                visited[neighbour]=True
                path.append(neighbour)

                #calling function to visit remaining vertex and if function return True then return True
                if CheckHamiltonian(neighbour)==True:
                    return True

                else:
                    #unvisit visited neighbour
                    visited[neighbour]=False
                    path.pop()
        return False
    



#driver code
nodes=[i for i in input('Enter the All the vertex in graph with space between each vertex:\n ').split()]

#create object for Graph class
graph=Graph(nodes)

for vertex in nodes:        #loop to add edegs

    #while loop to take edges from user then check if its correct edge
    while True:
        flag=True   #flag to decide when break while loop

        #taking edges for vertex from user
        edges=[edge for edge in input(f"\nEnter all Edge of '{vertex}' (eg: if vertex is A and edge is AB then type B):\n").split()]

        #loop to check if edge is vaild
        for edge in edges:
            if edge not in nodes:
                print('Enter correct vertexs!!')
                flag=False
                break       #break when edge is not correct

        if flag: break      #break when edge is correct

    graph_dict=graph.addEdge(vertex,edges)

graph.printGraph()          #printing graph adjacent list

path=list()                 #list contain path of graph
visited=dict()              #dict will conatain all visited node
for i in graph_dict:        #loop to get start vertex
    start=i                 #start vertex
    break

for i in graph_dict:        #loop to marks vertex initially not visited
    visited[i]=False

visited[start]=True         #mark start vertex as visited
path.append(start)          #add start vertext to path

#calling function  to check if Hamiltonian circuit exits or not
if CheckHamiltonian(start) :
    print("\nGraph has Hamiltonian Circuit and i.e.") 
    print(*path,start,sep=' --> ')
else:
    print("Graph not have a Hamiltonian Circuit")
