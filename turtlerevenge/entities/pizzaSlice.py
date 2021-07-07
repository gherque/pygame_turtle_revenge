import pygame

from turtlerevenge.config import Config
from turtlerevenge.assets.asset_manager import AssetManager, AssetType
from turtlerevenge.entities.gameobject import GameObject

class PizzaSlice(GameObject):

    def __init__(self, world, coordinates):
        super().__init__()
        self.__move_index = 0

        AssetManager.instance().load(AssetType.SpriteSheet, Config.pizza_spritesheet_name, Config.pizza_spritesheet_filename, data_filename = Config.pizza_spritesheet_coordinates_filename)
        _, self.clip = AssetManager.instance().get(AssetType.SpriteSheet, Config.pizza_spinning[self.__move_index], sheet_name = Config.pizza_spritesheet_name)

        self.coordinates = coordinates
        self.position = pygame.math.Vector2(coordinates)
        self.rect = self.clip.copy()
        # self.rect.inflate_ip(self.rect.width, self.rect.height)

        self.render_rect = self.clip.copy()

        self._center()

        self.__world = world

    def handle_input(self, key, is_pressed):
        pass

    def update(self, delta):
        if self.position != pygame.math.Vector2(self.coordinates[0] - (self.__world.screenCenterX - Config.screen_size[0] / 2), self.coordinates[1]):
            self.position = pygame.math.Vector2(self.coordinates[0] - (self.__world.screenCenterX - Config.screen_size[0] / 2), self.coordinates[1])
            self._center()

        if self.__move_index == 5:
            self.__move_index = 0

        self.__move_index = min(self.__move_index + Config.pizza_speed * delta / 13, 5)

    def render(self, surface):
        if self.position.x >= 0 or self.position.x <= Config.screen_size[0]:
            image, clip = AssetManager.instance().get(AssetType.SpriteSheet, Config.pizza_spinning[int(self.__move_index)], sheet_name = Config.pizza_spritesheet_name)
            surface.blit(image, self.render_rect, clip)

            if Config.debug:
                pygame.draw.rect(surface, Config.debug_collider_color, self.rect, 1)
                pygame.draw.rect(surface, Config.debug_render_color, self.render_rect, 1)

    def release(self):
        pass

    def get_pos(self):
        return self.position
