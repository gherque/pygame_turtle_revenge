import pygame

from enum import Enum

from turtlerevenge.states.state import State
from turtlerevenge.assets.asset_manager import AssetManager, AssetType
from turtlerevenge.assets.sound_manager import SoundManager
from turtlerevenge.ui.label import UILabel
from turtlerevenge.ui.label_clickable import UILabelClickable
from turtlerevenge.config import Config

class Actions(Enum):
    Start_Game = 0
    About = 1

class Intro(State):

    def __init__(self):
        super().__init__()

        AssetManager.instance().load(AssetType.Music, Config.sound_intro_name, Config.sound_intro_filename)

        AssetManager.instance().load(AssetType.Font, Config.font_name_huge, Config.font_filename, font_size = Config.font_size_huge)

        titlefont = AssetManager.instance().get(AssetType.Font, Config.font_name_huge)
        font = AssetManager.instance().get(AssetType.Font, Config.font_name_small)

        self.__label = UILabel((Config.screen_size[0] / 2, 100), titlefont, "Turtle Revenge", Config.color_green)
        self.__button1 = UILabelClickable((Config.screen_size[0] / 2, 250), font, "Click To Start The Game", Config.color_red, Config.color_white, action = Actions.Start_Game)
        self.__button2 = UILabelClickable((Config.screen_size[0] / 2, 300), font, "Click To Watch Credits", Config.color_red, Config.color_white, action = Actions.About)

    def enter(self):
        SoundManager.instance().play_music(Config.sound_intro_name, False)
        self.done = False

    def exit(self):
        pass

    def handle_input(self, event):
        if self.__button1.handle_input(event) == Actions.Start_Game:
            self.next_state = "GamePlay"
            self.done = True
        elif self.__button2.handle_input(event) == Actions.About:
            self.next_state = "About"
            self.done = True

    def update(self, delta_time):
        pass

    def render(self, surface):
        self.__label.render(surface)
        self.__button1.render(surface)
        self.__button2.render(surface)
