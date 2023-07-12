import matplotlib.pyplot as plt
import networkx as nx

def plot_graph(G,  communities_nodes):
    """
    plot the Graph
    """
    plt.figure(figsize=(20, 20))

    # num_communities = len(communities_nodes)
    if len(communities_nodes) == 1:
        # pos是为了保证每一次画图，后期在修改添加节点的时候，位置是不变的
        pos = nx.spring_layout(G, seed=42)
        nx.draw_networkx(G, pos=pos, node_size=400, with_labels=False, width=0.15, node_color='k', node_shape="*")
    else:
        """
        pos = nx.spring_layout(G)
        for i in range(len(communities_nodes)):
            nx.draw_networkx(G, pos=pos, node_size=400, with_labels=True, width=0.15, node_color=node_color,
                             label=f"Community {i}")
        """
        # 定义节点颜色和形状字典
        community_styles = {}
        for i, comm in enumerate(communities_nodes):
            # 随机生成颜色
            # color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
            # 固定每个社区的颜色
            color_list = ['r', 'b', 'm', 'g', 'c', 'y', 'w']
            # 从列表中随机选择一种形状
            # shape = random.choice(['o', '1', '^', 'd', 'D'])
            # 每次按照社区编号选择特定形状
            shape_list = ['o', 's', '^', 'd', 'D']
            community_styles[i] = {'color': color_list[i], 'shape': shape_list[i]}
        # 绘制图形
        # plt.figure(figsize=(20, 20))
        pos = nx.spring_layout(G, seed=42)
        for i, comm in enumerate(communities_nodes):
            nx.draw_networkx_nodes(G, pos, nodelist=comm, node_size=300,
                                   node_shape=community_styles[i]['shape'],
                                   node_color=community_styles[i]['color'])
        # nx.draw_networkx_labels(G, pos)  # 显示节点编号
        nx.draw_networkx_edges(G, pos, alpha=0.2)
        # 添加图例
        handles = []
        labels = []
        for i, comm in enumerate(communities_nodes):
            label = f'community {i + 1}'
            h = plt.scatter([], [], s=300, marker=community_styles[i]['shape'], color=community_styles[i]['color'])
            handles.append(h)
            labels.append(label)
        plt.legend(handles, labels, scatterpoints=1, fontsize=14)

    plt.show()

def show_matrix(AMatrix):
    """
    @param AMatrix: 邻接矩阵呢
    """
    plt.Figure(figsize=(20, 20))
    # show the random community networks graph
    plt.imshow(AMatrix)
    plt.show()


