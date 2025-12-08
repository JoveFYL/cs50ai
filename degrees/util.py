class Node():
    def __init__(self, parent, id, movie_id):
        # self.state = state
        self.parent = parent
        self.id = id
        self.movie_id = movie_id

    def get_id(self):
        return self.id

    def get_movie_id(self):
        return self.movie_id

    def get_parent(self):
        return self.parent

class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):

        self.frontier.append(node)

    # def contains_state(self, state):
    #     return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
