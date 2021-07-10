import pygame

from turtlerevenge.config import Config
from turtlerevenge.assets.asset_manager import AssetManager, AssetType
from turtlerevenge.entities.gameobject import GameObject

class Friend(GameObject):

    def __init__(self, world, coordinates):
        super().__init__()
        self.__speed = -1 * Config.friend_speed
        self.__walk_index = 0

        _, self.clip = AssetManager.instance().get(AssetType.SpriteSheet, Config.turtle[self.__walk_index], sheet_name = Config.mario_spritesheet_name)

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
        movement = pygame.math.Vector2(self.__speed, 0.0)

        self.coordinates += movement * delta

        if self.position != pygame.math.Vector2(self.coordinates[0] - (self.__world.screenCenterX - Config.screen_size[0] / 2), self.coordinates[1]):
            self.position = pygame.math.Vector2(self.coordinates[0] - (self.__world.screenCenterX - Config.screen_size[0] / 2), self.coordinates[1])

            if self.__walk_index == 1:
                self.__walk_index = 0

            self.__walk_index = min(self.__walk_index + Config.friend_speed * delta / 13, 1)

            self._center()

    def render(self, surface):
        if self.position.x >= 0 or self.position.x <= Config.screen_size[0]:
            sprite_name = Config.turtle[int(self.__walk_index)] if self.__speed < 0 else Config.turtle_reverse[int(self.__walk_index)]
            image, clip = AssetManager.instance().get(AssetType.SpriteSheet, sprite_name, sheet_name = Config.mario_spritesheet_name)
            surface.blit(pygame.transform.flip(image, True, False) if self.__speed > 0 else image, self.render_rect, clip)

        if Config.debug:
            pygame.draw.rect(surface, Config.debug_collider_color, self.rect, 1)
            pygame.draw.rect(surface, Config.debug_render_color, self.render_rect, 1)

    def release(self):
        pass

    def get_pos(self):
        return self.position

    def change_direction(self):
        self.__speed *= -1
