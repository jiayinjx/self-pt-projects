import sys                      #read arguments from console
import socket                   #socket programing
import json                     #sending and recieving packets
import subprocess

print("------ Start ------")
# Description: Implement two routing algorithms: (link-state routing and distance vector routing) via Python
# Input: A .txt file in the following format:
#   Node <X>
#   <connected node> <cost>
#   Node <Y>
#   <connected node> <cost>
#   …
# Output: output the solution in file. The least cost path.

# read in .txt file with command
# cmd: "python Routing nodeFile.txt"
#
# #variables used

config = sys.argv[1]
switch_num = 0
switches = []
path_map = [[(float('inf'),None) for j in range(switch_num)] for i in range(switch_num)]

# Nodes Class
class Node:
    def __init__(self, current_node_info):
        self.curr_node = current_node_info[0]
        self.neighbor = []
        # num_curr_neighbor = (len(current_node_info)-1)/2
        current_node_info = current_node_info[1:]
        i = 0
        while i < len(current_node_info):
            this_neighbor = [current_node_info[i], current_node_info[i+1]]
            self.neighbor.append(this_neighbor)
            i += 2
        print("node", self.curr_node, self.neighbor)

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

        # print("---- read nodes ----")
        # print(items)
        rangeIdx = []

        i = 0
        while i < len(items):
            if items[i] == 'Node':
                rangeIdx.append(i)
            i += 1
        lastNodeIdx = rangeIdx[len(rangeIdx)-1]
        r = 0
        while r+1 < len(rangeIdx):
            str = rangeIdx[r]+1
            end = rangeIdx[r+1]
            node = Node(items[str: end])
            r += 1
        
        node = Node(items[lastNodeIdx+1: len(items)])
        nodes.append(node)
        switch_num = rangeIdx


all_nodes = Nodes(config)
print("(float('inf'),None)", float('inf'))