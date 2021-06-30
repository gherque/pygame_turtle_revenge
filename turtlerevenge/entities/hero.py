import pygame

from turtlerevenge.config import Config
from turtlerevenge.assets.asset_manager import AssetManager, AssetType
from turtlerevenge.entities.gameobject import GameObject
from turtlerevenge.entities.projectile import ProjectileType

class Hero(GameObject):

    def __init__(self, world):
        super().__init__()
        self.__is_moving_up = False
        self.__is_moving_right = False
        self.__is_moving_down = False
        self.__is_moving_left = False
        self.__is_attacking = False
        self.__cool_down_time = 0.0
        self.__walk_index = 0
        self.__attack_index = 0
        self.__jumping_height = 0
        self.__direction_left = False

        AssetManager.instance().load(AssetType.SpriteSheet, Config.turtle_spritesheet_name, Config.turtle_spritesheet_filename, data_filename = Config.turtle_spritesheet_coordinates_filename)

        _, clip = AssetManager.instance().get(AssetType.SpriteSheet, Config.turtle_walk[self.__walk_index], sheet_name = Config.turtle_spritesheet_name)

        self.position = pygame.math.Vector2(Config.turtle_initial_position)
        self.rect = clip.copy()
        self.rect.inflate_ip(self.rect.width * -0.60, self.rect.height * -0.2)

        self.render_rect = clip.copy()

        self._center()

        self.__world = world

    def handle_input(self, key, is_pressed):
        if key == pygame.K_UP:
            self.__is_moving_up = is_pressed
            self.__is_moving_down = True if not is_pressed else self.__is_moving_down
        elif key == pygame.K_LEFT:
            self.__is_moving_left = is_pressed
        elif key == pygame.K_RIGHT:
            self.__is_moving_right = is_pressed
        elif key == pygame.K_SPACE:
            self.__is_attacking = is_pressed
            # TODO: Play sound
            if self.__cool_down_time <= 0.0:
                self.__fire_bullet()

    def update(self, delta):
        movement = pygame.math.Vector2(0.0, 0.0)

        if self.__is_moving_up:
            if self.__jumping_height < Config.turtle_max_jumping_height and not self.__is_moving_down:
                movement.y -= Config.turtle_speed
                self.__jumping_height += Config.turtle_speed * delta
            else:
                self.__is_moving_down = True
        if self.__is_moving_down:
            movement.y += Config.turtle_speed
        if self.__is_moving_left:
            movement.x -= Config.turtle_speed
        if self.__is_moving_right:
            movement.x += Config.turtle_speed

        self.__direction_left = True if movement.x < 0 or (self.__direction_left and movement.x == 0) else False

        self.position += movement * delta
        self.check_bounds()
        self._center()

        if self.__walk_index == 3:
            self.__walk_index = 0

        if self.__attack_index == 2:
            self.__attack_index = 0

        self.__walk_index = min(self.__walk_index + Config.turtle_speed * delta / 13, 3) if self.__is_moving_left ^ self.__is_moving_right else self.__walk_index
        self.__attack_index = min(self.__attack_index + Config.turtle_speed * delta / 13, 2) if self.__is_attacking else self.__attack_index

        if self.__is_moving_down:
            # TODO: Cuando toca con algo debe parar aunque no haya llegado al y origen (ej. cae encima de un piso superior). Ahora está en tamaño de la pantalla - 40 pero si hay hueco en el piso no debería parar ahí y debería morir
            if self.position.y >= Config.turtle_initial_position[1]:
                self.__is_moving_down = False
                self.position.y = Config.turtle_initial_position[1]
                self.__jumping_height = 0

        if self.__cool_down_time > 0.0:
            self.__cool_down_time -= delta

    def render(self, surface):
        turtle_name = Config.turtle_walk_reverse[int(self.__walk_index)] if self.__direction_left else Config.turtle_walk[int(self.__walk_index)]

        if self.__is_moving_up or self.__is_moving_down:
            turtle_name = Config.turtle_jump_reverse if self.__direction_left else Config.turtle_jump

        if self.__is_attacking:
            turtle_name = Config.turtle_attack_reverse[int(self.__attack_index)] if self.__direction_left else Config.turtle_attack[int(self.__attack_index)]

        image, clip = AssetManager.instance().get(AssetType.SpriteSheet, turtle_name, sheet_name = Config.turtle_spritesheet_name)
        surface.blit(pygame.transform.flip(image, True, False) if self.__direction_left else image, self.render_rect, clip)

        if Config.debug:
            pygame.draw.rect(surface, Config.debug_collider_color, self.rect, 1)
            pygame.draw.rect(surface, Config.debug_render_color, self.render_rect, 1)

    def release(self):
        pass

    def __fire_bullet(self):
        # TODO: Lanzar ataque con arma de mano.
        # self.__world.spawn_bullet(ProjectileType.AlliedBullet, self.render_rect.midtop, pygame.math.Vector2(Config.allied_bullet_velocity))
        self.__cool_down_time = Config.turtle_fire_cooldown

    def check_bounds(self):
        # TODO: Cuando llegue al centro de la pantalla que no avance sino que avance el background. Excepción: cuando llegue al final del background.
        if self.position.x < 0:
            self.position.x = 0
        elif self.position.x > Config.screen_size[0]:
            self.position.x = Config.screen_size[0]

        if self.position.y > Config.screen_size[1]:
            self.position.y = Config.screen_size[1]
        elif self.position.y < Config.screen_size[1] - (Config.screen_size[1] / 2):
            self.position.y = Config.screen_size[1] / 2

        return

    def get_pos(self):
        return self.position
