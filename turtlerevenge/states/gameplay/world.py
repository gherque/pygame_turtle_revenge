import pygame

from turtlerevenge.assets.asset_manager import AssetManager, AssetType
from turtlerevenge.assets.sound_manager import SoundManager
from turtlerevenge.entities.rendergroup import RenderGroup
from turtlerevenge.entities.hero import Hero
# from turtlerevenge.entities.enemies.enemy import Enemy
from turtlerevenge.entities.fall import Fall
from turtlerevenge.entities.pizzaSlice import PizzaSlice
from turtlerevenge.entities.sceneItem import SceneItem
from turtlerevenge.ui.label import UILabel
# from turtlerevenge.states.gameplay.spawner import Spawner
from turtlerevenge.config import Config
from turtlerevenge.states.gameplay.events import game_over_event, end_game_event

class World:

    def __init__(self):
        self.screenCenterX = Config.screen_size[0] / 2
        self.__playerGroup = RenderGroup()
        self.__sceneItemGroup = RenderGroup()
        self.__transparentSceneItems = RenderGroup()
        self.__addonGroup = RenderGroup()
        self.__pizzaSliceGroup = RenderGroup()
        self.__fallGroup = RenderGroup()
        # self.__enemies = RenderGroup()

        self.__pizzaSlices = 0
        self.__score = 0
        self.__finishTime = 120
        self.__remainingLifes = 1

    def init(self):
        # TODO: Pintar enemigos (setas, plantas carnívoras, luigis, marios)
        # TODO: Colisiones con enemigos (si es por arriba o atacando hacia el lado del enemigo -> ganar, si no morir)
        # TODO: Pintar amigos (tortugas, tortugas con pinchos)
        # TODO: Colisiones con amigos --> saludo pero con retardo por si vienen varios seguidos no quedarse hablando todo el rato

        AssetManager.instance().load(AssetType.SpriteSheet, Config.mario_spritesheet_name, Config.mario_spritesheet_filename, data_filename = Config.mario_spritesheet_coordinates_filename)
        AssetManager.instance().load(AssetType.Font, Config.font_name_medium, Config.font_filename, font_size = Config.font_size_medium)

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
        self.__sceneItemGroup.add(SceneItem(self, Config.scene_final_flag, Config.scene[Config.current_level]["finalFlag"]))

        # Main floor
        i = 0
        for floorHole in Config.scene[Config.current_level]["floorHoles"]:
            for j in range(floorHole[0]):
                self.__sceneItemGroup.add(SceneItem(self, Config.scene_floor, (i * 16 + 8, Config.screen_size[1] - 32 + 8)))
                self.__sceneItemGroup.add(SceneItem(self, Config.scene_floor, (i * 16 + 8, Config.screen_size[1] - 16 + 8)))
                i += 1
            for z in range(floorHole[1] - 1):
                self.__fallGroup.add(Fall(self, ((i + 1) * 16, Config.screen_size[1] - 32)))
                i += 1
            i += 1

        # Pipes
        for pipe in Config.scene[Config.current_level]["pipes"]["vertical"]:
            self.__fallGroup.add(Fall(self, (pipe[0] * 16 - 24, Config.screen_size[1] - 32 - 16 * pipe[1] - 60)))
            self.__sceneItemGroup.add(SceneItem(self, Config.scene_pipe_vertical_end, (pipe[0] * 16 + 17, Config.screen_size[1] - 32 - 16 * pipe[1] - 17)))
            self.__fallGroup.add(Fall(self, (pipe[0] * 16 + 56, Config.screen_size[1] - 32 - 16 * pipe[1] - 60)))
            for i in range(pipe[1]):
                self.__sceneItemGroup.add(SceneItem(self, Config.scene_pipe_vertical_extension, (pipe[0] * 16 + 17, Config.screen_size[1] - 16 * i - 32 - 8)))

        # Block structures
        for block in Config.scene[Config.current_level]["blockStructures"]:
            for i in range(block[2]):
                for j in range(block[1]):
                    if block[3]:
                        if j == 0:
                            self.__fallGroup.add(Fall(self, (block[0] * 16 + 8 + (j + i) * 16 - 24, Config.screen_size[1] - 32 - i * 16 - 16 * 4)))
                        self.__sceneItemGroup.add(SceneItem(self, Config.scene_block, (block[0] * 16 + 8 + (j + i) * 16, Config.screen_size[1] - 32 - 8 - i * 16)))
                        if i == (block[2] - 1) and j + i == (block[1] - 1):
                            self.__fallGroup.add(Fall(self, (block[0] * 16 + 8 + (j + i + 1) * 16 + 8, Config.screen_size[1] - 32 - i * 16 - 16 * 4)))
                    else:
                        if i == (block[2] - 1) and j == 0:
                            self.__fallGroup.add(Fall(self, (block[0] * 16 + 8 + j * 16 - 24, Config.screen_size[1] - 32 - i * 16 - 16 * 4)))
                        self.__sceneItemGroup.add(SceneItem(self, Config.scene_block, (block[0] * 16 + 8 + j * 16, Config.screen_size[1] - 32 - 8 - i * 16)))
                        if j + i == (block[1] - 1):
                            self.__fallGroup.add(Fall(self, (block[0] * 16 + 8 + j * 16 + 24, Config.screen_size[1] - 32 - i * 16 - 16 * 4)))

                    if j + i >= (block[1] - 1):
                        break

        # Upper floors
        for bricksObject in Config.scene[Config.current_level]["bricks"]:
            for i in range(bricksObject[1]):
                if i == 0:
                    self.__fallGroup.add(Fall(self, (bricksObject[0] * 16 + 8 + i * 16 - 20, Config.screen_size[1] - 32 - bricksObject[2] * 16 - 16 * 4)))
                self.__sceneItemGroup.add(SceneItem(self, Config.scene_bricks, (bricksObject[0] * 16 + 8 + i * 16, Config.screen_size[1] - 32 - 16 * bricksObject[2] - 8)))
                if i == (bricksObject[1] - 1):
                    self.__fallGroup.add(Fall(self, (bricksObject[0] * 16 + 8 + i * 16 + 24, Config.screen_size[1] - 32 - bricksObject[2] * 16 - 16 * 4)))

        # Addons
        for addon in Config.scene[Config.current_level]["addons"]:
            self.__addonGroup.add(SceneItem(self, Config.scene_addon1, (addon[0] * 16 + 8, Config.screen_size[1] - 32 - 16 * addon[1] - 8)))

        # Falls
        for fall in Config.scene[Config.current_level]["falls"]:
            self.__fallGroup.add(Fall(self, (fall[0] * 16 - 24, Config.screen_size[1] - 32 - 16 * fall[1] - 16 * 4)))
            self.__fallGroup.add(Fall(self, (fall[0] * 17 + 24, Config.screen_size[1] - 32 - 16 * fall[1] - 16 * 4)))

        # Pizza slices
        for pizzaSlice in Config.scene[Config.current_level]["pizzaSlices"]:
            self.__pizzaSliceGroup.add(PizzaSlice(self, (pizzaSlice[0] + 13, pizzaSlice[1] - 15)))

        self.__playerGroup.add(Hero(self))

        # self.__spawner = Spawner(self)
        AssetManager.instance().load(AssetType.Music, Config.sound_action_name, Config.sound_action_filename)
        SoundManager.instance().play_music(Config.sound_action_name)

        self.__set_score_surface()

    def handle_input(self, key, is_pressed):
        for game_object in self.__playerGroup:
            game_object.handle_input(key, is_pressed)

    def update(self, delta_time):
        self.__transparentSceneItems.update(delta_time)
        self.__sceneItemGroup.update(delta_time)
        self.__addonGroup.update(delta_time)
        self.__pizzaSliceGroup.update(delta_time)
        self.__fallGroup.update(delta_time)
        self.__playerGroup.update(delta_time)
        # self.__enemies.update(delta_time)
        # self.__spawner.update(delta_time)

        # Player/sceneItems collisions
        for sceneItem in pygame.sprite.groupcollide(self.__sceneItemGroup, self.__playerGroup, False, False).keys():
            self.__playerGroup.sprites()[0].check_collision_type(sceneItem, 'sceneItem')

        # Player/addons collisions
        for addon in pygame.sprite.groupcollide(self.__addonGroup, self.__playerGroup, False, False).keys():
            self.__playerGroup.sprites()[0].check_collision_type(addon, 'addon')

        # Player/pizzaSlices collisions
        for pizzaSlice in pygame.sprite.groupcollide(self.__pizzaSliceGroup, self.__playerGroup, True, False).keys():
            self.__pizzaSlices += 1
            # TODO: Play sfx Sound

        # Player/falls collisions
        for fall in pygame.sprite.groupcollide(self.__fallGroup, self.__playerGroup, False, False).keys():
            self.__playerGroup.sprites()[0].fall()

        # for enemy in pygame.sprite.groupcollide(self.__enemies, self.__allied_bullets, True, True).keys():
        #     self.spawn_explosion(enemy.body.status.position.xy, False)

        # for player in pygame.sprite.groupcollide(self.__playerGroup, self.__enemies, True, True).keys():
        #     self.spawn_explosion(player.position.xy, True)
        #     self.game_over()

        self.__set_score_surface()

    def render(self, surface):
        self.__transparentSceneItems.draw(surface)
        self.__sceneItemGroup.draw(surface)
        self.__addonGroup.draw(surface)
        self.__pizzaSliceGroup.draw(surface)
        self.__playerGroup.draw(surface)
        self.__fallGroup.draw(surface)
        # self.__enemies.draw(surface)
        # self.__spawner.render(surface)

        self.__label1.render(surface)
        self.__label2.render(surface)
        self.__label3.render(surface)
        self.__label4.render(surface)
        self.__label5.render(surface)
        self.__label6.render(surface)
        self.__label7.render(surface)
        self.__label8.render(surface)
        self.__label9.render(surface)
        self.__label10.render(surface)

    def quit(self):
        self.__transparentSceneItems.empty()
        self.__sceneItemGroup.empty()
        self.__addonGroup.empty()
        self.__pizzaSliceGroup.empty()
        self.__fallGroup.empty()
        self.__playerGroup.empty()
        # self.__enemies.empty()
        # self.__spawner = None

    # def spawn_enemy(self, enemy_type, spawn_point, end_point, waypoints):
    #     self.__enemies.add(Enemy(self, enemy_type, spawn_point, end_point, waypoints))

    def game_over(self):
        pygame.time.set_timer(game_over_event, Config.game_over_time, True)
        SoundManager.instance().stop_music(Config.game_over_time)
        self.screenCenterX = Config.screen_size[0] / 2

    def game_end(self):
        pygame.time.set_timer(end_game_event, Config.end_game_time, True)
        SoundManager.instance().stop_music(Config.end_game_time)

    def get_hero_pos(self):
        if len(self.__playerGroup) > 0:
            return self.__playerGroup.sprites()[0].get_pos()
        else:
            return pygame.math.Vector2(0.0, 0.0)

    def get_score_xposition(self, order, total):
        return Config.screen_size[0] / total * order - Config.screen_size[0] / total / 2

    def __set_score_surface(self):
        font = AssetManager.instance().get(AssetType.Font, Config.font_name_medium)

        self.__label1 = UILabel((self.get_score_xposition(5, 5), 25), font, "Lifes", Config.color_white)
        self.__label2 = UILabel((self.get_score_xposition(5, 5), 50), font, str(self.__remainingLifes), Config.color_white)
        self.__label3 = UILabel((self.get_score_xposition(1, 5), 25), font, "Score", Config.color_white)
        self.__label4 = UILabel((self.get_score_xposition(1, 5), 50), font, str(self.__score), Config.color_white)
        self.__label5 = UILabel((self.get_score_xposition(2, 5), 25), font, "Pizza Slices", Config.color_white)
        self.__label6 = UILabel((self.get_score_xposition(2, 5), 50), font, str(self.__pizzaSlices), Config.color_white)
        self.__label7 = UILabel((self.get_score_xposition(3, 5), 25), font, "Level", Config.color_white)
        self.__label8 = UILabel((self.get_score_xposition(3, 5), 50), font, str(Config.current_level + 1), Config.color_white)
        self.__label9 = UILabel((self.get_score_xposition(4, 5), 25), font, "Time", Config.color_white)
        self.__label10 = UILabel((self.get_score_xposition(4, 5), 50), font, str(self.__finishTime), Config.color_white)
