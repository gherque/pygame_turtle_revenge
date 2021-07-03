import pygame

from turtlerevenge.assets.asset_manager import AssetManager, AssetType
from turtlerevenge.entities.rendergroup import RenderGroup
from turtlerevenge.entities.hero import Hero
# from turtlerevenge.entities.projectile import Projectile, ProjectileType
# from turtlerevenge.entities.explosion import Explosion
# from turtlerevenge.entities.enemies.enemy import Enemy
from turtlerevenge.entities.sceneItem import SceneItem
from turtlerevenge.assets.sound_manager import SoundManager
# from turtlerevenge.assets.parallax import Parallax
# from turtlerevenge.states.gameplay.spawner import Spawner
from turtlerevenge.config import Config
from turtlerevenge.states.gameplay.events import game_over_event, end_game_event

class World:

    def __init__(self):
        self.screenCenterX = Config.screen_size[0] / 2
        self.__players = RenderGroup()
        self.__sceneItems = RenderGroup()
        self.__transparentSceneItems = RenderGroup()
        # self.__allied_bullets = RenderGroup()
        # self.__enemy_bullets = RenderGroup()
        # self.__explosions = RenderGroup()
        # self.__enemies = RenderGroup()

    def init(self):
        # TODO: Pintar los escenarios rígidos (falta addons (interrogantes))
        # TODO: Pintar enemigos (setas, luigis, marios)
        # TODO: Colisiones con enemigos (si es por arriba o atacando hacia el lado del enemigo -> ganar, si no morir)
        # TODO: Pintar amigos (tortugas, tortugas con pinchos)
        # TODO: Colisiones con amigos --> saludo pero con retardo por si vienen varios seguidos no quedarse hablando todo el rato
        # TODO: Colisiones con escenario: revisar colisiones para no dejar mover o quedarse en niveles superiores y detectar NO colisiones para bajar de nivel o salir del escenario (morir)

        AssetManager.instance().load(AssetType.SpriteSheet, Config.mario_spritesheet_name, Config.mario_spritesheet_filename, data_filename = Config.mario_spritesheet_coordinates_filename)

        # Clouds
        for single_cloud in Config.scene[Config.current_level]["clouds"]["single"]:
            self.__transparentSceneItems.add(SceneItem(self, Config.scene_cloud_single, single_cloud))
        for double_cloud in Config.scene[Config.current_level]["clouds"]["double"]:
            self.__transparentSceneItems.add(SceneItem(self, Config.scene_cloud_double, double_cloud))
        for triple_cloud in Config.scene[Config.current_level]["clouds"]["triple"]:
            self.__transparentSceneItems.add(SceneItem(self, Config.scene_cloud_triple, triple_cloud))

        # Mountains
        for small_mountain in Config.scene[Config.current_level]["mountains"]["small"]:
            self.__transparentSceneItems.add(SceneItem(self, Config.scene_mountain_small, small_mountain))
        for big_mountain in Config.scene[Config.current_level]["mountains"]["big"]:
            self.__transparentSceneItems.add(SceneItem(self, Config.scene_mountain_big, big_mountain))

        # Bushs
        for single_bush in Config.scene[Config.current_level]["bushs"]["single"]:
            self.__transparentSceneItems.add(SceneItem(self, Config.scene_bush_single, single_bush))
        for double_bush in Config.scene[Config.current_level]["bushs"]["double"]:
            self.__transparentSceneItems.add(SceneItem(self, Config.scene_bush_double, double_bush))
        for triple_bush in Config.scene[Config.current_level]["bushs"]["triple"]:
            self.__transparentSceneItems.add(SceneItem(self, Config.scene_bush_triple, triple_bush))

        # Castle
        self.__transparentSceneItems.add(SceneItem(self, Config.scene_castle, Config.scene[Config.current_level]["castle"]))

        # Final Flag
        self.__sceneItems.add(SceneItem(self, Config.scene_final_flag, Config.scene[Config.current_level]["finalFlag"]))

        # Main floor
        i = 0
        for floorHole in Config.scene[Config.current_level]["floorHoles"]:
            for j in range(floorHole[0]):
                self.__sceneItems.add(SceneItem(self, Config.scene_floor, (i * 16 + 8, Config.screen_size[1] - 32 + 8)))
                self.__sceneItems.add(SceneItem(self, Config.scene_floor, (i * 16 + 8, Config.screen_size[1] - 16 + 8)))
                i += 1
            i += floorHole[1]

        # Pipes
        for pipe in Config.scene[Config.current_level]["pipes"]["vertical"]:
            self.__sceneItems.add(SceneItem(self, Config.scene_pipe_vertical_end, (pipe[0] * 16 + 17, Config.screen_size[1] - 32 - 16 * pipe[1] - 17)))
            for i in range(pipe[1]):
                self.__sceneItems.add(SceneItem(self, Config.scene_pipe_vertical_extension, (pipe[0] * 16 + 17, Config.screen_size[1] - 16 * i - 32 - 8)))

        # Block structures
        for block in Config.scene[Config.current_level]["blockStructures"]:
            for i in range(block[2]):
                for j in range(block[1]):
                    if block[3]:
                        self.__sceneItems.add(SceneItem(self, Config.scene_block, (block[0] * 16 + 8 + (j + i) * 16, Config.screen_size[1] - 32 - 8 - i * 16)))
                    else:
                        self.__sceneItems.add(SceneItem(self, Config.scene_block, (block[0] * 16 + 8 + j * 16, Config.screen_size[1] - 32 - 8 - i * 16)))

                    if j + i >= (block[1] - 1):
                        break

        # Upper floors
        for bricksObject in Config.scene[Config.current_level]["bricks"]:
            for i in range(bricksObject[1]):
                self.__sceneItems.add(SceneItem(self, Config.scene_bricks, (bricksObject[0] * 16 + 8 + i * 16, Config.screen_size[1] - 32 - 16 * bricksObject[2] - 8)))


            # self.__sceneItems.add(SceneItem(self, Config.scene_block, (block[0] * 16 + 17, Config.screen_size[1] - 32 - 16 * block[1] - 17)))
            # for i in range(block[1]):
            #     self.__sceneItems.add(SceneItem(self, Config.scene_block_vertical_extension, (block[0] * 16 + 17, Config.screen_size[1] - 16 * i - 32 - 8)))

        self.__players.add(Hero(self))
        # self.__parallax = Parallax()
        # self.__parallax.add_background(Config.jungle_name, 0, Config.jungle_speed)
        # self.__parallax.add_background(Config.clouds_name, 1, Config.clouds_speed)

        # self.__spawner = Spawner(self)
        AssetManager.instance().load(AssetType.Music, Config.sound_action_name, Config.sound_action_filename)
        SoundManager.instance().play_music(Config.sound_action_name)

    def handle_input(self, key, is_pressed):
        for game_object in self.__players:
            game_object.handle_input(key, is_pressed)

    def update(self, delta_time):
        self.__transparentSceneItems.update(delta_time)
        self.__sceneItems.update(delta_time)
        self.__players.update(delta_time)
        # self.__enemies.update(delta_time)
        # self.__allied_bullets.update(delta_time)
        # self.__enemy_bullets.update(delta_time)
        # self.__explosions.update(delta_time)
        # self.__parallax.update(delta_time)
        # self.__spawner.update(delta_time)

        # for player in pygame.sprite.groupcollide(self.__players, self.__enemy_bullets, True, True).keys():
        #     self.spawn_explosion(player.position.xy, True)
        #     self.game_over()

        # for enemy in pygame.sprite.groupcollide(self.__enemies, self.__allied_bullets, True, True).keys():
        #     self.spawn_explosion(enemy.body.status.position.xy, False)

        # for player in pygame.sprite.groupcollide(self.__players, self.__enemies, True, True).keys():
        #     self.spawn_explosion(player.position.xy, True)
        #     self.game_over()

    def render(self, surface):
        # self.__parallax.render(surface)
        self.__transparentSceneItems.draw(surface)
        self.__sceneItems.draw(surface)
        self.__players.draw(surface)
        # self.__enemies.draw(surface)
        # self.__allied_bullets.draw(surface)
        # self.__enemy_bullets.draw(surface)
        # self.__explosions.draw(surface)
        # self.__spawner.render(surface)

    def quit(self):
        self.__transparentSceneItems.empty()
        self.__sceneItems.empty()
        self.__players.empty()
        # self.__enemies.empty()
        # self.__allied_bullets.empty()
        # self.__enemy_bullets.empty()
        # self.__explosions.empty()
        # self.__parallax = None
        # self.__spawner = None

    # def spawn_bullet(self, projectile_type, position, velocity):
    #     if projectile_type == ProjectileType.AlliedBullet:
    #         self.__allied_bullets.add(Projectile(projectile_type, position, velocity))
    #         SoundManager.instance().play_sound(Config.allied_gunfire_name)
    #     if projectile_type == ProjectileType.EnemyBullet:
    #         self.__enemy_bullets.add(Projectile(projectile_type, position, velocity))
    #         SoundManager.instance().play_sound(Config.enemy_gunfire_name)

    # def spawn_explosion(self, position, is_hero):
    #     self.__explosions.add(Explosion(position))
    #     if is_hero:
    #         name = Config.explosion1_name
    #     else:
    #         name = Config.explosion2_name

    #     SoundManager.instance().play_sound(name)

    # def spawn_enemy(self, enemy_type, spawn_point, end_point, waypoints):
    #     self.__enemies.add(Enemy(self, enemy_type, spawn_point, end_point, waypoints))

    def game_over(self):
        pygame.time.set_timer(game_over_event, Config.game_over_time, True)
        SoundManager.instance().stop_music(Config.game_over_time)

    def game_end(self):
        pygame.time.set_timer(end_game_event, Config.end_game_time, True)
        SoundManager.instance().stop_music(Config.end_game_time)

    def get_hero_pos(self):
        if len(self.__players) > 0:
            return self.__players.sprites()[0].get_pos()
        else:
            return pygame.math.Vector2(0.0, 0.0)