from tree import Node


class KnightPathFinder:
    def __init__(self, position):
        self._root = Node(position)
        self._considered_positions = set((position,))

    def get_valid_moves(self, pos):
        deltas = ((1, 2), (1, -2), (2, 1), (2, -1),
                  (-1, 2), (-1, -2), (-2, 1), (-2, -1))
        moves = [(pos[0] + x, pos[1] + y)
                 for (x, y) in deltas
                 if pos[0] + x >= 0 and pos[0] + x < 8
                 and pos[1] + y >= 0 and pos[1] + y < 8]
        return moves

    def new_move_positions(self, pos):
        new_moves = [position for position in self.get_valid_moves(pos)
                     if position not in self._considered_positions]
        self._considered_positions.update(new_moves)
        return new_moves


    def build_move_tree(self):
      nodes = [self._root]
      while nodes:
        node = nodes.pop(0)
        moves = self.new_move_positions(node.value)
        children = [Node(pos) for pos in moves]
        for child in children:
          node.add_child(child)
        nodes.extend(children)


finder = KnightPathFinder((0, 0))
finder.build_move_tree()
print(finder._root.children)
