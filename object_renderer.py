from settings import *


class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_texture = self.load_wall_texture()
        self.win_texture = self.load_win_texture()
        self.lose_texture = self.load_lose_texture()
        self.maze_solved = False
        self.player_lost = False
        self.fade_value = 0
        self.background_texture = self.get_texture("Resources/Textures/background2.png", (WIDTH, HALF_HEIGHT))
        self.background_offset = 0

    def load_lose_texture(self):
        return self.get_texture("Resources/Textures/You_lose.png")



    def load_win_texture(self):
        return self.get_texture("Resources/Textures/You_win.png")

    def display_win_or_lose_screen(self, texture):
        screen_width, screen_height = self.screen.get_size()
        scaled_win_texture = pg.transform.scale(texture, (screen_width, screen_height))
        win_surface = pg.Surface((screen_width, screen_height), pg.SRCALPHA)
        win_surface.blit(scaled_win_texture, (0, 0))
        win_surface.set_alpha(self.fade_value)
        self.screen.blit(win_surface, (0, 0))
        if self.fade_value < 500:
            self.fade_value += 5

    def draw(self):
        if self.maze_solved:
            self.game.sound.win_sound.play()
            self.display_win_or_lose_screen(self.win_texture)
        elif self.player_lost:
            self.game.sound.lose_sound.play()
            self.display_win_or_lose_screen(self.lose_texture)
        elif self.game.game_active:
            self.screen.fill((30, 30, 30))
            self.render_objects()
        else:
            self.draw_background()
            self.render_objects()

    def draw_background(self):
        self.background_offset = (self.background_offset + 4 * self.game.player.rel) % WIDTH
        self.screen.blit(self.background_texture, (-self.background_offset, 0))
        self.screen.blit(self.background_texture, (-self.background_offset + WIDTH, 0))

    def render_objects(self):
        list_of_objects = self.game.raycast.objects_to_render
        for depth, wall_column, wall_pos in list_of_objects:
            self.screen.blit(wall_column, wall_pos)

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

    def load_wall_texture(self):
        return {
            1: self.get_texture("Resources/Textures/260x260_Wall.png"),
            2: self.get_texture("Resources/Textures/ending.png")
        }
