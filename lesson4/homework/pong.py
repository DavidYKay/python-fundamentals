import cocos
from cocos.director import director

PADDLE_SPEED = 12
AI_PADDLE_SPEED = 5
TIME_TICK = 0.1
TIME_PER_FRAME = 1.0 / 60

MIN_X = 0
MAX_X = 600
MIN_Y = 0
MAX_Y = 600

BALL_SIZE = (48, 48)
PADDLE_SIZE = (20, 80)
INITIAL_BALL_VELOCITY = (5, 2)

def axis_overlapping(min_a, max_a, min_b, max_b):
    """Are these two ranges overlapping each other?"""
    ## TODO: Implement this
    return False

def colliding(a, b):
    """Is A colliding with B?"""
    ## TODO: Implement this. It may help to use axis_overlapping.
    return False

def bounce(ball, paddle):
    """Given a ball and a paddle, send the ball bouncing away with a new velocity."""
    ball.velocity = (-ball.velocity[0], -ball.velocity[1])

def avg(nums):
    """Take a list of numbers and calculate the mean."""
    return sum(nums) / len(nums)

class PongLayer(cocos.layer.Layer):
    is_event_handler = True
    def __init__(self):
        """Runs when we create a ball layer"""
        super(PongLayer, self).__init__()

        self.elapsed = 0

        self.ball = cocos.sprite.Sprite("images/pokeball.png")
        self.ball.size = BALL_SIZE
        self.ball.velocity = INITIAL_BALL_VELOCITY

        self.paddle_a = cocos.sprite.Sprite("images/paddle_a.png")
        self.paddle_b = cocos.sprite.Sprite("images/paddle_b.png")

        self.add(self.ball)
        self.add(self.paddle_a)
        self.add(self.paddle_b)

        mid_y = avg([MAX_Y, MIN_Y])
        self.ball.position = (avg([MAX_X, MIN_X]), mid_y)
        self.paddle_a.velocity = (0, 0)
        self.paddle_a.position = (MIN_X + PADDLE_SIZE[0], mid_y)
        self.paddle_b.position = (MAX_X - PADDLE_SIZE[0], mid_y)
        self.paddle_a.size = PADDLE_SIZE
        self.paddle_b.size = PADDLE_SIZE

        self.schedule(self.update_game_state)

    def update_game_state(self, delta_time):
        """Fires as often as possible"""
        # Record how long it's been since the last time we ran this function
        self.elapsed += delta_time
        # Have we waited long enough to update the game state? Some computers are very fast and should wait so that our game doesn't run absurdly fast.
        if self.elapsed > TIME_PER_FRAME:
            self.elapsed = 0
            # Update the ball's position
            self.ball.position = (self.ball.position[0] + self.ball.velocity[0], self.ball.position[1] + self.ball.velocity[1])

            # TODO: Make the ball bounce off of the top / bottom boundaries
            # TODO: Make the ball bounce off of each player's paddle
            # TODO: If the ball runs off the left or right side of the screen, reset the ball's position
            # TODO: Make the computer's paddle move towards the position of the ball, at the speed of AI_PADDLE_SPEED

        else:
            # We haven't waited long enough. Let's not update the game state
            print("%s was less than %s" % (self.elapsed, TIME_PER_FRAME))

    def on_key_press(self, key, modifiers):
        """Fires when a key is pressed"""
        if key == 65362:
            # up arrow pressed
            # TODO: Move the player's paddle up
            pass
        elif key == 65364:
            # down arrow pressed
            # TODO: Move the player's paddle down
            pass
        else:
            print("(ball) unknown key pressed:", key)

    def on_key_release(self, key, modifiers):
        """Fires when a key is released"""
        print("released key:", key)
        self.paddle_a.velocity = (0, 0)

if __name__ == '__main__':
    director.init(resizable=True)
    director.run(cocos.scene.Scene(PongLayer()))
