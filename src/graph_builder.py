import json
import sys
from math import log

import numpy as np


class GraphBuilder:
    def __init__(self, graph, config_file, mode):
        self.graph = graph
        self.mode = mode
        self.parse_config(config_file)

    def parse_config(self, config_file):
        with open(config_file, 'r') as f:
            json_config = json.load(f)

        self.c1 = json_config['c1']
        self.c2 = json_config['c2']
        self.c3 = json_config['c3']
        self.c4 = json_config['c4']
        self.max_iterations_count = json_config['max_iterations_count']

    def initialize_coordinates(self):
        coordinates = []
        for v in range(self.graph.shape[0]):
            if self.mode == '3D':
                coordinates.append(
                    np.array([np.random.randint(0, 10), np.random.randint(0, 10), np.random.randint(0, 10)],
                             dtype=float))
            else:
                coordinates.append(
                    np.array([np.random.randint(0, 10), np.random.randint(0, 10)], dtype=float))

        return np.array(coordinates)

    def get_coordinates(self):
        coordinates = self.initialize_coordinates()

        all_forces_norms = [sys.maxsize]
        for i in range(self.max_iterations_count):
            forces = []
            for v in range(self.graph.shape[0]):
                for u in range(self.graph.shape[0]):
                    if u != v:
                        shift_vector = coordinates[u] - coordinates[v]
                        d = max(np.linalg.norm(shift_vector), 0.0001)

                        if self.graph[v][u]:
                            force = self.c1 * log(d / self.c2)
                        else:
                            force = -self.c3 / d ** 2

                        shift = self.c4 * force * shift_vector / d
                        coordinates[v] += shift
                        forces.append(force)
            cur_forces_norm = np.linalg.norm(forces)

            if cur_forces_norm >= np.max(all_forces_norms[-10:]):
                print('Iterations count: {}'.format(i))
                break

            all_forces_norms.append(cur_forces_norm)

        return coordinates
