# 6.00.2x Problem Set 5
# Graph optimization
# Finding shortest paths through MIT buildings
#

import string
# This imports everything from `graph.py` as if it was defined in this file!
from graph import * 

#
# Problem 2: Building up the Campus Map
#
# Before you write any code, write a couple of sentences here 
# describing how you will model this problem as a graph. 

# This is a helpful exercise to help you organize your
# thoughts before you tackle a big design problem!
#

def load_map(mapFilename):
    """ 
    Parses the map file and constructs a directed graph

    Parameters: 
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive 
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    file = open(mapFilename, "r")
    data = file.read().split("\n")
    nodeList = []
    for line in data:
        node = []
        details = line.split(" ")
        for detail in details:
            node.append(int(detail))
        nodeList.append(node)
            
    print "Loading map from file..."
    
    MITgraph = WeightedDigraph()
  
    for node in nodeList:
        start = node[0]
        end = node[1]
        totalDistance = node[2]
        outdoorDistance = node[3]
        
        startNode = Node(start)
        endNode = Node(end)
        
        if not MITgraph.hasNode(startNode):
            MITgraph.addNode(startNode)
            
        if not MITgraph.hasNode(endNode):
            MITgraph.addNode(endNode)
            
        edge = WeightedEdge(startNode,endNode,totalDistance,outdoorDistance)
        MITgraph.addEdge(edge)
    
    return MITgraph

#
# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize
# and what the constraints are
#

def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):    
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    def getTotalDistances(validPaths, digraph):
        allDistances= []
        for path in validPaths:
            start = 0
            end = 1
            total = 0
            allEdges = digraph.edges[path[start]]
            #print(allEdges)
            for node in range(len(path) - 1):
                for edge in allEdges:
                    if edge[0] == path[end]:
                        #print(edge[1].getTotalDistance())
                        total += edge[1].getTotalDistance()
                start += 1
                end += 1
            #print("Total distance for this path = %s" % total)
            allDistances.append(total)
        return allDistances
    
    def getTotalOutdoor(validPaths, digraph):
        allOutdoors = []
        for path in validPaths:
            start = 0
            end = 1
            total = 0
            allEdges = digraph.edges[path[start]]
            #print(allEdges)
            for node in range(len(path) - 1):
                for edge in allEdges:
                    if edge[0] == path[end]:
                        #print(edge[1].getOutdoorDistance())
                        total += edge[1].getOutdoorDistance()
                start += 1
                end += 1
            #print("Total outdoor distance for this path = %s" % total)
            allOutdoors.append(total)
        return allOutdoors
     
    def returnPath(currentNode, end, digraph, path = [], seen = []):
        if currentNode not in seen:
            children = digraph.childrenOf(currentNode)
            #print("Children of this Node: %s" % children)
            if str(currentNode) == str(end):
                path.append(end)
                #print("yes")
            else:
                if end in children:
                    path.append(currentNode)
                    path.append(end)
                else:
                    path.append(currentNode)
                    #print("Updated path: %s" % path)
                    seen.append(currentNode)
                    returnPath(children[-1], end, digraph, path, seen)
        return path
            
    startNode = Node(start)
    endNode = Node(end)
    
    totalList = [edge for edge in digraph.childrenOf(startNode)] 
    #print(totalList) 
    validPaths = []
    while totalList:
        attempt = totalList.pop(-1)
        result = returnPath(attempt, endNode, digraph, path = [startNode])
        if endNode in result:
            validPaths.append(result)
            
    print("Valid paths: %s" % validPaths)
    print("Making a list of Total Distances for all paths")
    allDistances = getTotalDistances(validPaths, digraph)
    print("    Path distances: %s" % allDistances)
    
    print("Making a list of Total Outdoor Distances for all paths")
    allOutdoors = getTotalOutdoor(validPaths, digraph)
    print("    Path outdoor distances: %s" % allOutdoors)

    okPaths = []
    updatedDist = []
    print("\nDiscard paths which don't satisfy the criteria")
    
    print("Paths before the cull:\n    %s" % validPaths)
    for distance in range(len(allDistances)):
        if allDistances[distance] <= maxTotalDist and allOutdoors[distance] <= maxDistOutdoors:
            okPaths.append(validPaths[distance])
            updatedDist.append(allDistances[distance])
    try:
        okPaths[0]
        print(okPaths[0])
    except:
        raise ValueError
        
    print("Paths after the cull:\n    %s" % okPaths)

    print("Of the remaining paths, return the shortest path")
    shortest = maxTotalDist
    bestPath = 0
    for i in range(len(okPaths)):
        distance = updatedDist[i]
        if distance < shortest:
            shortest = distance
            bestPath = okPaths[i]
            
    pathString = []
    for j in range(len(bestPath)):
            pathString.append(str(bestPath[j]))
    print("Shortest path is %s" % pathString)
    
    return pathString

#
# Problem 4: Finding the Shorest Path using Optimized Search Method
#
def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using directed depth-first.
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
	not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    #TODO
    pass

# Uncomment below when ready to test
#### NOTE! These tests may take a few minutes to run!! ####
if __name__ == '__main__':
#     Test cases
     mitMap = load_map("mit_map.txt")
#    print isinstance(mitMap, Digraph)
#    print isinstance(mitMap, WeightedDigraph)
#    print 'nodes', mitMap.nodes
#    print 'edges', mitMap.edges


     LARGE_DIST = 1000000

     #Test case 1
     print "---------------"
     print "Test case 1:"
     print "Find the shortest-path from Building 32 to 56"
     expectedPath1 = ['32', '56']
     brutePath1 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
     brutePath2 = bruteForceSearch(mitMap, "1", "3", 80, 80)
#     dfsPath1 = directedDFS(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
#     print "Expected: ", expectedPath1
#     print "Brute-force: ", brutePath1
#     print "DFS: ", dfsPath1
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath1 == brutePath1, expectedPath1 == dfsPath1)

#     Test case 2
#     print "---------------"
#     print "Test case 2:"
#     print "Find the shortest-path from Building 32 to 56 without going outdoors"
#     expectedPath2 = ['32', '36', '26', '16', '56']
#     brutePath2 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, 0)
#     dfsPath2 = directedDFS(mitMap, '32', '56', LARGE_DIST, 0)
#     print "Expected: ", expectedPath2
#     print "Brute-force: ", brutePath2
#     print "DFS: ", dfsPath2
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath2 == brutePath2, expectedPath2 == dfsPath2)

#     Test case 3
#     print "---------------"
#     print "Test case 3:"
#     print "Find the shortest-path from Building 2 to 9"
#     expectedPath3 = ['2', '3', '7', '9']
#     brutePath3 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
#     dfsPath3 = directedDFS(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
#     print "Expected: ", expectedPath3
#     print "Brute-force: ", brutePath3
#     print "DFS: ", dfsPath3
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath3 == brutePath3, expectedPath3 == dfsPath3)

#     Test case 4
#     print "---------------"
#     print "Test case 4:"
#     print "Find the shortest-path from Building 2 to 9 without going outdoors"
#     expectedPath4 = ['2', '4', '10', '13', '9']
#     brutePath4 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, 0)
#     dfsPath4 = directedDFS(mitMap, '2', '9', LARGE_DIST, 0)
#     print "Expected: ", expectedPath4
#     print "Brute-force: ", brutePath4
#     print "DFS: ", dfsPath4
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath4 == brutePath4, expectedPath4 == dfsPath4)

#     Test case 5
#     print "---------------"
#     print "Test case 5:"
#     print "Find the shortest-path from Building 1 to 32"
#     expectedPath5 = ['1', '4', '12', '32']
#     brutePath5 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
#     dfsPath5 = directedDFS(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
#     print "Expected: ", expectedPath5
#     print "Brute-force: ", brutePath5
#     print "DFS: ", dfsPath5
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath5 == brutePath5, expectedPath5 == dfsPath5)

#     Test case 6
#     print "---------------"
#     print "Test case 6:"
#     print "Find the shortest-path from Building 1 to 32 without going outdoors"
#     expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
#     brutePath6 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, 0)
#     dfsPath6 = directedDFS(mitMap, '1', '32', LARGE_DIST, 0)
#     print "Expected: ", expectedPath6
#     print "Brute-force: ", brutePath6
#     print "DFS: ", dfsPath6
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath6 == brutePath6, expectedPath6 == dfsPath6)

#     Test case 7
#     print "---------------"
#     print "Test case 7:"
#     print "Find the shortest-path from Building 8 to 50 without going outdoors"
#     bruteRaisedErr = 'No'
#     dfsRaisedErr = 'No'
#     try:
#         bruteForceSearch(mitMap, '8', '50', LARGE_DIST, 0)
#     except ValueError:
#         bruteRaisedErr = 'Yes'
    
#     try:
#         directedDFS(mitMap, '8', '50', LARGE_DIST, 0)
#     except ValueError:
#         dfsRaisedErr = 'Yes'
    
#     print "Expected: No such path! Should throw a value error."
#     print "Did brute force search raise an error?", bruteRaisedErr
#     print "Did DFS search raise an error?", dfsRaisedErr

#     Test case 8
#     print "---------------"
#     print "Test case 8:"
#     print "Find the shortest-path from Building 10 to 32 without walking"
#     print "more than 100 meters in total"
#     bruteRaisedErr = 'No'
#     dfsRaisedErr = 'No'
#     try:
#         bruteForceSearch(mitMap, '10', '32', 100, LARGE_DIST)
#     except ValueError:
#         bruteRaisedErr = 'Yes'
    
#     try:
#         directedDFS(mitMap, '10', '32', 100, LARGE_DIST)
#     except ValueError:
#         dfsRaisedErr = 'Yes'
    
#     print "Expected: No such path! Should throw a value error."
#     print "Did brute force search raise an error?", bruteRaisedErr
#     print "Did DFS search raise an error?", dfsRaisedErr
