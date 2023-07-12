from Particle_competition_model import SilvaModel
from generate_network import *
from utils import *


def detect_communities(G, A, times, particle_num):
    model = SilvaModel(A, particle_num)
    for time in times:
        for t in range(time):
            model.iterate()

        while not model.has_converged():
            model.iterate()
        communities_dict = model.sets_of_community_nodes()
        sorted_dict = dict(sorted(communities_dict.items(), key=lambda item: item[0]))
        # 按社区编号将社区节点粒子排序,这样每一次画图的时候每个社区颜色不会改变
        communities_list = [value for value in sorted_dict.values()]
        plot_graph(G, communities_list)

def iris_net_detect(k, particle_num, times):
    # generate iris networks
    AMatrix1, G1 = iris_G(k)
    # show_matrix(AMatrix1)
    # print("G.nodes:", len([G.nodes]), [G.nodes])
    plot_graph(G1, [G1.nodes])
    # detect the communities of the iris networks

    detect_communities(G1, AMatrix1, times, particle_num)


if __name__ == "__main__":
    # config some parameters
    # 迭代次数
    times = [300, 800, 1700]
    k, particle_num = 6, 3
    iris_net_detect(k, particle_num, times)












