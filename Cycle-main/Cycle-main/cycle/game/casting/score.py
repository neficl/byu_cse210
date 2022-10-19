from game.casting.actor import Actor


class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
        _test (string): Text given previously
    """
    def __init__(self):
        """Creates and tracks the score
        
        Args:
            super().__init__(): Initiates the Actor class
            _points: tracks the points for the game."""
        super().__init__()
        self._points = 0

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points

    def get_points(self):
        """Gets self._points
        
        Returns:
            _points: the point value
        """

        return self._points