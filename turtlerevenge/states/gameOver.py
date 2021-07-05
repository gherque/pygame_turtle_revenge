import pygame

from enum import Enum

from turtlerevenge.states.state import State
from turtlerevenge.assets.asset_manager import AssetManager, AssetType
from turtlerevenge.assets.sound_manager import SoundManager
from turtlerevenge.ui.label import UILabel
from turtlerevenge.ui.label_clickable import UILabelClickable
from turtlerevenge.config import Config

class Actions(Enum):
    Intro = 0

class GameOver(State):

    def __init__(self):
        super().__init__()

        AssetManager.instance().load(AssetType.Music, Config.sound_gameover_name, Config.sound_gameover_filename)

        AssetManager.instance().load(AssetType.Font, Config.font_name_huge, Config.font_filename, font_size = Config.font_size_huge)
        AssetManager.instance().load(AssetType.Font, Config.font_name_massive, Config.font_filename, font_size = Config.font_size_massive)

        font_huge = AssetManager.instance().get(AssetType.Font, Config.font_name_huge)
        font_massive = AssetManager.instance().get(AssetType.Font, Config.font_name_massive)
        font_small = AssetManager.instance().get(AssetType.Font, Config.font_name_small)

        center_x_position = Config.screen_size[0] / 2

        self.__label1 = UILabel((center_x_position, 100), font_huge, "Turtle Revenge", Config.color_green)
        self.__label2 = UILabel((center_x_position, 225), font_massive, "GAME OVER", Config.color_red)
        self.__label3 = UILabel((center_x_position, 290), font_small, "Maybe next time", Config.color_green)
        # TODO: Poner puntuación conseguida y quizás enviar a un ranking

        self.__button = UILabelClickable((center_x_position, 350), font_small, "Click To Return Intro", Config.color_red, Config.color_white, action = Actions.Intro)

    def enter(self):
        SoundManager.instance().play_music(Config.sound_gameover_name)
        self.done = False

    def exit(self):
        pass

    def handle_input(self, event):
        if self.__button.handle_input(event) == Actions.Intro:
            self.next_state = "Intro"
            self.done = True

    def update(self, delta_time):
        pass

    def render(self, surface):
        self.__label1.render(surface)
        self.__label2.render(surface)
        self.__label3.render(surface)
        self.__button.render(surface)
