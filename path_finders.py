from tree import Node

class KnightPathFinder:
  def __init__(self, position):

    self._root = Node(position)

    self._considered_positions = set((position,))

  def get_valid_moves(self, pos) :
    deltas = ((1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1))

    moves = [ (pos[0]+ x, pos[1] + y)
              for (x, y) in deltas
              if pos[0] + x >= 0 and pos[0] + x < 8
              and pos[1] + y >= 0 and pos[1] + y < 8 ]

    return moves

  def new_move_positions(self, pos):
    newMoves = [ position for position in self.get_valid_moves(pos) if position not in self._considered_positions ]
    self._considered_positions.update(newMoves)
    return newMoves

knight = KnightPathFinder((0, 0))

print(knight.new_move_positions((0, 0)))
print(knight.new_move_positions((1, 2)))
print(knight.new_move_positions((7, 7)))
print(knight.new_move_positions((6, 5)))
