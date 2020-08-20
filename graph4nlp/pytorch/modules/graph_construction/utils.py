from scipy import sparse
import torch
import dgl
from dgl.nn.pytorch.softmax import edge_softmax

from ..utils.generic_utils import to_cuda
from ..utils.constants import INF
from ...data.data import GraphData

def convert_adj_to_dgl_graph(adj, mask_off_val, use_edge_softmax=False):
    """Convert adjacency matrix to DGLGraph
    """
    binarized_adj = sparse.coo_matrix(adj.detach().cpu().numpy() != mask_off_val)
    dgl_graph = dgl.DGLGraph(binarized_adj)
    edge_weight = adj[adj != mask_off_val]

    if use_edge_softmax:
        edge_weight = edge_softmax(dgl_graph, edge_weight)

    dgl_graph.edata['a'] = edge_weight

    return dgl_graph


def convert_adj_to_graph(adj, mask_off_val):
    """Convert adjacency matrix to GraphData
    """
    binarized_adj = sparse.coo_matrix(adj.detach().cpu().numpy() != mask_off_val)
    graph_data = GraphData()
    graph_data.from_scipy_sparse_matrix(binarized_adj)
    edge_weight = adj[adj != mask_off_val]

    graph_data.edge_features['a'] = edge_weight

    return graph_data