import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class GraphDrawer:
    def __init__(self, graph, coordinates, mode):
        self.coordinates = coordinates
        self.graph = graph
        self.mode = mode

    def draw(self):
        if self.mode == '3D':
            return self.draw_3d()
        else:
            return self.draw_2d()

    def draw_3d(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        for i in range(self.graph.shape[0]):
            for j in range(self.graph.shape[1]):
                if i < j and self.graph[i][j]:
                    ax.plot([self.coordinates[i][0], self.coordinates[j][0]],
                            [self.coordinates[i][1], self.coordinates[j][1]],
                            [self.coordinates[i][2], self.coordinates[j][2]],
                            linewidth=3, linestyle="-", c="purple",
                            marker='o')

        plt.show(block=True)

    def draw_2d(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        for i in range(self.graph.shape[0]):
            for j in range(self.graph.shape[1]):
                if i < j and self.graph[i][j]:
                    ax.plot([self.coordinates[i][0], self.coordinates[j][0]],
                            [self.coordinates[i][1], self.coordinates[j][1]],
                            linewidth=3, linestyle="-", c="purple",
                            marker='o')

        plt.show(block=True)
