def add_node(v):
    global node_count
    if v in nodes:
        print(v,"Always present in graph")
    else:
        node_count = node_count + 1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)

def add_edge(v1,v2,e):
    if v1 not in nodes:
        print(v1,"is not present in graph")
    elif v2 not in nodes:
        print(v2," is not present in graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = e
        # graph[index2][index1] = e

def delete_node(v):
    global node_count
    if v not in nodes:
        print(v,"is not present in graph")
    else:
        index1 = nodes.index(v)
        node_count = node_count - 1
        nodes.remove(v)
        graph.pop(index1)
        for i in graph:
            i.pop(index1)

def delete_edge(v1,v2):
    if v1 not in nodes:
        print(v1," is not present in graph")
    elif v2 not in nodes:
        print(v2," is not prsent in graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 0
        # graph[index2][index1] = 0
        

def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format (graph[i][j],"<4"),end=" ")
        print()

        
nodes = []
graph = []
node_count = 0
print("Before adding nodes")
print(nodes)
print(graph)


add_node("A")
add_node("B")
add_node("C")
print("After adding nodes")
print(nodes)
add_edge("A","C",6)
add_edge("A","B",2)
print_graph()
delete_edge("A","C")
print("Graph after deleting")
print(graph)
print_graph()
print("Nodes:- ",nodes)
print("Count nodes : ",node_count)
