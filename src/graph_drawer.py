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
                    x_coordinates = [self.coordinates[i][0], self.coordinates[j][0]]
                    y_coordinates = [self.coordinates[i][1], self.coordinates[j][1]]
                    z_coordinates = [self.coordinates[i][2], self.coordinates[j][2]]
                    ax.plot(x_coordinates,
                            y_coordinates,
                            z_coordinates,
                            marker='o',
                            ms=20,
                            linewidth=10,
                            linestyle="-",
                            c='black'
                            )

        plt.show(block=True)

    def draw_2d(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        for i in range(self.graph.shape[0]):
            for j in range(self.graph.shape[1]):
                if i < j and self.graph[i][j]:
                    x_coordinates = [self.coordinates[i][0], self.coordinates[j][0]]
                    y_coordinates = [self.coordinates[i][1], self.coordinates[j][1]]
                    ax.plot(x_coordinates,
                            y_coordinates,
                            marker='o',
                            ms=25,
                            linewidth=10,
                            linestyle="-",
                            c="black")

        plt.show(block=True)
