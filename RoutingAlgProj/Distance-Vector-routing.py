import sys

# Class to represent a graph used in Bellman-Ford Alg.
class Graph:
    def __init__(self, nodes):
        self.N = nodes  # No. of nodes
        self.graph = []

    # To add an edge to graph (unidirectional, from u to v):
    def add_edge(self, u, v, w):
        # u:parent node, v:current node w:cost
        self.graph.append([u, v, w])      

    # To generate the lines of the output table:
    def line_list(self, cost, next_node, iteration):
        line_head = 'Iteration'+str(iteration)
        line_list = [line_head]
        for i in range(self.N):
            routing = "(" + str(next_node[i]) + ", " + str(cost[i]) + ")"
            line_list.append(routing)
        return line_list

    # Bellman-Ford algorithm
    # Find shortest distances from all the nodes to the target:
    def bellmanford(self, target):
        # Initialize cost from target to all other nodes as infinite, target to target as O
        # and the parent nodes of all other nodes as -1, of target as itself.
        cost = [float("Inf")] * self.N
        next_node = [int(-1)] * self.N
        cost[target] = int(0)
        next_node[target] = target
        parent_set_iter = [target]
        # Initialization of the output lines
        output_iter = 0
        output_lines = []
        line = self.line_list(cost, next_node, output_iter)
        output_lines.append(line)

        # Relax all edges |N| - 1 times.
        # Update cost value and parent index of the adjacent nodes of
        # the chosen nodes. Only consider those nodes still in queue
        for i in range(self.N - 1):
            parent_set = list(parent_set_iter)           # the parent set only change once per iteration!
            for u, v, w in self.graph:
                if u in parent_set:
                    # use a temp parent set to avoid instant updates
                    # of parent nodes set before one iteration is done
                    parent_set_iter.append(v)
                    parent_set_iter = list(set(parent_set_iter))
                    if cost[u] != float("Inf") and cost[u] + w < cost[v]:
                        cost[v] = cost[u] + w
                        next_node[v] = u
            output_iter = output_iter + 1
            line = self.line_list(cost, next_node, output_iter)
            if (line[1:] == output_lines[-1][1:]) is False:
                output_lines.append(line)

        f = open(table_path,'w')
        # Make the table header
        header = "Iterations"
        for i in range(self.N):
            node_name = "Node" + str(i+1)
            header = header + '\t' + node_name
        f.write(header+'\n')
        # Write the routing information
        for row in output_lines:
            row_str = "\t".join(row)
            f.write('\n')
            f.write(row_str)
        f.close()
        print("Solution has been output in the ./OUTPUT_bellmanford.txt")

# Configuration of path
table_path = './OUTPUT_bellmanford.txt'          # path of output table

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


print("<------ Implement of Bellman-Ford algorithm ------>")
all_nodes = Nodes(config)
target = switches[0]
print("number switches: ", len(switches))
read = Read()
g = Graph(len(switches))
print("---- show switches in this test ----")
for s in switches:
    print("Node : ", s)
print("---- show paths in this test ----")
for path in paths:
    print(paths.index(path), path)

for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] != 0:
            u = i
            v = j
            w = graph[i][j]
            g.add_edge(u, v, w)
g.bellmanford(int(target))

