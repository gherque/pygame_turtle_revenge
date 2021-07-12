import pygame

from turtlerevenge.config import Config
from turtlerevenge.entities.gameobject import GameObject

class NextLevelPortal(GameObject):

    def __init__(self, world, coordinates):
        super().__init__()

        self.coordinates = coordinates
        self.position = pygame.math.Vector2(coordinates)
        self.rect = pygame.Rect(0, 0, 5, 16)

        self.render_rect = self.rect.copy()

        self._center()

        self.__world = world

    def handle_input(self, key, is_pressed):
        pass

    def update(self, delta):
        if self.position != pygame.math.Vector2(self.coordinates[0] - (self.__world.screenCenterX - Config.screen_size[0] / 2), self.coordinates[1]):
            self.position = pygame.math.Vector2(self.coordinates[0] - (self.__world.screenCenterX - Config.screen_size[0] / 2), self.coordinates[1])
            self._center()

    def render(self, surface):
        if (self.position.x >= 0 or self.position.x <= Config.screen_size[0]) and Config.debug:
            pygame.draw.rect(surface, (255, 255, 255), self.rect, 1)
            # pygame.draw.rect(surface, Config.debug_render_color, self.render_rect, 1)

    def release(self):
        pass

    def get_pos(self):
        return self.position
