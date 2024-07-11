from settings import *
from map import Map
from player import Player
from raycasting import Raycasting
from object_renderer import ObjectRenderer
from object_handler import ObjectHandler
from random import randint
from sound import Sound


class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 0
        self.current_input = ""
        self.question = ""
        self.answer = 0
        self.game_active = False
        self.feedback_color = None
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycast = Raycasting(self)
        self.object_handler = ObjectHandler(self)
        self.sound = Sound(self)
        self.sound.game_sound.play()

    def generate_question(self):
        num1 = randint(1, 12)
        num2 = randint(1, 12)
        self.answer = num1 * num2
        self.question = f"What is {num1} * {num2}?"
        self.game_active = True
        self.player.moving = False

    def draw_text_box(self, text, y):
        font = pg.font.Font("Resources/Old London font/OldLondon.ttf", 36)
        text_surf = font.render(text, True, pg.Color('white'))
        text_rect = text_surf.get_rect(center=(RES[0] // 2, y))
        pg.draw.rect(self.screen, pg.Color('black'), text_rect.inflate(20, 20), border_radius=5)
        self.screen.blit(text_surf, text_rect)

    def start_combat(self, sprite_identifier):
        self.sprite_to_modify = self.object_handler.get_sprite_by_identifier(sprite_identifier)
        if self.sprite_to_modify.is_alive():
            self.generate_question()

    def check_answer(self):
        try:
            if int(self.current_input) == self.answer:
                self.sound.correct.play()
                self.sprite_to_modify.health -= 25
                self.feedback_color = (0, 255, 0, 128)
            else:
                self.sound.wrong.play()
                self.player.player_health -= 25
                self.feedback_color = (255, 0, 0, 128)
        except ValueError:
            self.player.player_health -= 25
            self.feedback_color = (255, 0, 0, 128)
        self.current_input = ""
        self.game_active = False

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            if self.game_active:
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        self.check_answer()
                    elif event.key == pg.K_BACKSPACE:
                        self.current_input = self.current_input[:-1]
                    elif event.unicode.isdigit():
                        self.current_input += event.unicode

    def update(self):
        self.player.update()
        self.raycast.update()
        self.object_handler.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps():.2f}')

    def draw(self):
        self.screen.fill((30, 30, 30))
        self.object_renderer.draw()
        if self.game_active and self.player.is_alive():
            self.draw_text_box(self.question, RES[1] // 2)
            self.draw_text_box(self.current_input, RES[1] // 2 + 50)
        if self.feedback_color and self.player.is_alive():
            overlay = pg.Surface(RES)  # Create a transparent surface
            overlay.set_alpha(self.feedback_color[3])  # Set opacity
            overlay.fill(self.feedback_color[:3])  # Fill with the feedback color
            self.screen.blit(overlay, (0, 0))  # Display the overlay
            self.feedback_color = None
        pg.display.flip()

    def run(self):
        while True:
            self.events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
