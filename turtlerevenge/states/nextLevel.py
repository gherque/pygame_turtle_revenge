import pygame

from enum import Enum

from turtlerevenge.states.state import State
from turtlerevenge.assets.asset_manager import AssetManager, AssetType
from turtlerevenge.assets.sound_manager import SoundManager
from turtlerevenge.ui.label import UILabel
from turtlerevenge.ui.label_clickable import UILabelClickable
from turtlerevenge.config import Config

class Actions(Enum):
    GamePlay = 0

class NextLevel(State):

    def __init__(self):
        super().__init__()

        AssetManager.instance().load(AssetType.Music, Config.sound_gameend_name, Config.sound_gameend_filename)

        AssetManager.instance().load(AssetType.Font, Config.font_name_huge, Config.font_filename, font_size = Config.font_size_huge)
        AssetManager.instance().load(AssetType.Font, Config.font_name_massive, Config.font_filename, font_size = Config.font_size_massive)

    def enter(self):
        # TODO: If level is 1 or 2 (intermediates levels), continue with next screen without show partial scores

        font_huge = AssetManager.instance().get(AssetType.Font, Config.font_name_huge)
        font_small = AssetManager.instance().get(AssetType.Font, Config.font_name_small)

        center_x_position = Config.screen_size[0] / 2

        initialScore = Config.score
        Config.score += (
            Config.remaining_lifes * Config.lifes_remaining_score +
            Config.pizzaSlices * Config.pizza_slice_score +
            int(Config.remainingTime) * Config.seconds_remaining_score +
            int(Config.finalFlagHeight) * Config.finalFlag_height_score)

        self.__label1 = UILabel((center_x_position, 100), font_huge, "Turtle Revenge", Config.color_green)
        self.__label2 = UILabel((center_x_position, 150), font_small, "LEVEL FINISHED", Config.color_green)
        self.__label3 = UILabel((center_x_position, 175), font_small, "Initial Score: " + str(initialScore), Config.color_green)
        self.__label4 = UILabel((center_x_position, 200), font_small, "Pizza slices: " + str(Config.pizzaSlices) + " * " + str(Config.pizza_slice_score) + " = " + str(Config.pizzaSlices * Config.pizza_slice_score), Config.color_green)
        self.__label5 = UILabel((center_x_position, 225), font_small, "Remaining Lifes: " + str(Config.remaining_lifes) + " * " + str(Config.lifes_remaining_score) + " = " + str(Config.remaining_lifes * Config.lifes_remaining_score), Config.color_green)
        self.__label6 = UILabel((center_x_position, 250), font_small, "Remaining Time: " + str(int(Config.remainingTime)) + " * " + str(Config.seconds_remaining_score) + " = " + str(int(Config.remainingTime) * Config.seconds_remaining_score), Config.color_green)
        self.__label7 = UILabel((center_x_position, 275), font_small, "Final Flag Height: " + str(int(Config.finalFlagHeight)) + " * " + str(Config.finalFlag_height_score) + " = " + str(int(Config.finalFlagHeight) * Config.finalFlag_height_score), Config.color_green)
        self.__label8 = UILabel((center_x_position, 300), font_small, "New Score: " + str(Config.score), Config.color_green)
        self.__button = UILabelClickable((center_x_position, 350), font_small, "Click To Next Level", Config.color_red, Config.color_white, action = Actions.GamePlay)

        SoundManager.instance().play_music(Config.sound_gameend_name, True)
        self.done = False

    def exit(self):
        pass

    def handle_input(self, event):
        if self.__button.handle_input(event) == Actions.GamePlay:
            Config.pizzaSlices = 0
            Config.remainingTime = 0
            Config.finalFlagHeight = 0

            if Config.current_level + 1 == len(Config.scene):
                self.next_state = "GameEnd"
                Config.remaining_lifes = 1
                Config.score = 0
                Config.current_level = 0
            else:
                Config.remaining_lifes += 1
                Config.current_level += 1
                self.next_state = "GamePlay"

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
        self.__label8.render(surface)
        self.__button.render(surface)
