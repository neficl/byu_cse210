import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.
    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction.
        
        Args:
            _is_game_over (boolean): declares whether the game has ended.
        """
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.
        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        
        snake1 = cast.get_first_actor("snake1")
        snake2 = cast.get_first_actor("snake2")
        
        if not self._is_game_over:
            snake1.grow_tail(1,constants.RED)
            snake2.grow_tail(1,constants.GREEN)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)
        else: 
            snake1.grow_tail(1,constants.WHITE)
            snake2.grow_tail(1,constants.WHITE)
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score1 = cast.get_first_actor("score1")
        score2 = cast.get_first_actor("score2")
        snake1 = cast.get_first_actor("snake1")
        snake2 = cast.get_first_actor("snake2")
        head1 = snake1.get_segments()[0]
        head2 = snake2.get_segments()[0]
        body1 = snake1.get_segments()[1:]
        body2 = snake2.get_segments()[1:]

        segments = []
        for piece in body1:
            segments.append(piece)
        for piece in body2:
            segments.append(piece)

        
        for segment in segments:
            if head1.get_position().equals(segment.get_position()):
                self._is_game_over = True
                score2.add_points(1)
                score2.set_text("Player Two: %d" % (score2.get_points()))
            if head2.get_position().equals(segment.get_position()):
                self._is_game_over = True
                score1.add_points(1)
                score1.set_text("Player One: %d" % (score1.get_points()))
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            snake1 = cast.get_first_actor("snake1")
            snake2 = cast.get_first_actor("snake2")
            body1 = snake1.get_segments()
            body2 = snake2.get_segments()
            segments = []

            for piece in body1:
                segments.append(piece)
            for piece in body2:
                segments.append(piece)

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            # Overriding the font size for "Game over"
            message.set_font_size(45)
            cast.add_actor("messages", message)

            for segment in segments:
                segment.set_color(constants.WHITE)