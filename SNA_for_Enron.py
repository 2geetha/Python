# Visualizing Enron Network (Python)

# jump-start code developed by Tom Miller

# prepare for Python version 3x features and functions
from __future__ import division, print_function

# ensure that the package networkx has been installed
# by using the package manager under Enthought Canopy

# load packages into the workspace for this program
from operator import itemgetter
import networkx as nx
import os
import matplotlib.pyplot as plt  # 2D plotting

# ---------------------------------------------
# read in network edge list
# Entron from-node and to-node email addresses
# ---------------------------------------------
# read Enron edge data creating a NetworkX directed graph object g
# note use of blank text lines between edge lines in input file

#os.chdir('C://Users//Geetha\\MSPA\\452_WebAndNetworkDataScience\\452_Assignment_3_Option_2')

f = open('toWithLay.txt', 'rb')
#f = open('toWithLay.csv', 'rb')
g = nx.read_edgelist(f, create_using = nx.DiGraph(), delimiter = ',', nodetype = str)
f.close()


# print graph attributes
print('This is a directed network/graph (True or False): ', g.is_directed())
print('Number of nodes: ', nx.number_of_nodes(g))
print('Number of edges: ', nx.number_of_edges(g))
print('Network density: ', round(nx.density(g), 4))
# determine the total number of links for the network 

# plot the degree distribution 
fig = plt.figure()
plt.hist(nx.degree(g).values())
plt.axis([0, 8, 0, 8])
plt.xlabel('Node Degree')
plt.ylabel('Frequency')
plt.show()
    
# examine alternative layouts for plotting the network 
# plot the network/graph with default layout 
fig = plt.figure()
nx.draw_networkx(g, node_size = 0, node_color = 'yellow')
plt.show()

# spring layout
fig = plt.figure()
nx.draw_networkx(g, node_size = 0, node_color = 'yellow',\
    pos = nx.spring_layout(g))
plt.show()

# circlular layout
fig = plt.figure()
nx.draw_networkx(g, node_size = 0, node_color = 'yellow',\
    pos = nx.circular_layout(g))
plt.show()

# shell/concentric circles layout
fig = plt.figure()
nx.draw_networkx(g, node_size = 0, node_color = 'yellow',\
    pos = nx.shell_layout(g))
plt.show()

# pick the visualization that you prefer and route that to external pdf file
fig = plt.figure()

nx.draw_networkx(g, node_size = 25, node_color = 'yellow',\
    pos = nx.spring_layout(g), font_size=4, with_labels=False)
plt.show()
plt.savefig('sample_plot.pdf', bbox_inches = 'tight', dpi = None,
    facecolor = 'w', edgecolor = 'b', orientation = 'portrait', 
    papertype = None, format = None, pad_inches = 0.25, frameon = None)


#ego-graph
node_and_degree=g.degree()
(largest_hub,degree)=sorted(node_and_degree.items(),key=itemgetter(1))[-1]
(smallest_hub,degree)=sorted(node_and_degree.items(),reverse=True,key=itemgetter(1))[-1]
    # Create ego graph of main hub
hub_ego=nx.ego_graph(g,largest_hub)
hub_small_ego=nx.ego_graph(g,smallest_hub)
    # Draw graph
pos=nx.spring_layout(hub_ego)
plt.axis("off")
nx.draw(hub_ego,pos,node_color='b',node_size=50,with_labels=False)
plt.show()
    # Draw ego as large and red
nx.draw_networkx_nodes(hub_ego,pos,nodelist=[largest_hub],node_size=50,node_color='r', with_labels=False,radius=1)
plt.savefig('ego_graph.png')
plt.show()

#smallest egograph
pos=nx.spring_layout(hub_small_ego)

nx.draw(hub_small_ego,pos,node_color='b',node_size=50,with_labels=False)

    # Draw ego as large and red
nx.draw_networkx_nodes(hub_small_ego,pos,nodelist=[smallest_hub],node_size=50,node_color='r', with_labels=False,radius=1)
plt.savefig('ego_small_graph.png')
plt.show()
# options for visualization
# a static plot with many nodes and edges may not be especially informative
# so we look for alternatives... Gephi provides interactive network plots 
# dump the graph object in GraphML format for input to Gephi
nx.write_graphml(g,'wiki_data_to_gephi.graphml')

# Gephi is open-source GUI for exploring networks... it depends on Java.
# We need to install Gephi software first
# Gephi download and documentation site: http://gephi.github.io/
# Note that if your version of Java does not match up with Gephi,
# you may have difficulties running this program.