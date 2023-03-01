class ChessPiece:
    def __init__(self, position, colour, captured):
        self.position = position
        self.colour = colour
        self.captured = captured

class Pawn(ChessPiece):
    def __init__(self, position, colour, captured):
        super().__init__(position, colour, captured)

    def move(self, forward, spaces):
        # Check if move is allowed
        new_position = ... # Move according to PAWN rules
        self.position = new_position
