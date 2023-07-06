import turtle as t

writer = t.Turtle()


class Object2D:
    def __init__(self, pos=[0,0], shape="square", width=2, height=2, dx=0, dy=0, color="white"):
        self.pos, self.shape, self.width, self.height = pos, shape, width, height
        self.dx, self.dy = dx, dy
        self.color = color


class Pong:
    def __init__(self):
        self.board_size = [800, 540]
        self.playerL = Object2D(pos=[-350, 0], width=4, height=1)
        self.playerR = Object2D(pos=[350, 0], width=4, height=1)
        self.ball = Object2D(pos=[0,0], width=1, height=1, shape="circle", color="orange", dx=0.15, dy=0.15)

    # MEMBER-3/4
    # player move functions
    def playerL_up(self):
        self.playerL.pos[1] += 10
        writer.clear(); writer.write("playerL_up"+str(self.playerL.pos))

    def playerR_up(self):
        self.playerR.pos[1] += 10
        writer.clear(); writer.write("playerR_up"+str(self.playerR.pos))

    def playerL_down(self):
        self.playerL.pos[1] -= 10
        writer.clear(); writer.write("playerL_down"+str(self.playerL.pos))

    def playerR_down(self):
        self.playerR.pos[1] -= 10
        writer.clear(); writer.write("playerR_down"+str(self.playerR.pos))

    # MEMBER 2
    def update_ball_pos(self):
        # update ball.pos following dx, dy
        # ...
        writer.clear(); writer.write("ball_pos"+str(self.ball.pos))

    def check_ball_pos(self):
        game_end = False
        if not self.process_player_hit():
            if self.process_fall():
                game_end = True
            else:
                self.process_border_hit()
        return game_end

    # MEMBER 3
    def process_player_hit(self):
        # let's say: diff = difference between ball.pos and  player.pos
        # if diff_x is below 20 and diff_y is below 70 (for either player), consider this a player-hit
        # if a player-hit occurs, return True and reverse the ball direction along x-axis.
        # ...
        return False

    # MEMBER 2
    def process_fall(self):
        # ball falls, if ball goes beyond 350 (or -350) along x-axis
        # if a fall is detected, return True
        # ...
        return False

    # MEMBER 3
    def process_border_hit(self):
        # border-hit occurs when ball moves beyond 250 (or -250) along y-axis
        # if a border-hit is detected, return True and reverse the ball direction along y-axis
        # ...
        return False


class Simulate:
    def __init__(self, pong):
        self.pong = pong
        self.window = window = t.Screen()
        window.title("The Pong Game")
        window.bgcolor("green")
        window.setup(width=self.pong.board_size[0], height=self.pong.board_size[1])
        window.tracer(0)

        self.ball = self.draw_obj(self.pong.ball)
        self.playerL = self.draw_obj(self.pong.playerL)
        self.playerR = self.draw_obj(self.pong.playerR)

        self.window.update()
        self.bind_keys()

    def bind_keys(self):
        self.window.listen()
        self.window.onkey(self.pong.playerL_up, "w")
        self.window.onkey(self.pong.playerL_down, "s")
        self.window.onkey(self.pong.playerR_up, "Up")
        self.window.onkey(self.pong.playerR_down, "Down")

    def draw_obj(self, obj):
        ob = t.Turtle()
        ob.speed(0)
        ob.shape(obj.shape)
        ob.color(obj.color)
        ob.shapesize(obj.width, obj.height, 0)
        ob.penup()
        ob.goto(obj.pos[0], obj.pos[1])
        return ob

    # MEMBER 1
    def update_obj(self):
        # update position of all simulation objects using obj.goto(posx, posy)
        # ...
        self.window.update()


pong = Pong()
sim = Simulate(pong)

# MEMBER-1
while True:
    game_over = False
    # update ball_pos in the pong object
    # ...
    sim.update_obj()
    # check ball_pos and decide game_over
    # ...
    if game_over:
        break

writer.clear(); writer.write("Game Over")
t.done()

