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

class About(State):

    def __init__(self):
        super().__init__()

        AssetManager.instance().load(AssetType.Music, Config.sound_about_name, Config.sound_about_filename)

        AssetManager.instance().load(AssetType.Font, Config.font_name_huge, Config.font_filename, font_size = Config.font_size_huge)

        titlefont = AssetManager.instance().get(AssetType.Font, Config.font_name_huge)
        font = AssetManager.instance().get(AssetType.Font, Config.font_name_small)

        center_x_position = Config.screen_size[0] / 2

        self.__label1 = UILabel((center_x_position, 100), titlefont, "Turtle Revenge", Config.color_green)
        self.__label2 = UILabel((center_x_position, 200), font, "Author: Gustavo Hernández " + chr(169) + "2021", Config.color_green)
        self.__label3 = UILabel((center_x_position, 225), font, "A simple game example to demonstrate know-how adquired", Config.color_green)
        self.__label4 = UILabel((center_x_position, 250), font, "during 'Videogames' course on Valencia International University.", Config.color_green)
        self.__label5 = UILabel((center_x_position, 275), font, "This game have been made as a student demonstration. The resources", Config.color_green)
        self.__label6 = UILabel((center_x_position, 300), font, "loaded on this game are under copyright by their respective owners.", Config.color_green)
        self.__label7 = UILabel((center_x_position, 325), font, "Partial or total copying of this code is strictly prohibited.", Config.color_green)
        self.__button = UILabelClickable((center_x_position, 400), font, "Click To Return Intro", Config.color_red, Config.color_white, action = Actions.Intro)

    def enter(self):
        SoundManager.instance().play_music(Config.sound_about_name, False)
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
        self.__label4.render(surface)
        self.__label5.render(surface)
        self.__label6.render(surface)
        self.__label7.render(surface)
        self.__button.render(surface)
