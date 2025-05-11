
class Node():
    def __init__(self, state, parent, action, cost = 0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost


class StackFrontier():
    # The frontier is a stack of nodes
    # The stack is a LIFO (Last In First Out) data structure
    # The last node added to the stack is the first one to be removed

    def __init__(self):
        self.frontier = []

    # add a node to the frontier
    def add(self, node):
        self.frontier.append(node)

    # return if the state is in the frontier
    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)
    
    # return if the frontier is empty
    def empty(self):
        return len(self.frontier) == 0
    
    # remove the last node added to the frontier
    def remove(self):
        if self.empty():
            raise Exception("Empty frontier")
        else:
            return self.frontier.pop()
        
class QueueFrontier(StackFrontier):
    # The frontier is a queue of nodes
    # The queue is a FIFO (First In First Out) data structure
    # The first node added to the queue is the first one to be removed

    # remove the first node added to the frontier
    def remove(self):
        if self.empty():
            raise Exception("Empty frontier")
        else:
            return self.frontier.pop(0)
        

class customFrontier(StackFrontier):
    def remove(self, metric):
        if self.empty():
            raise Exception("Empty frontier")
        self.costs = []
        for node in self.frontier:
            self.costs.append(metric(node.state))
        min_cost = min(self.costs)
        min_index = self.costs.index(min_cost)
        node = self.frontier[min_index]
        self.frontier.remove(node)
        return node
    
class AlphaFrontier(StackFrontier):
    def remove(self, metric):
        if self.empty():
            raise Exception("Empty frontier")
        self.costs = []
        for node in self.frontier:
            self.costs.append(metric(node.state)+node.cost)
        min_cost = min(self.costs)
        min_index = self.costs.index(min_cost)
        node = self.frontier[min_index]
        self.frontier.remove(node)
        return node