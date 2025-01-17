from settings import *


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.moving = True
        self.player_health = 75
        self.rel = 0

    def is_alive(self):
        return self.player_health > 0

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos

        self.wall_collision(dx, dy)

        if keys[pg.K_LEFT]:
            self.angle -= PLAYER_ROTATION * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_ROTATION * self.game.delta_time
        self.angle %= math.tau

    def mouse_control(self):
        mx, my = pg.mouse.get_pos()
        if mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT:
            pg.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])
        self.rel = pg.mouse.get_rel()[0]
        self.rel = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel))
        self.angle += self.rel * MOUSE_SENSITIVITY * self.game.delta_time

    def check_wall(self, x, y):
        if (x, y) in self.game.map.world_map:
            if self.game.map.world_map[(x, y)] == 2:
                self.game.object_renderer.maze_solved = True
                return False
        return (x, y) not in self.game.map.world_map

    def wall_collision(self, dx, dy):
        scale = PLAYER_SIZE_SCALE / (self.game.delta_time + 0.00001)
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy

    def update(self):
        if self.moving:
            self.mouse_control()
            self.movement()
        if not self.is_alive():
            self.game.game_active = True
            self.game.object_renderer.player_lost = True

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)
