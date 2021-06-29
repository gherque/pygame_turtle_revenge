import pygame

from turtlerevenge.states.state import State
from turtlerevenge.states.gameplay.world import World
from turtlerevenge.states.gameplay.events import game_over_event, end_game_event

class GamePlay(State):

    def __init__(self):
        super().__init__()
        self.__world = World()

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            self.__world.handle_input(event.key, True)
        if event.type == pygame.KEYUP:
            self.__world.handle_input(event.key, False)
        if event.type == game_over_event:
            self.next_state = "GameOver"
            self.done = True
        if event.type == end_game_event:
            self.next_state = "GameEnd"
            self.done = True

    def update(self, delta_time):
        self.__world.update(delta_time)

    def render(self, surface):
        self.__world.render(surface)

    def enter(self):
        self.done = False
        self.__world.init()

    def exit(self):
        self.__world.quit()