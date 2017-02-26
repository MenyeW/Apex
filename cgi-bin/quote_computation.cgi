#!/Python27/python

import pymongo
import memcache

def dijkstra(graph,src,dest,visited=[],distances={},predecessors={}):

    if src == dest:
        path=[]
        pred=dest
        while pred != None:
            path.append(pred)
            pred=predecessors.get(pred,None)
        #print path
        #print distances[dest]
        return path, distances[dest]
    else :     
        # if it is the initial  run, initializes the cost
        if not visited: 
            distances[src]=0
        # visit the neighbors
        for neighbor in graph[src] :
            if neighbor not in visited:
                new_distance = distances[src] + graph[src][neighbor]
                if new_distance < distances.get(neighbor,float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = src
        # mark as visited
        visited.append(src)
        unvisited={}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k,float('inf'))
                
        x=min(unvisited, key=unvisited.get)
        return dijkstra(graph,x,dest,visited,distances,predecessors)

def createCostMatrix():
    #db code
    client = pymongo.MongoClient()
    db = client.careem
    routes = db.Partner_Routes
    all_routes = routes.find()
    g = dict()
    cities = set()
    for route in all_routes:
        src = route["src"]
        dst = route["dst"]
        cost = route["cost"]
        if not src in g:
            g[src] = {}
        if not dst in g:
            g[dst] = {}
        if not src in cities:
            cities.add(src)
        if not dst in cities:
            cities.add(dst)
        g[src][dst] = cost
        g[dst][src] = cost
    costs = dict()
    paths = dict()
    for city1 in cities:
        costs[city1] = {}
        paths[city1] = {}
        for city2 in cities:
            if not city1 == city2:
                paths[city1][city2] , costs[city1][city2]  = dijkstra(g, city1, city2,[],{},{})
                paths[city1][city2].reverse()
    mc = memcache.Client(['127.0.0.1:11211'], debug=0)
    mc.set("pathMatrix",paths)
    mc.set("costMatrix",costs)

if __name__ == '__main__':
    createCostMatrix()
    print "Content-Type: text/html"     # HTML is following
    print                               # blank line, end of headers


