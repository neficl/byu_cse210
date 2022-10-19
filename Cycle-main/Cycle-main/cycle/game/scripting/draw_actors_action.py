from game.scripting.action import Action
from game.shared.point import Point

class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score1 = cast.get_first_actor("score1")
        score2 = cast.get_first_actor("score2")
        score2.set_text("Player Two: %d" % (score2.get_points()))
        score1.set_text("Player One: %d" % (score1.get_points()))
        snake1 = cast.get_first_actor("snake1")
        snake2 = cast.get_first_actor("snake2")
        body1 = snake1.get_segments()
        body2 = snake2.get_segments()
        segments = []
        for piece in body1:
            segments.append(piece)
        for piece in body2:
            segments.append(piece)

        score2.set_position(Point(785,0))

        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_actors(segments)
        self._video_service.draw_actor(score1)
        self._video_service.draw_actor(score2)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()