import pygame

from turtlerevenge.config import Config
from turtlerevenge.assets.asset_manager import AssetManager, AssetType
from turtlerevenge.entities.gameobject import GameObject

class SceneItem(GameObject):

    def __init__(self, world, type, coordinates):
        super().__init__()

        self.image, self.clip = AssetManager.instance().get(AssetType.SpriteSheet, type, sheet_name = Config.mario_spritesheet_name)

        self.coordinates = coordinates
        self.position = pygame.math.Vector2(coordinates)
        self.rect = self.clip.copy()
        self.rect.inflate_ip(self.rect.width * -0.60, self.rect.height * -0.2)

        self.render_rect = self.clip.copy()

        self._center()

        self.__world = world

    def handle_input(self, key, is_pressed):
        pass

    def update(self, delta):
        if self.position != pygame.math.Vector2(self.coordinates[0] - (self.__world.screenCenterX - Config.screen_size[0] / 2), self.coordinates[1]):
            self.position = pygame.math.Vector2(self.coordinates[0] - (self.__world.screenCenterX - Config.screen_size[0] / 2), self.coordinates[1])
            self._center()

    def render(self, surface):
        if self.position.x >= 0 or self.position.x <= Config.screen_size[0]:
            surface.blit(self.image, self.render_rect, self.clip)

            if Config.debug:
                pygame.draw.rect(surface, Config.debug_collider_color, self.rect, 1)
                pygame.draw.rect(surface, Config.debug_render_color, self.render_rect, 1)

    def release(self):
        pass

    def get_pos(self):
        return self.position
