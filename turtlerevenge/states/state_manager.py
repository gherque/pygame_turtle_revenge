from turtlerevenge.states.about import About
from turtlerevenge.config import Config
from turtlerevenge.states.intro import Intro
from turtlerevenge.states.gameEnd import GameEnd
from turtlerevenge.states.gameOver import GameOver
from turtlerevenge.states.gameplay.gameplay import GamePlay

class StateManager:

    def __init__(self):
        self.__states = {
            "Intro": Intro(),
            "GamePlay": GamePlay(),
            "About": About(),
            "GameOver": GameOver(),
            "GameEnd": GameEnd()
        }

        self.__current_state_name = "Intro"  # Start State
        self.__current_state = self.__states[self.__current_state_name]
        self.__current_state.enter()

    def handle_event(self, event):
        self.__current_state.handle_input(event)

    def update(self, delta_time):
        if self.__current_state.done:
            self.__change_state()
        self.__current_state.update(delta_time)

    def render(self, surface):
        surface.fill(Config.scene[Config.current_level]["background_color"] if self.__current_state_name == "GamePlay" else Config.background_color)
        self.__current_state.render(surface)

    def quit(self):
        self.__current_state.exit()

    def __change_state(self):
        self.__current_state.exit()
        previous_state = self.__current_state_name

        self.__current_state_name = self.__current_state.next_state
        self.__current_state = self.__states[self.__current_state_name]
        self.__current_state.previous_state = previous_state
        self.__current_state.enter()
