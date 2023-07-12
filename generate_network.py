import numpy as np
import networkx as nx
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import kneighbors_graph

def random_networks(pin, pout, networksize, CN):
    """
    generate a random community networks
    pin:Random connection probability between nodes within the community
    pout:Random connection probability of nodes between various communities
    @return:the matrix of the networks
    """
    NETWORK_SIZE=networksize
    #PROBABILITY_OF_EAGE=0.8  #Limited to global
    pin=pin
    #pout=0.01
    pout=pout
    M = CN # Community Number
    Amatrix = [[0 for i in range(NETWORK_SIZE)] for i in range(NETWORK_SIZE)]
    #def generateRandomNetwork()：
    for i in range(0,NETWORK_SIZE):
        for j in range(i,NETWORK_SIZE):
            Amatrix[i][j] = Amatrix[j][i] = 0

    # Intracommunity (社区内部)
    intvl = int(NETWORK_SIZE/M)  #输出为： 16
    bgIntvl = 0
    endIntvl = intvl

    for m in range(M):
        for i in range(bgIntvl,endIntvl):
            for j in range(bgIntvl,endIntvl):
                if (i==j):
                    continue
                probability=np.random.random()
                if(probability <= pin):
                    Amatrix[i][j] = Amatrix[j][i] = 1
        #Update Interval
        bgIntvl += intvl
        endIntvl += intvl

    # INTERcommunity  （共同性，共通性）
    bg1 = 0
    end1 = intvl   #intvl = 16
    for m1 in range(M-1):    # M=8
        # Destiny Range Initial Conditions
        bg2 = end1
        end2 = end1 + intvl
        for m2 in range(M-m1-1):
            for i in range(bg1, end1):
                for j in range(bg2,end2):
                    probability=np.random.random()
                    if(probability <= pout):
                        Amatrix[i][j] = Amatrix[j][i] = 1
            # Destiny Range Update
            bg2 = end2
            end2 = end2 + intvl
        bg1 = end1
        end1 = end1 + intvl
    D = np.array(Amatrix)
    # 构建一个Graph
    G = nx.Graph()
    for i in range(D.shape[0]):
        G.add_node(i)
    for i in range(len(D)):
        for j in range(len(D)):
            if (D[i][j] == 1):
                G.add_edge(i, j)
    return D, G
def iris_G(k):
    """
    @return:adj_Matrix, G
    """
    # 加载iris数据集
    iris = load_iris()
    X = iris.data

    # 标准化数据
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    # 计算节点之间的距离
    # 构建k-nearest neighbor图
    G = kneighbors_graph(X, k, mode='connectivity', include_self=False)

    # 将稀疏矩阵转换为无向图
    G = G.toarray()
    G = np.maximum(G, G.transpose())

    # 将数组转换为networkx图,可以直接show出来的
    G = nx.from_numpy_array(G)

    # 将稀疏矩阵转换为无向图的邻接矩阵
    adj_matrix = nx.to_numpy_array(G)


    return adj_matrix, G


