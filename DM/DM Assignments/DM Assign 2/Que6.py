'''
Write a program to identify that the given graph is planar or not.
'''

def main():    
    vertx=int(input("Enter the Total number of Vertex in the graph: ")) #taking total number vertx and edges from user
    edges=int(input('Enter the Total number of Edges in the graph: ')) #taking total number vertx and edges from user

    max=vertx*(vertx-1)/2 #max edge of vertx

    
    if edges>max: #checking the edge is valid or not
        print("Edge is not correct")
        exit()
          
    if (edges<=3*vertx-6 and vertx>=3) or vertx==2:  #checking the graph is planer or not
        print("Graph is Planer ")
    else:
        print("Graph is Not Planer ")

if __name__=="__main__":
    main()