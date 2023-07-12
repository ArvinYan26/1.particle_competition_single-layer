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


def random_networks_detect(pin, pout, networksize, CN, times, particle_num):
    # generate random networks and Graph
    AMatrix, G = random_networks(pin, pout, networksize, CN)
    # print("G.nodes:", len([G.nodes]), [G.nodes])
    show_matrix(AMatrix)
    plot_graph(G, [G.nodes])
    # detect the communities of the random networks
    detect_communities(G, AMatrix, times, particle_num)

if __name__ == '__main__':
    # config some parameters
    pin, pout = 0.7, 0.01
    networksize = 128
    CN = 4    #CN: number of community
    # 设置模型参数
    # 迭代次数
    times = [300, 800, 1700]
    particle_num = 4
    random_networks_detect(pin, pout, networksize, CN, times, particle_num)
