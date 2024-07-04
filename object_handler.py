from sprites import *


class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        add_sprite = self.add_sprite


        add_sprite(Sprites(game))
        add_sprite(AnimatedSprite(game))
    def update(self):
        [sprite.update() for sprite in self.sprite_list]

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)