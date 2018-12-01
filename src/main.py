import argparse

from formulas_parser import SmileFormulaParser
from graph_builder import GraphBuilder
from graph_drawer import GraphDrawer

if __name__ == '__main__':
    ap = argparse.ArgumentParser()

    ap.add_argument("-f", "--formula", required=True,
                    help="Formula in pseudo SMILE notation")
    ap.add_argument("-m", "--mode", required=True,
                    help="Mode: 2D or 3D")
    ap.add_argument("-c", '--config', required=True,
                    help='Path to config file')

    args = vars(ap.parse_args())

    formula = args['formula']
    mode = args['mode']
    config_file = args['config']

    graph = SmileFormulaParser(formula).parse_formula()

    coordinates = GraphBuilder(graph, config_file, mode).get_coordinates()

    GraphDrawer(graph, coordinates, mode).draw()