from sprites import *


class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        add_sprite = self.add_sprite


        self.setup_sprites()

    def get_sprite_by_identifier(self, identifier):
        for sprite in self.sprite_list:
            if sprite.identifier == identifier:
                return sprite
        return None

    def setup_sprites(self):
        self.add_sprite(AnimatedSprite(self.game, "sprite1"))

    def update(self):
        [sprite.update() for sprite in self.sprite_list]

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)