from settings import *


class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_texture = self.load_wall_texture()

    def draw(self):
        self.render_objects()


    def render_objects(self):
        list_of_objects = self.game.raycast.objects_to_render
        for depth, wall_column, wall_pos in  list_of_objects:
            self.screen.blit(wall_column, wall_pos)


    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

    def load_wall_texture(self):
        return {
            1: self.get_texture('Resources/Textures/260x260_Wall.png'),
        }
