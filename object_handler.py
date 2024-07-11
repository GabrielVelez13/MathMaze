from sprites import *


class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.setup_sprites()

    def get_sprite_by_identifier(self, identifier):
        for sprite in self.sprite_list:
            if sprite.identifier == identifier:
                return sprite
        return None

    def setup_sprites(self):
        self.add_sprite(AnimatedSprite(self.game, "sprite1", (4.4, 7.5)))
        self.add_sprite(AnimatedSprite(self.game, "sprite2", (8.4, 1.5)))
        self.add_sprite(AnimatedSprite(self.game, "sprite3", (8.4, 7.5)))
        self.add_sprite(AnimatedSprite(self.game, "sprite4", (13.4, 1.5)))
        self.add_sprite(AnimatedSprite(self.game, "sprite5", (14.4, 4.5)))

    def update(self):
        [sprite.update() for sprite in self.sprite_list]

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)
