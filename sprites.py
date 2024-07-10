from settings import *
from collections import deque
import os

class Sprites:
    def __init__(self, game, identifier, path='Resources/Sprites/Bringer-Of-Death/Individual Sprite/Idle/Bringer-of-Death_Idle_1.png',
                 pos=(1.5, 1.5), scale=0.7, shift=0.27, health=100):
        self.game = game
        self.player = game.player
        self.identifier = identifier
        self.x, self.y = pos
        self.image = pg.image.load(path).convert_alpha()
        self.IMAGE_WIDTH = self.image.get_width()
        self.IMAGE_HALF_WIDTH = self.image.get_width() // 2
        self.IMAGE_RATIO = self.IMAGE_WIDTH / self.image.get_height()
        self.dx, self.dy, self.theta, self.screen_x, self.dist, self.norm_dist = 0, 0, 0, 0, 1, 1
        self.sprite_half_width = 0
        self.SPRITE_SCALE = scale
        self.SPRITE_HEIGHT_SHIFT = shift
        self.health = health


    def get_sprite_projection(self):
        proj = SCREEM_DIST / self.norm_dist * self.SPRITE_SCALE
        proj_width, proj_height = proj * self.IMAGE_RATIO, proj

        image = pg.transform.scale(self.image, (proj_width, proj_height))

        self.sprite_half_width = proj_width // 2
        height_shift = proj_height * self.SPRITE_HEIGHT_SHIFT
        pos = self.screen_x - self.sprite_half_width, HEIGHT // 2 - proj_height // 2 + height_shift

        self.game.raycast.objects_to_render.append((self.norm_dist, image, pos))

    def is_alive(self):
        return self.health > 0

    def is_visible(self, dx, dy):
        steps = max(abs(dx), abs(dy)) * 2
        step_dx, step_dy = dx / steps, dy / steps
        test_x, test_y = self.player.x, self.player.y

        for _ in range(int(steps)):
            test_x += step_dx
            test_y += step_dy
            if (int(test_x), int(test_y)) in self.game.map.world_map:
                return False

        return True

    def get_sprite(self):
        dx = self.x - self.player.x
        dy = self.y - self.player.y
        self.dx, self.dy = dx, dy
        self.theta = math.atan2(dy, dx)

        delta = self.theta - self.player.angle
        if (dx > 0 and self.player.angle > math.tau) or (dx < 0 and dy < 0):
            delta += math.tau

        delta_rays = delta / DELTA_ANGLE
        self.screen_x = ((NUM_RAYS // 2) + delta_rays) * SCALE

        self.dist = math.hypot(dx, dy)
        self.norm_dist = self.dist * math.cos(delta)
        if -self.IMAGE_HALF_WIDTH < self.screen_x < (WIDTH + self.IMAGE_HALF_WIDTH) and self.norm_dist > 0.5:
            if self.is_visible(dx, dy) and self.is_alive():
                self.get_sprite_projection()
                self.rotate_player_to_sprite()
                # Trigger gameplay if the sprite is visible and the game is not already active
                if not self.game.game_active:
                    self.game.start_combat(self.identifier)


    def rotate_player_to_sprite(self):
        sprite_direction = math.atan2(self.y - self.player.y, self.x - self.player.x)
        player_angle_normalized = self.player.angle % math.tau
        sprite_direction_normalized = sprite_direction % math.tau
        clockwise = (sprite_direction_normalized - player_angle_normalized) % math.tau
        counterclockwise = (player_angle_normalized - sprite_direction_normalized) % math.tau
        if clockwise < counterclockwise:
            self.player.angle += clockwise
        else:
            self.player.angle -= counterclockwise


    def update(self):
        self.get_sprite()


class AnimatedSprite(Sprites):
    def __init__(self, game, identifier, path=IDLE_ANIMATION,
                 pos=(2.5, 3.2), scale=0.8, shift=0.16, health=100, animation_time=120):
        super().__init__(game, identifier, path, pos, scale, shift, health)
        self.animation_time = animation_time
        self.path = path.rsplit('/', 1)[0]
        self.images = self.get_images(self.path)
        self.animation_time_prev = pg.time.get_ticks()
        self.animation_trigger = False
        self.health = health
        self.death = self.get_images(DEATH_ANIMATION)
        self.death_animation_played = False


    def update(self):
        super().update()
        self.check_animation_time()
        if self.is_alive():
            self.animate(self.images)
        else:
            self.animate(self.death)

    def animate(self, images):
        if self.animation_trigger:
            images.rotate(-1)
            self.image = images[0]

    def check_animation_time(self):
        self.animation_trigger = False
        time_now = pg.time.get_ticks()
        if time_now - self.animation_time_prev > self.animation_time:
            self.animation_time_prev = time_now
            self.animation_trigger = True

    def get_images(self, path):
        images = deque()
        for file_name in os.listdir(path):
            if os.path.isfile(os.path.join(path, file_name)):
                img = pg.image.load(path + '/' + file_name).convert_alpha()
                images.append(img)
        return images
