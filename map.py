from settings import pg


_ = False
mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, 2, _, 1, _, _, _, _, _, _, _, 1],
    [1, _, 1, 1, 1, 1, _, 1, _, 1, 1, _, 1, 1, 1, 1],
    [1, 2, _, _, 2, 1, _, 1, _, _, _, _, 1, _, _, 1],
    [1, 1, 1, 1, _, 1, _, 1, 1, 1, _, _, 1, 1, _, 1],
    [1, 2, _, _, 2, 1, _, _, _, _, _, _, _, _, _, 1],
    [1, _, 1, 1, _, 1, 1, 1, 1, 1, _, _, 1, 1, 1, 1],
    [1, _, 1, _, _, _, _, _, _, 1, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
class Map:
    def __init__(self, Game):
        self.game = Game
        self.map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for y, row in enumerate(self.map):
            for x, tile in enumerate(row):
                if tile == 1:
                    self.world_map[(x, y)] = tile

    def draw(self):
        [pg.draw.rect(self.game.screen, 'teal', (tile[0] * 100, tile[1] * 100, 100, 100), 2) for tile in self.world_map]

