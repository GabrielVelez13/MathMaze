from settings import *

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = "Resources/sounds/"
        self.correct = pg.mixer.Sound(self.path + "Correct Answer Tone.wav")
        self.wrong = pg.mixer.Sound(self.path + "Funny Fail Low Tone.wav")
        self.game_sound = pg.mixer.Sound(self.path + "Horror Piano.mp3")
        self.win_sound = pg.mixer.Sound(self.path + "Medieval Show Fanfare Announcement.wav")
        self.lose_sound = pg.mixer.Sound(self.path + "Slow Sad Trombone Fail.wav")