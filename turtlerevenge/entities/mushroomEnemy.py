import pygame

from turtlerevenge.config import Config
from turtlerevenge.assets.asset_manager import AssetManager, AssetType
from turtlerevenge.entities.gameobject import GameObject

class MushroomEnemy(GameObject):

    def __init__(self, world, coordinates):
        super().__init__()
        self.__speed = -1 * Config.foolEnemy_speed
        self.__walk_index = 0
        self.is_removed = False
        self.__is_player_moving_left = False

        _, self.clip = AssetManager.instance().get(AssetType.SpriteSheet, Config.mushroom[self.__walk_index], sheet_name = Config.mario_spritesheet_name)

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
        movement = pygame.math.Vector2(0.0, 0.0)
        if self.is_removed:
            if self.position.y <= Config.screen_size[1]:
                movement = pygame.math.Vector2(abs(self.__speed) / 5 * (-1 if self.__is_player_moving_left else 1), abs(self.__speed))
        else:
            movement = pygame.math.Vector2(self.__speed, 0.0)

        self.coordinates += movement * delta

        if self.position != pygame.math.Vector2(self.coordinates[0] - (self.__world.screenCenterX - Config.screen_size[0] / 2), self.coordinates[1]):
            self.position = pygame.math.Vector2(self.coordinates[0] - (self.__world.screenCenterX - Config.screen_size[0] / 2), self.coordinates[1])

            if self.__walk_index == 1:
                self.__walk_index = 0

            self.__walk_index = min(self.__walk_index + abs(self.__speed) * delta / 16, 1)

            self._center()

    def render(self, surface):
        mushroom_sprite_name = Config.mushroom_lying_down if self.is_removed else Config.mushroom[int(self.__walk_index)]
        if self.position.x >= 0 or self.position.x <= Config.screen_size[0]:
            image, clip = AssetManager.instance().get(AssetType.SpriteSheet, mushroom_sprite_name, sheet_name = Config.mario_spritesheet_name)
            surface.blit(image, self.render_rect, clip)

        if Config.debug:
            pygame.draw.rect(surface, Config.debug_collider_color, self.rect, 1)
            pygame.draw.rect(surface, Config.debug_render_color, self.render_rect, 1)

    def release(self):
        pass

    def get_pos(self):
        return self.position

    def change_direction(self):
        if not self.is_removed:
            self.__speed *= -1

    def remove(self, is_player_moving_left):
        self.is_removed = True
        self.__is_player_moving_left = is_player_moving_left
        # TODO: Play sfx sound
