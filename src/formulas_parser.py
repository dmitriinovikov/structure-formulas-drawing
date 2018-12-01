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

    def find_last_non_bracket(self, stack):
        i = -1
        while stack[i] == '(' or stack[i] == ')':
            i -= 1
        return stack[i]

    def parse_formula(self):
        prepared_formula = self.prepare_formula()
        self.graph = np.zeros((self.vertices_count, self.vertices_count))
        cur_vertex_idx = 0
        stack = [0]
        for i in range(1, len(prepared_formula)):
            next_element = prepared_formula[i]
            if next_element == '(':
                stack.append(next_element)
            elif next_element == ')':
                while stack[-1] != '(':
                    stack.pop()
                stack.pop()
            else:
                self.add_edge_to_graph(self.find_last_non_bracket(stack), cur_vertex_idx + 1)
                cur_vertex_idx += 1
                stack.append(cur_vertex_idx)
        return self.graph
