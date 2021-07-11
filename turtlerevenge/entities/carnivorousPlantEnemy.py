import pygame

from turtlerevenge.config import Config
from turtlerevenge.assets.asset_manager import AssetManager, AssetType
from turtlerevenge.assets.sound_manager import SoundManager
from turtlerevenge.entities.gameobject import GameObject

class CarnivorousPlantEnemy(GameObject):

    def __init__(self, world, type, coordinates):
        super().__init__()
        self.__type = type
        self.__is_moving_up = False
        self.__initial_y = coordinates[1]

        _, self.clip = AssetManager.instance().get(AssetType.SpriteSheet, Config.carnivorousPlant[0 if self.__is_moving_up else 1], sheet_name = Config.mario_spritesheet_name)
        AssetManager.instance().load(AssetType.Sound, Config.sfx_smashEnemy_name, Config.sfx_smashEnemy_filename)

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
        if self.__initial_y + 30 < self.position.y:
            self.__is_moving_up = True
        elif self.__initial_y > self.position.y:
            self.__is_moving_up = False

        movement = pygame.math.Vector2(0.0, Config.plants_speed * (-1 if self.__is_moving_up else 1))

        self.coordinates += movement * delta

        if self.position != pygame.math.Vector2(self.coordinates[0] - (self.__world.screenCenterX - Config.screen_size[0] / 2), self.coordinates[1]):
            self.position = pygame.math.Vector2(self.coordinates[0] - (self.__world.screenCenterX - Config.screen_size[0] / 2), self.coordinates[1])

            self._center()

    def render(self, surface):
        if self.__type == "carnivorousPlant":
            carnivorousPlant_sprite_name = Config.carnivorousPlant[0 if self.__is_moving_up else 1]
        else:
            carnivorousPlant_sprite_name = Config.carnivorousPlant_dark[0 if self.__is_moving_up else 1]
        if self.position.x >= 0 or self.position.x <= Config.screen_size[0]:
            image, clip = AssetManager.instance().get(AssetType.SpriteSheet, carnivorousPlant_sprite_name, sheet_name = Config.mario_spritesheet_name)
            surface.blit(image, self.render_rect, clip)

        if Config.debug:
            pygame.draw.rect(surface, Config.debug_collider_color, self.rect, 1)
            pygame.draw.rect(surface, Config.debug_render_color, self.render_rect, 1)

    def release(self):
        pass

    def get_pos(self):
        return self.position
