import pygame

from turtlerevenge.assets.asset_manager import AssetManager, AssetType
from turtlerevenge.assets.sound_manager import SoundManager
from turtlerevenge.entities.carnivorousPlantEnemy import CarnivorousPlantEnemy
from turtlerevenge.entities.hero import Hero
from turtlerevenge.entities.fall import Fall
from turtlerevenge.entities.friend import Friend
from turtlerevenge.entities.mushroomEnemy import MushroomEnemy
from turtlerevenge.entities.pizzaSlice import PizzaSlice
from turtlerevenge.entities.rendergroup import RenderGroup
from turtlerevenge.entities.sceneItem import SceneItem
from turtlerevenge.ui.label import UILabel
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
        self.__mushroomEnemyGroup = RenderGroup()
        self.__carnivorousPlantEnemyGroup = RenderGroup()
        self.__friendGroup = RenderGroup()

        self.__pizzaSlices = 0
        self.__score = 0
        self.__remainingLifes = 1
        self.__remainingTime = Config.scene[Config.current_level]["availableTime"]
        self.__start_ticks = pygame.time.get_ticks()

    def init(self):
        # TODO: Pintar enemigos (plantas carnívoras, luigis, marios)
        # TODO: Colisiones con enemigos (si es por arriba o atacando hacia el lado del enemigo -> ganar, si no morir)
        # TODO: Nuevo entity tipo fall para acciones en tuberías (si estás colisionando y pulsas el botón para abajo en tuberías verticales o para la dirección de la tubería horizontal, next level)
        # TODO: En config scenes, poner la posición inicial del player (Así coincide con puerta castillo o encima tubería...)
        # TODO: En config scenes, poner el límite en x del escenario para saber cuando el player no puede avanzar más
        # TODO: En config scenes, poner el color del fondo del escenario
        # TODO: Corregir estructuras de bloque en nivel 2-2

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
            self.__fallGroup.add(Fall(self, (pipe[0] * 16 - 12, Config.screen_size[1] - 32 - 16 * pipe[1] - 30)))
            self.__sceneItemGroup.add(SceneItem(self, Config.scene_pipe_vertical_end, (pipe[0] * 16 + 17, Config.screen_size[1] - 32 - 16 * pipe[1] - 17)))
            self.__fallGroup.add(Fall(self, (pipe[0] * 16 + 44, Config.screen_size[1] - 32 - 16 * pipe[1] - 30)))
            for i in range(pipe[1]):
                self.__sceneItemGroup.add(SceneItem(self, Config.scene_pipe_vertical_extension, (pipe[0] * 16 + 17, Config.screen_size[1] - 16 * i - 32 - 8)))

        for pipe in Config.scene[Config.current_level]["pipes"]["horizontal"]:
            self.__fallGroup.add(Fall(self, (pipe[0] * 16 - 12, Config.screen_size[1] - 32 - pipe[1] * 16 - 60)))
            self.__sceneItemGroup.add(SceneItem(self, Config.scene_pipe_horizontal_end, (pipe[0] * 16 + 14, Config.screen_size[1] - 32 - pipe[1] * 16 - 16)))
            self.__sceneItemGroup.add(SceneItem(self, Config.scene_pipe_horizontal_conn, (pipe[0] * 16 + 32 + 14, Config.screen_size[1] - 32 - pipe[1] * 16 - 16)))

        # Block structures
        for block in Config.scene[Config.current_level]["blockStructures"]:
            for i in range(block[2]):
                for j in range(block[1]):
                    if block[3]:
                        if j == 0:
                            self.__fallGroup.add(Fall(self, (block[0] * 16 + 8 + (j + i) * 16 - 12, Config.screen_size[1] - 32 - i * 16 - 16)))
                        self.__sceneItemGroup.add(SceneItem(self, Config.scene_block, (block[0] * 16 + 8 + (j + i) * 16, Config.screen_size[1] - 32 - 8 - i * 16)))
                        if i == (block[2] - 1) and j + i == (block[1] - 1):
                            self.__fallGroup.add(Fall(self, (block[0] * 16 + 8 + (j + i) * 16 + 12, Config.screen_size[1] - 32 - i * 16 - 16)))
                    else:
                        if i == (block[2] - 1) and j == 0:
                            self.__fallGroup.add(Fall(self, (block[0] * 16 + 8 + j * 16 - 12, Config.screen_size[1] - 32 - i * 16 - 16)))
                        self.__sceneItemGroup.add(SceneItem(self, Config.scene_block, (block[0] * 16 + 8 + j * 16, Config.screen_size[1] - 32 - 8 - i * 16)))
                        if j + i == (block[1] - 1):
                            self.__fallGroup.add(Fall(self, (block[0] * 16 + 8 + j * 16 + 12, Config.screen_size[1] - 32 - i * 16 - 16)))

                    if j + i >= (block[1] - 1):
                        break

        # Upper floors
        for bricksObject in Config.scene[Config.current_level]["bricks"]:
            for i in range(bricksObject[1]):
                if i == 0:
                    self.__fallGroup.add(Fall(self, (bricksObject[0] * 16 + 8 + i * 16 - 16, Config.screen_size[1] - 32 - bricksObject[2] * 16 - 25)))
                self.__sceneItemGroup.add(SceneItem(self, Config.scene_bricks, (bricksObject[0] * 16 + 8 + i * 16, Config.screen_size[1] - 32 - 16 * bricksObject[2] - 8)))
                if i == (bricksObject[1] - 1):
                    self.__fallGroup.add(Fall(self, (bricksObject[0] * 16 + 8 + i * 16 + 16, Config.screen_size[1] - 32 - bricksObject[2] * 16 - 25)))

        # Addons
        for addon in Config.scene[Config.current_level]["addons"]:
            self.__addonGroup.add(SceneItem(self, Config.scene_addon1, (addon[0] * 16 + 8, Config.screen_size[1] - 32 - 16 * addon[1] - 8)))

        # Falls
        for fall in Config.scene[Config.current_level]["falls"]:
            self.__fallGroup.add(Fall(self, (fall[0] * 16 - 12, Config.screen_size[1] - 32 - 16 * fall[1] - 16)))
            self.__fallGroup.add(Fall(self, (fall[0] * 17 + 12, Config.screen_size[1] - 32 - 16 * fall[1] - 16)))

        # Pizza slices
        for pizzaSlice in Config.scene[Config.current_level]["pizzaSlices"]:
            self.__pizzaSliceGroup.add(PizzaSlice(self, (pizzaSlice[0] + 13, pizzaSlice[1] - 15)))

        # Enemies
        for enemy in Config.scene[Config.current_level]["enemies"]:
            if enemy[0] == "mushroom" or enemy[0] == "mushroom_dark":
                self.__mushroomEnemyGroup.add(MushroomEnemy(self, enemy[0], (enemy[1] * 16 + 9, Config.screen_size[1] - 32 - enemy[2] * 16 - 9)))
            elif enemy[0] == "carnivorousPlant" or enemy[0] == "carnivorousPlant_dark":
                self.__carnivorousPlantEnemyGroup.add(CarnivorousPlantEnemy(self, enemy[0], (enemy[1] * 16 + 2, Config.screen_size[1] - 32 - enemy[2] * 16 - 9)))

        # Friends
        for friend in Config.scene[Config.current_level]["friends"]:
            if friend[0] == "turtle":
                self.__friendGroup.add(Friend(self, (friend[1] * 16 + 9, Config.screen_size[1] - 32 - friend[2] * 16 - 12)))

        self.__playerGroup.add(Hero(self))

        AssetManager.instance().load(AssetType.Music, Config.sound_action_name, Config.sound_action_filename)
        SoundManager.instance().play_music(Config.sound_action_name, False)
        AssetManager.instance().load(AssetType.Sound, Config.sfx_prize_name, Config.sfx_prize_filename)

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
        self.__mushroomEnemyGroup.update(delta_time)
        self.__carnivorousPlantEnemyGroup.update(delta_time)
        self.__friendGroup.update(delta_time)
        self.__playerGroup.update(delta_time)

        # Player/sceneItems collisions
        for sceneItem in pygame.sprite.groupcollide(self.__sceneItemGroup, self.__playerGroup, False, False).keys():
            self.__playerGroup.sprites()[0].check_collision_type(sceneItem, 'sceneItem')

        # Player/addons collisions
        for addon in pygame.sprite.groupcollide(self.__addonGroup, self.__playerGroup, False, False).keys():
            self.__playerGroup.sprites()[0].check_collision_type(addon, 'addon')

        # Player/pizzaSlices collisions
        for pizzaSlice in pygame.sprite.groupcollide(self.__pizzaSliceGroup, self.__playerGroup, True, False).keys():
            self.__pizzaSlices += 1
            SoundManager.instance().play_sound(Config.sfx_prize_name)

        # Player/falls collisions
        for fall in pygame.sprite.groupcollide(self.__fallGroup, self.__playerGroup, False, False).keys():
            self.__playerGroup.sprites()[0].fall()

        # FoolEnemies/sceneItems collisions
        for mushroomEnemy in pygame.sprite.groupcollide(self.__mushroomEnemyGroup, self.__sceneItemGroup, False, False).keys():
            mushroomEnemy.change_direction()

        # FoolEnemies/falls collisions
        for mushroomEnemy in pygame.sprite.groupcollide(self.__mushroomEnemyGroup, self.__fallGroup, False, False).keys():
            mushroomEnemy.change_direction()

        # FoolEnemies/player collisions
        for mushroomEnemy in pygame.sprite.groupcollide(self.__mushroomEnemyGroup, self.__playerGroup, False, False).keys():
            playerWinEnemy, is_player_moving_left = self.__playerGroup.sprites()[0].player_win_enemy("mushroom", mushroomEnemy)
            if playerWinEnemy == 1:
                self.__score += Config.mushroom_killed_score if not mushroomEnemy.is_removed else 0
                mushroomEnemy.remove(is_player_moving_left)
            elif playerWinEnemy == 0 and not mushroomEnemy.is_removed:
                self.__playerGroup.sprites()[0].remove()

        # Friends/sceneItems collisions
        for friend in pygame.sprite.groupcollide(self.__friendGroup, self.__sceneItemGroup, False, False).keys():
            friend.change_direction()

        # Friends/falls collisions
        for friend in pygame.sprite.groupcollide(self.__friendGroup, self.__fallGroup, False, False).keys():
            friend.change_direction()

        # Friends/player collisions
        for friend in pygame.sprite.groupcollide(self.__friendGroup, self.__playerGroup, False, False).keys():
            friend.greet_hero()

        # CarnivorousPlant/player collisions
        for carnivorousPlantEnemy in pygame.sprite.groupcollide(self.__carnivorousPlantEnemyGroup, self.__playerGroup, False, False).keys():
            self.__playerGroup.sprites()[0].remove()

        self.__set_score_surface()

    def render(self, surface):
        self.__transparentSceneItems.draw(surface)
        self.__carnivorousPlantEnemyGroup.draw(surface)
        self.__sceneItemGroup.draw(surface)
        self.__addonGroup.draw(surface)
        self.__pizzaSliceGroup.draw(surface)
        self.__fallGroup.draw(surface)
        self.__mushroomEnemyGroup.draw(surface)
        self.__friendGroup.draw(surface)
        self.__playerGroup.draw(surface)

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
        self.__mushroomEnemyGroup.empty()
        self.__friendGroup.empty()
        self.__carnivorousPlantEnemyGroup.empty()
        self.__playerGroup.empty()

    def game_over(self):
        if self.__remainingLifes == 0:
            # TODO: Mostrar puntuaciones y repintar todo el escenario
            pygame.time.set_timer(game_over_event, Config.game_over_time, True)
            SoundManager.instance().stop_music(Config.game_over_time)
        else:
            pygame.time.delay(750)
            self.__playerGroup.empty()
            self.screenCenterX = Config.screen_size[0] / 2
            self.__remainingLifes -= 1
            pygame.time.delay(500)
            self.__playerGroup.add(Hero(self))
            self.__remainingTime = Config.scene[Config.current_level]["availableTime"]
            self.__start_ticks = pygame.time.get_ticks()

    def game_end(self, finalFlagHeight):
        # TODO: Mostrar puntuaciones, sumar nivel y repintar todo el escenario, si el nivel terminado era el último entonces game end
        pygame.time.set_timer(end_game_event, Config.end_game_time, True)
        SoundManager.instance().stop_music(Config.end_game_time)

    def get_hero_pos(self):
        if len(self.__playerGroup) > 0:
            return self.__playerGroup.sprites()[0].get_pos()
        else:
            return pygame.math.Vector2(0.0, 0.0)

    def __get_score_xposition(self, order, total):
        return Config.screen_size[0] / total * order - Config.screen_size[0] / total / 2

    def __set_score_surface(self):
        font = AssetManager.instance().get(AssetType.Font, Config.font_name_medium)

        self.__remainingTime = Config.scene[Config.current_level]["availableTime"] - (pygame.time.get_ticks() - self.__start_ticks) / 1000

        if self.__remainingTime <= 0.0:
            self.game_over()
        else:
            currentLevel = str(Config.current_level + 1) if Config.current_level == 1 else str(Config.current_level - 1)
            if Config.current_level == 1 or Config.current_level == 2 or Config.current_level == 3:
                currentLevel = '2 - ' + str(Config.current_level)

            self.__label1 = UILabel((self.__get_score_xposition(5, 5), 25), font, "Lifes", Config.color_white)
            self.__label2 = UILabel((self.__get_score_xposition(5, 5), 50), font, str(self.__remainingLifes), Config.color_white)
            self.__label3 = UILabel((self.__get_score_xposition(1, 5), 25), font, "Score", Config.color_white)
            self.__label4 = UILabel((self.__get_score_xposition(1, 5), 50), font, str(self.__score), Config.color_white)
            self.__label5 = UILabel((self.__get_score_xposition(2, 5), 25), font, "Pizza Slices", Config.color_white)
            self.__label6 = UILabel((self.__get_score_xposition(2, 5), 50), font, str(self.__pizzaSlices), Config.color_white)
            self.__label7 = UILabel((self.__get_score_xposition(3, 5), 25), font, "Level", Config.color_white)
            self.__label8 = UILabel((self.__get_score_xposition(3, 5), 50), font, currentLevel, Config.color_white)
            self.__label9 = UILabel((self.__get_score_xposition(4, 5), 25), font, "Time", Config.color_white)
            self.__label10 = UILabel((self.__get_score_xposition(4, 5), 50), font, str(int(self.__remainingTime)), Config.color_white)