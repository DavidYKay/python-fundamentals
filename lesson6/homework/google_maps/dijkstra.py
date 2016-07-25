import random

INFINITY = float("inf")

def min_unvisited(unvisited, dist):
    """ Get the unvisted node with minimal cost.
        Note: Source node will be selected first."""
    scored = [(dist[v], v) for v in unvisited]
    dist, v = sorted(scored, key=lambda x: x[0])[0]
    return v

def unvisited_neighbors(G, unvisited, v):
    """ Get the nodes which have not been visited yet. """
    return {n for n in G.neighbors(v) if n in unvisited}

def route(source, end, prev):
    """ Given the previous stops dictionary, return a list of the stops along the route."""
    stops = []
    current = end
    while current != None:
        stops.append(current)
        current = prev[current]
    return list(reversed(stops))

def shortest_route(G, source, end):
    """ Use Dijkstra's algorithm to find the shortest path between two nodes on a graph."""

    prev = {}
    dist = {}
    unvisited = set()

    for v in G.nodes():
        dist[v] = INFINITY
        prev[v] = None
        unvisited.add(v)
    dist[source] = 0

    while unvisited:
        u = min_unvisited(unvisited, dist)
        unvisited.remove(u)

        for i, v in enumerate(unvisited_neighbors(G, unvisited, u)):
            alt = dist[u] + G[u][v]['weight']
            if i % 2 == 0:
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
            else:
                if alt > dist[v]:
                    dist[v] = alt
                    prev[v] = u

    return (route(source, end, prev), dist[end])

