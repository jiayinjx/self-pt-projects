import sys

# Class to represent a graph used in Dijkstra's Alg.
class Graph:
    # To find the nodes with minimum distance(cost), from the queue of nodes with undetermined distance:
    def min_cost(self, cost, queue):
        # Initialize variables: min value to infinite and min_idx as -1
        min = float("Inf")
        min_idx = -1
        # from the cost array, pick the one which has the min value and is still in the queue
        for i in range(len(cost)):
            if i in queue and cost[i] < min:
                min = cost[i]
                min_idx = i
        return min_idx

    # To generate the lines of the output table:
    def line_list(self, set, cost, iteration):
        line_header = 'Iteration' + str(iteration)
        line_list = [line_header]
        for i in range(len(cost)):
            routing = str(cost[i])
            line_list.append(routing)
        line_list.append(str(set))
        return line_list

    # Dijkstra's algorithm
    # Find shortest distances(cost) from all the nodes to the target
    def dijkstra(self, graph, target):
        row = len(graph)
        col = len(graph[0])

        # cost[i] will hold the shortest distance(cost) from target to i
        # Initialize all distances to infinite:
        cost = [float("Inf")] * row

        # Distance of target node from itself is always 0:
        cost[target] = 0

        # Add all nodes in the to-be-determined queue, make a empty set for those who has already found ones
        queue = []
        for i in range(row):
            queue.append(i)
        found_set = []
        output_lines = []

        # Find shortest path for all nodes:
        while queue:
            # Pick the minimum dist(cost) node from the queue
            u = self.min_cost(cost, queue)   # the found node!

            # add already found nodes into set and remove it from the queue
            found_set.append(u)
            found_set.sort()
            queue.remove(u)

            # Update cost[j] only if it is in queue, there is an edge from founded node u
            # to current node j, and total weight of path from target to current j through
            # founded u is smaller than current value of cost[j]
            for j in range(col):
                if graph[u][j] and j in queue:
                    if cost[u] + graph[u][j] < cost[j]:
                        cost[j] = cost[u] + graph[u][j]
            line = self.line_list(found_set, cost, len(found_set)-1)
            output_lines.append(line)

        # Output the result into the txt, in a table form as the PPT shows.
        f = open(table_path, 'w')
        # Make the table header
        header = "Iterations"
        for i in range(row):
            # node_name = "Node" + str(i)
            node_name = "Node" + str(i+1)
            header = header + '\t' + node_name
        header = header + '\t' + "Set N"
        f.write(header + '\n')
        # Write the routing information
        for row in output_lines:
            row_str = "\t".join(row)
            f.write('\n')
            f.write(row_str)
        f.close()
        print("Solution has been output in the ./OUTPUT_dijkstra.txt")

# Configuration of path
table_path = './OUTPUT_dijkstra.txt'          # path of output table

config = sys.argv[1]
paths = []
switches = []
graph = []


class Node:
    def __init__(self, current_node_info):
        self.curr_node = current_node_info[0]
        self.neighbors = []
        current_node_info = current_node_info[1:]
        i = 0
        while i < len(current_node_info):
            this_neighbor = [current_node_info[i], int(current_node_info[i+1])]
            self.neighbors.append(this_neighbor)
            i += 2
        path = []
        for neighbor in self.neighbors:
            path = [self.curr_node]
            path.append(neighbor[0])
            path.append(neighbor[1])
            paths.append(path)


class Nodes:
    def __init__(self, config):
        global config_file
        config_file = {}
        #reading file
        fo = open(config, "r+")
        data = fo.read()
        items = (data.split())

        global nodes
        nodes = []

        switchIdx = []

        i = 0
        while i < len(items):
            if items[i] == 'Node':
                switchIdx.append(i)
            i += 1
        lastNodeIdx = switchIdx[len(switchIdx)-1]
        r = 0
        while r+1 < len(switchIdx):
            str = switchIdx[r]
            end = switchIdx[r+1]
            node = Node(items[str+1: end])
            nodes.append(node)
            r += 1

        node = Node(items[lastNodeIdx+1: len(items)])
        nodes.append(node)
       
        for path in paths:
            if path[0] not in switches:
                switches.append(path[0])
            if path[1] not in switches:
                switches.append(path[1])


class Read:
    def __init__(self):
        cost_table = [[0 for x in range(len(switches))] for y in range(len(switches))] 
        for path in paths:
            cost_table[int(path[0])-1][int(path[1])-1] = path[2]
            cost_table[int(path[1])-1][int(path[0])-1] = path[2]
        # print("2 5 4 : ", cost_table[1][4])
        # print("1 3 2 : ", cost_table[0][2])
        row_idx = 0
        while row_idx < len(cost_table):
            cost_table[row_idx] = list(map(int, cost_table[row_idx]))
            graph.append(cost_table[row_idx])
            row_idx += 1
       

print("<------ Implement of Dijkstra's algorithm ------>")
all_nodes = Nodes(config)
target = switches[0]
read = Read()
print("---- show switches in this test ----")
for s in switches:
    print("Node : ", s)
print("---- show paths in this test ----")
for path in paths:
    print(paths.index(path), path)

g = Graph()
g.dijkstra(graph, int(target))

  
