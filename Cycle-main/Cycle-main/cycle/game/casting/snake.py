import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Red_Snake(Actor):
    """
    A long limbless reptile.
    The responsibility of Snake is to move itself.
    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        """Initiates the Red_Snake(Actor) class.
        Args:
            super(): Inherits the Actor class.
            _segments (list): the list of segments to track the body
            _prepare_body (method): sets the position and velocity of the body.
        """
        super().__init__()
        self._segments = []
        self._prepare_body()

    def get_segments(self):
        """Gets the segments of the body
        
        Returns:
            _segments (list): the different segments of the body.
        """
        return self._segments

    def move_next(self):
        """Moves the positions of the segments and updates the velocities.
        
        Args:
            _segments (list): the different segments of the body."""
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) -1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        """Get's the head's position.
        
        Returns: 
            _segments[0] (list): The position of the head."""
        return self._segments[0]

    def grow_tail(self, number_of_segments, color):
        """Continually adds segments to the body to allow the snake to grow.
        
        Args: 
            _segments (list): the segments of the snake's body
        """
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(color)
            self._segments.append(segment)

    def turn_head(self, velocity):
        """Changes the velocity of the head.
        
        Args:
            _segments[0] (list): The head.
        """
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        """Tracks the individual segments of the snake's body.
        
        Args: 
            _segments (list): the different segments of the snake's body."""
        x = int(constants.MAX_X / 4)
        y = int(constants.MAX_Y / 2)

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x, y + i * constants.CELL_SIZE)
            velocity = Point(0,-1 * constants.CELL_SIZE)
            text = "@" if i == 0 else "#"
        
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(constants.RED)
            self._segments.append(segment)