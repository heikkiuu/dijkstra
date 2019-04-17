import timeit

# Define file location
# File path is hardcoded and filename taken as user input
filename = input('Enter file name: ')
filepath = "C:/dijkstra" +filename

# Start timer to measure runtime
start = timeit.default_timer()

# Read the file in data
# Save the information of the first and the last line
with open(filepath,"r") as f:
    data = (f.read().splitlines())
numberOfCities = data[0].split()[0]
numberOfRoutes = data[0].split()[1]
destinationCity = data[-1]

# Initialize i as 1 to start looping through the data from the second line
# Initialize graph
i = 1
graph = {}

# Loop through all of the edges and weights(heights)
# Save the information to the graph
# Since we are working with an undirected graph, the edges between nodes will be saved to the graph both ways
while i <= int(numberOfRoutes):
    a = data[i].split()[0]
    b = data[i].split()[1]
    height = data[i].split()[2]
    if a not in graph:
        graph[a] = {}
    graph[a].update({b:int(height)})
    if b not in graph:
        graph[b] = {}
    graph[b].update({a:int(height)})
    i += 1
# print(graph)

# Initialize the function
def dijkstra(graph, start, goal):
    maxHeight = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 9999999
    path = []

    # Set all nodes to infinity and starting node to 0
    # maxHeight = {'1': 0, '2': 9999999, '3': 9999999, ... , 'n' : 9999999}
    for node in unseenNodes:
        maxHeight[node] = infinity
    maxHeight[start] = 0

    # Loop through all of the nodes in unseenNodes
    while unseenNodes:
        minNode = None
        for node in unseenNodes:

            # First case
            if minNode is None:
                minNode = node

            # Find the lowest height
            elif maxHeight[node] < maxHeight[minNode]:
                minNode = node

        # Child nodes are connected nodes, weights(height) are edge values
        # Keep track of highest edge value
        for childNode, height in graph[minNode].items():
            if max(height, maxHeight[minNode]) < maxHeight[childNode]:
                maxHeight[childNode] = max(height, maxHeight[minNode])
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)
    # print(maxHeight)
    # print(predecessor)

    # Trace the path from goal to start
    currentNode = goal
    while currentNode != start:
        path.insert(0, currentNode)
        currentNode = predecessor[currentNode]
    path.insert(0, start)
    print('Path: ' + str(path))
    print('Maximum height: ' + str(maxHeight[goal]))

# start and destinationCity can be changed to any other node in the graph
dijkstra(graph, '1', destinationCity)

# Stop the timer and print the runtime
stop = timeit.default_timer()
print('Runtime: ', stop - start)