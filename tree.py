class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children

    def add_child(self, node):
        if node not in self.children:
            self.children.append(node)
            node.parent = self

    def remove_child(self, node):
        self.children.remove(node)
        node.parent = None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        if node == None:
          self._parent = None
          return

        if node == self.parent: 
          return
        if self.parent:
            self.parent.remove_child(self)
        self._parent = node
        node.add_child(self)


    def depth_search(self, value, visited=set()):
        if self == None or self in visited:
          return None
        if self.value == value:
            return self
        else:
          visited.add(self)
          for child in self.children:
            found = child.depth_search(value, visited)
            if found:
              return found

    
    def breadth_search(self, value, queue=[]):
        if self == None:
          return None
        if self.value == value:
            return self
        else:
          queue.extend(self.children)
          return queue.pop(0).breadth_search(value, queue)
