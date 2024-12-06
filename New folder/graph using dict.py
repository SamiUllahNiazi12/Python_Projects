
def add_node(v):
    if v in graph:
        print(v,"present in graph")
    else:
        graph[v] = []

def add_edge(v1,v2):
    if v1 not in graph:
        print(v1,"is not present in graph")
    elif v2 not in graph:
        print(v2,"is not present in graph")
    else:
        
        # for weighted graph
        # list1 = [v2,cost]
        # list2 = [v1,cost]
        # graph[v1].append(list1)
        # graph[v2].append(list2)

        # for unweighted graph
        graph[v1].append(v2)
        graph[v2].append(v1)


# def delete_node(v):
#     if v not in graph:
#         print(v, " is not present in graph")
#     else:
#         graph.pop(v)
#         for i in graph:
#             list1 = graph[i]
#             for j in list1:
#                 list1.remove(j)
#                 break

# def delete_edge(v1,v2,cost):
#     if v1 not in graph:
#         print(v1," is not present in grsph")
#     elif v2 not in graph:
#         print(v2," is not present in graph")
#     else:
#         temp = [v1,cost]
#         temp1 = [v2,cost]
#         if temp1 in graph[v1]:
#            graph[v1].remove(temp1)
#            graph[v2].remove(temp)

    
# for unweighted and undirected graph
        # if v2 in graph[v1]:
            # graph[v1].remove(v2)
            # graph[v2].remove(v1)

"""def DFS(node,visited,graph):
    if node not in graph:
        print("Given node is not present in graph")
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS(i,visited,graph) """   

def DFSiterative(node,graph):
    visited = set()
    if node not in graph:
        print("Node is not present in graph")
        return
    stack = []
    stack.append(node)
    while stack:
        current = stack.pop()
        if current not in visited:
           print(current)
           visited.add(current)
           for i in graph[current]:
              stack.append(i)



# visited = set()
graph = {}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
# add_node("F")
# add_node("G")
add_edge("A","B") # 10 is for weighted graph
add_edge("A","C")
add_edge("A","D")
add_edge("B","E")
add_edge("B","D")
add_edge("C","D")
add_edge("D","E")
print(graph)
DFSiterative("A",graph)

# print(graph,"\n Before deletion")
# delete_edge("B","E",43)