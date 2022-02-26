#Program to check if graph is planer or not
#this program not work for K3,3

def main():
    #taking total number vertex and edges from user
    vertex=int(input("Enter the Total number of vertex in the graph: "))
    edges=int(input('Enter the Total number of edges in the graph: '))

    #max edge of vertex
    max=vertex*(vertex-1)/2

    #checking the edge is valid or not
    if edges>max:
        print("Edge is not correct")
        exit()
        
    #checking the graph is planer or not
    if (edges<=3*vertex-6 and vertex>=3) or vertex==2:
        print("Graph is planer ")
    else:
        print("Graph is not planer ")

if __name__=="__main__":
    main()