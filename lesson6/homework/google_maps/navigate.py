import csv
import math
import matplotlib.pyplot as plt
import networkx as nx

from sys import argv
from dijkstra import shortest_route

def square(x):
    return x*x

def load_zips():
    """ Get the unvisted node with minimal cost."""
    with open('simple_zips.csv') as f:
        return list(csv.DictReader(f))

def location(city):
    return (float(city["Lat"]), float(city["Long"]))

def get_distance(a, b):
    a_x, a_y = a
    b_x, b_y = b
    return math.sqrt((square(abs(a_x - b_x)) + square(abs(a_y - b_y))))

def make_graph(cities):
    """ Make a graph data structure, given a list of dictionaries representing the cities."""
    G = nx.Graph()
    pos = {city["City"]: location(city) for city in cities}
    edge_labels = {}
    for city in cities:
        name = city["City"]
        destinations = city["Nearby"].split(",")
        for d in destinations:
            distance = get_distance(location(city), pos[d])
            G.add_edge(name, d, weight=distance)
            edge_labels[(name,d)] = "%6.1f" % distance
    if __name__ == '__main__':
        # NOTE: The program will stop here to draw the graph. You'll need to close the window to keep going.
        nx.draw(G, pos=pos)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
        plt.show()
    return G

def navigate(G, source, dest):
    """ The main method. Given a source and dest, find the fastest route along the graph G."""
    return shortest_route(G, source, dest)

if __name__ == '__main__':
    try:
        _, src, dest = argv
    except ValueError:
        print("Usage:   python navigate.py [SOURCE] [DESTINATION]\n" +
                "Example: python navigate.py NASHVILLE ORLANDO\n")
        raise
    g = make_graph(load_zips())
    print(navigate(g, src, dest))
