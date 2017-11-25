import graph_tool.all as gt
import numpy as np


def deg_sampler():
    return np.random.poisson(7)

def edge_probs(r, s):
    if r == s:
        return 0.999
    else:
        return 0.999

N = 100
g, bm = gt.random_graph(N, deg_sampler, block_membership = np.random.choice((0, 1), size = N), directed = False, edge_probs = edge_probs, n_iter = 1000, model = 'blockmodel-degree')
print(g)

g.save('sbm2blocks.gt')
