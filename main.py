from settings import *
from map import *
from player import *


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 0
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)

    def update(self):
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.2f}')
        self.player.update()

    def draw(self):
        self.screen.fill('black')
        self.map.draw()
        self.player.draw()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    self.player.rotate_left()
                if event.key == pg.K_d:
                    self.player.rotate_right()
    def run(self):
        while True:
            self.events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()