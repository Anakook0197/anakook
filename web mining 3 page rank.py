import networkx as nx
# create the graph
G = nx.DiGraph()
G.add_nodes_from(['page1', 'page2', 'page3', 'page4'])
G.add_edges_from([('page1', 'page2'), ('page1', 'page2'), ('page1', 'page3'), ('page3', 'page1')])

# calculate PageRank scores
pr = nx.pagerank(G, alpha=0.85)
rw = nx.pagerank(G)

# Print the random walk probability of each page print(rw)
print("the random walk is as follows")
print("page 1",rw['page1'])
print("page 2",rw['page2'])
print("page 3",rw['page3'])
print("page 4",rw['page4'])


