import numpy as np
import graph_tool.all as gt
import matplotlib.pyplot as plt
plt.style.use('classic')
from itertools import product

#g = gt.collection.data['karate']
#g = gt.collection.data['dolphins']
#g = gt.collection.data['football']
#g = gt.collection.data['netscience']
#g = gt.collection.data['polblogs']
#g = gt.collection.data['power']
g = gt.load_graph('sbm2blocks.gt')
gt.graph_draw(g)

adj_mat = gt.adjacency(g).todense()

edge_nbr_ratio = g.new_edge_property('float')
ratios = []

for e in g.edges():
    v1, v2 = e
    nbrs1 = g.get_out_neighbours(v1)
    nbrs2 = g.get_out_neighbours(v2)

    pairs = product(nbrs1, nbrs2)
    tot = 0
    for pair in pairs:
        if pair[0] != pair[1]: tot += 1
        if adj_mat[pair[0], pair[1]] == 1:
            edge_nbr_ratio[e] += 1

    try:
        edge_nbr_ratio[e] /= tot
        ratios.append(edge_nbr_ratio[e])
    except:
        pass

ratios = np.array(ratios)
print(ratios.mean(), ratios.std())
plt.hist(ratios, bins = 20)
plt.show()



    
