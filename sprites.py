from settings import *
from collections import deque
import os

class Sprites:
    def __init__(self, game, path='Resources/Sprites/Bringer-Of-Death/Individual Sprite/Idle/Bringer-of-Death_Idle_1.png',
                 pos=(1.5, 1.5), scale=0.7, shift=0.27):
        self.game = game
        self.player = game.player
        self.x, self.y = pos
        self.image = pg.image.load(path).convert_alpha()
        self.IMAGE_WIDTH = self.image.get_width()
        self.IMAGE_HALF_WIDTH = self.image.get_width() // 2
        self.IMAGE_RATIO = self.IMAGE_WIDTH / self.image.get_height()
        self.dx, self.dy, self.theta, self.screen_x, self.dist, self.norm_dist = 0, 0, 0, 0, 1, 1
        self.sprite_half_width = 0
        self.SPRITE_SCALE = scale
        self.SPRITE_HEIGHT_SHIFT = shift

    def get_sprite_projection(self):
        proj = SCREEM_DIST / self.norm_dist * self.SPRITE_SCALE
        proj_width, proj_height = proj * self.IMAGE_RATIO, proj

        image = pg.transform.scale(self.image, (proj_width, proj_height))

        self.sprite_half_width = proj_width // 2
        height_shift = proj_height * self.SPRITE_HEIGHT_SHIFT
        pos = self.screen_x - self.sprite_half_width, HEIGHT // 2 - proj_height // 2 + height_shift

        self.game.raycast.objects_to_render.append((self.norm_dist, image, pos))

    def is_visible(self, dx, dy):
        # Perform a simplified raycast from the player to the sprite
        steps = max(abs(dx), abs(dy)) * 2  # Increase steps for higher accuracy
        step_dx, step_dy = dx / steps, dy / steps
        test_x, test_y = self.player.x, self.player.y

        for _ in range(int(steps)):
            test_x += step_dx + .1
            test_y += step_dy + .1
            if (int(test_x), int(test_y)) in self.game.map.world_map:
                return False  # Wall is blocking the sprite
        return True

    def get_sprite(self):
        dx = self.x - self.player.x
        dy = self.y - self.player.y
        self.dx, self.dy = dx, dy
        self.theta = math.atan2(dy, dx)

        delta = self.theta - self.player.angle
        if (dx > 0 and self.player.angle > math.pi) or (dx < 0 and dy < 0):
            delta += math.tau

        delta_rays = delta / DELTA_ANGLE
        self.screen_x = ((NUM_RAYS // 2) + delta_rays) * SCALE

        self.dist = math.hypot(dx, dy)
        self.norm_dist = self.dist * math.cos(delta)
        if -self.IMAGE_HALF_WIDTH < self.screen_x < (WIDTH + self.IMAGE_HALF_WIDTH) and self.norm_dist > 0.5:
            if self.is_visible(dx, dy):
                self.get_sprite_projection()

    def update(self):
        self.get_sprite()


class AnimatedSprite(Sprites):
    def __init__(self, game, path='Resources/Sprites/Bringer-Of-Death/Individual Sprite/Idle/Bringer-of-Death_Idle_1.png',
                 pos=(2.5, 3.5), scale=0.8, shift=0.16, animation_time=120):
        super().__init__(game, path, pos, scale, shift)
        self.animation_time = animation_time
        self.path = path.rsplit('/', 1)[0]
        self.images = self.get_images(self.path)
        self.animation_time_prev = pg.time.get_ticks()
        self.animation_trigger = False

    def update(self):
        super().update()
        self.check_animation_time()
        self.animate(self.images)

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
