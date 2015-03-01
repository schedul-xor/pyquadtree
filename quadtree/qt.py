# -*- coding:utf-8 -*-

class NodeStatus:
    GRAY = 0
    EXISTING_TERMINAL = 1
    EMPTY_TERMINAL = 2
    SURELY_MIXED = 3

class Node:
    def __init__(self,value,status=NodeStatus.GRAY):
        self.value = value
        self.children = [None,None,None,None]
        self.parent = None
        self.status = status
        self.path_cache = []

    def update_child(self,child,slot):
        if self.children[slot] != None:
            self.children[slot].parent = None
        self.children[slot] = child

class Tree:
    def __init__(self):
        self.root = Node(None)
        self.found_appending_status = {
            'i': 0,
            'node': self.root
        }
        
    def find_appending_node(self,adding_path):
        current_node = self.root
        appending_root_node = None
        for i in range(len(adding_path)):
            slot = adding_path[i]
            child_node = current_node.children[slot]
            if child_node == None:
                appending_root_node = current_node
                break
            current_node = child_node
        if appending_root_node == None:
            appending_root_node = current_node
        self.found_appending_status['node'] = appending_root_node
        self.found_appending_status['i'] = i

    def append_rest_of_the_nodes_required(self,adding_path,appending_node,appending_path_index,final_status,value):
        for i in range(appending_path_index,len(adding_path)):
            appending_slot = adding_path[i]
            status = final_status
            if i < len(adding_path)-1:
                status = NodeStatus.GRAY
            new_child_node = Node(None,status)
            appending_node.update_child(new_child_node,appending_slot)
            new_child_node.parent = appending_node
            new_path_cache = appending_node.path_cache[:]
            new_path_cache.append(appending_slot)
            new_child_node.path_cache = new_path_cache

            appending_node = new_child_node
            
        return appending_node

    def merge_parents_from_end(self,end_node):
        while True:
            parent_node = end_node.parent
            if parent_node == None: break
            there_are_still_gray_children_left = False
            found_existing_leaves = 0
            found_empty_leaves = 0
            for i in range(4):
                child = parent_node.children[i]
                if child == None:
                    there_are_still_gray_children_left = True
                else:
                    status = child.status
                    if status == NodeStatus.EXISTING_TERMINAL:
                        found_existing_leaves = found_existing_leaves+1
                    elif status == NodeStatus.EMPTY_TERMINAL:
                        found_empty_leaves = found_empty_leaves+1
                    elif status == Nodestatus.SURELY_MIXED:
                        found_existing_leaves = found_existing_leaves+1
                        found_empty_leaves = found_empty_leaves+1
                    else:
                        there_are_still_gray_children_left = True
                if there_are_still_gray_children_left: break
            if there_are_still_gray_children_left: break
                
            merged = False
            if found_empty_leaves < 1:
                parent_node.status = NodeStatus.EXISTING_TERMINAL
                merged = True
            elif found_existing_leaves < 1:
                parent_node.status = NodeStatus.EMPTY_TERMINAL
                merged = True
            else:
                parent_node.status = NodeStatus.SURELY_MIXED
            
            if merged:
                for i in range(4):
                    parent_node.update_child(None,i)
            
            end_node = parent_node

    def add_terminal(self,adding_path,is_existing,value):
        self.find_appending_node(adding_path)
        appending_path_index = self.found_appending_status['i']
        appending_node = self.found_appending_status['node']
        
        final_status = NodeStatus.EMPTY_TERMINAL
        if is_existing:
            final_status = NodeStatus.EXISTING_TERMINAL
        end_node = self.append_rest_of_the_nodes_required(adding_path,appending_node,appending_path_index,final_status,value)

        self.merge_parents_from_end(end_node)

    def add_gray(self,adding_path):
        self.find_appending_node(adding_path)
        appending_path_index = self.found_appending_status['i']
        appending_node = self.found_appending_status['node']
        end_node = self.append_rest_of_the_nodes_required(adding_path,appending_node,appending_path_index,NodeStatus.GRAY,None)
        
    def for_each_shallow_paths_in_path(self,target_path,callback):
        starting_node = self.root
        is_invalid_path = False
        for starting_index in range(len(target_path)):
            is_terminal = False
            slot = target_path[starting_index]
            found_child = starting_node.children[slot]
            if found_child != None:
                status = found_child.status
                if status == NodeStatus.EXISTING_TERMINAL or status == NodeStatus.EMPTY_TERMINAL:
                    is_terminal = True
                    break
            else:
                is_invalid_path = True
                break
            starting_node = found_child
            if is_terminal: break
            
        if is_invalid_path:
            invalid_root_path = starting_node.path_cache[:]
            invalid_root_path.append(target_path[starting_index])
            callback(invalid_root_path,NodeStatus.GRAY,None)
            return
            
        found_nodes0 = [starting_node]
        found_nodes1 = []
        
        open_nodes = found_nodes0
        closed_nodes = found_nodes1

        while True:
            while len(open_nodes) > 0:
                open_node = open_nodes.pop()
                self.for_each_shallow_paths_in_node(open_node,closed_nodes,callback)
            for open_node in open_nodes:
                closed_nodes.append(open_node)

            if len(closed_nodes) < 1: break
            
            t = closed_nodes
            closed_nodes = open_nodes
            open_nodes = t
        
            closed_nodes = []

    def for_each_shallow_paths_in_node(self,node,found_children,callback):
        path_cache = node.path_cache
        node_status = node.status

        if node_status == NodeStatus.EXISTING_TERMINAL or node_status == NodeStatus.EMPTY_TERMINAL:
            value = node.value
            callback(path_cache,node_status,value)
        elif node_status == NodeStatus.SURELY_MIXED:
            for i in range(4):
                child = node.children[i]
                found_children.append(child)
        elif node_status == NodeStatus.GRAY:
            for i in range(4):
                child = node.children[i]
                if child == None:
                    path_cache.append(i)
                    callback(path_cache,NodeStatus.GRAY,None)
                    path_cache.pop()
                else:
                    found_children.append(child)

    def status_for_path(self,path):
        self.find_appending_node(path)
        appending_node = self.found_appending_status['node']
        if appending_node == None:
            return NodeStatus.GRAY
        return appending_node.status

    def value_for_path(self,path):
        self.find_appending_node(path)
        appending_node = self.found_appending_status['node']
        if appending_node == None:
            return None
        return appending_node.value
