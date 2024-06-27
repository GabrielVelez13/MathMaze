from settings import *
import math

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.angle_rad = math.radians(self.angle)

    def movement(self):
        speed = PLAYER_SPEED * self.game.delta_time

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            if (round(self.angle_rad) == 0):
                self.x += speed
            if (round(self.angle_rad) == 3):
                self.x -= speed
            if (round(self.angle_rad) == 5):
                self.y -= speed
            if  (round(self.angle_rad) == 2):
                self.y += speed

        if keys[pg.K_s]:
            if (round(self.angle_rad) == 0):
                self.x -= speed
            if (round(self.angle_rad) == 3):
                self.x += speed
            if (round(self.angle_rad) == 5) :
                self.y += speed
            if (round(self.angle_rad) == 2):
                self.y -= speed

    def rotate_left(self):
        self.angle -= 90
        self.angle %= 360
        self.angle_rad = math.radians(self.angle)

    def rotate_right(self):
        self.angle += 90
        self.angle %= 360
        self.angle_rad = math.radians(self.angle)

    def draw(self):
        pg.draw.line(self.game.screen, 'red', (self.x * 100, self.y * 100),
                     (self.x * 100 + WIDTH * math.cos(self.angle_rad), self.y * 100 + HEIGHT * math.sin(self.angle_rad)), 2)

        pg.draw.circle(self.game.screen, 'white', (self.x * 100, self.y * 100), 20)
    def update(self):
        self.movement()
    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)