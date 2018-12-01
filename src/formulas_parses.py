import numpy as np


class SmileFormulaParser:

    def __init__(self, smile):
        self.formula = smile
        self.graph = None
        self.vertices_count = 0

    def add_edge_to_graph(self, v, u):
        self.graph[v][u] = 1
        self.graph[u][v] = 1

    def prepare_formula(self):
        prepared_formula = ''
        for c in self.formula:
            if c.isalpha():
                self.vertices_count += 1
                prepared_formula += c
            elif c == '(' or c == ')':
                prepared_formula += c

        return prepared_formula

    def parse_formula(self):
        prepared_formula = self.prepare_formula()
        self.graph = np.zeros((self.vertices_count, self.vertices_count))
        cur_vertex_idx = 0
        stack = []
        is_last_symbol_close_bracket = False
        for i in range(1, len(prepared_formula)):
            next_element = prepared_formula[i]
            if next_element == '(':
                if not is_last_symbol_close_bracket:
                    is_last_symbol_close_bracket = False
                    stack.append(cur_vertex_idx)
            elif next_element == ')':
                is_last_symbol_close_bracket = True
            else:
                if is_last_symbol_close_bracket:
                    self.add_edge_to_graph(stack[-1], cur_vertex_idx + 1)
                else:
                    self.add_edge_to_graph(cur_vertex_idx, cur_vertex_idx + 1)
                cur_vertex_idx += 1
                is_last_symbol_close_bracket = False

        return self.graph
