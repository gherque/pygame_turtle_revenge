#!/usr/bin/env python3

class Config:

    # Main configuration
    screen_size = (640, 480)
    game_title = "Turtle Revenge"
    background_color = (0, 0, 0)
    current_level = 4
    total_levels = 5
    collision_tolerance = 10
    game_over_time = 1000
    end_game_time = 1000

    # Font info
    font_filename = ["turtlerevenge", "assets", "fonts", "Turtles.ttf"]
    font_name_small = "font_name_small"
    font_name_medium = "font_name_medium"
    font_name_huge = "font_name_huge"
    font_name_massive = "font_name_massive"
    font_size_small = 12
    font_size_medium = 20
    font_size_huge = 50
    font_size_massive = 75
    # sizes: mini, tiny, small, medium, large, big, huge, massive

    # Sounds & Sfx
    sound_intro_name = "sound_intro"
    sound_intro_filename = ["turtlerevenge", "assets", "music", "Intro.mp3"]
    sound_gameover_name = "sound_gameover"
    sound_gameover_filename = ["turtlerevenge", "assets", "music", "GameOver.mp3"]
    sound_gameend_name = "sound_gameend"
    sound_gameend_filename = ["turtlerevenge", "assets", "music", "GameEnd.mp3"]
    sound_action_name = "sound_action"
    sound_action_filename = ["turtlerevenge", "assets", "music", "Action.mp3"]
    sound_about_name = "sound_about"
    sound_about_filename = ["turtlerevenge", "assets", "music", "About.mp3"]
    sfx_friendHello_name = "friendHello"
    sfx_friendHello_filename = ["turtlerevenge", "assets", "sfx", "friendHello.wav"]
    sfx_prize_name = "prize"
    sfx_prize_filename = ["turtlerevenge", "assets", "sfx", "prize.wav"]
    sfx_smashEnemy_name = "smashEnemy"
    sfx_smashEnemy_filename = ["turtlerevenge", "assets", "sfx", "smashEnemy.wav"]
    sfx_swordStrike_name = "swordStrike"
    sfx_swordStrike_filename = ["turtlerevenge", "assets", "sfx", "swordStrike.wav"]
    sfx_turtleDie_name = "turtleDie"
    sfx_turtleDie_filename = ["turtlerevenge", "assets", "sfx", "turtleDie.wav"]

    # Turtle brand colors
    color_red = (237, 28, 36)
    color_green = (143, 209, 41)
    color_black = (0, 0, 0)
    color_white = (255, 255, 255)

    # SpriteSheets
    turtle_spritesheet_name = "turtleSpriteSheet"
    turtle_spritesheet_filename = ["turtlerevenge", "assets", "images", "turtleSpriteSheet.gif"]
    turtle_spritesheet_coordinates_filename = ["turtlerevenge", "assets", "images", "turtleSpriteSheetCoordinates.json"]
    mario_spritesheet_name = "marioSpriteSheet"
    mario_spritesheet_filename = ["turtlerevenge", "assets", "images", "marioSpriteSheet.gif"]
    mario_spritesheet_coordinates_filename = ["turtlerevenge", "assets", "images", "marioSpriteSheetCoordinates.json"]
    pizza_spritesheet_name = "pizzaSpriteSheet"
    pizza_spritesheet_filename = ["turtlerevenge", "assets", "images", "pizzaSpriteSheet.png"]
    pizza_spritesheet_coordinates_filename = ["turtlerevenge", "assets", "images", "pizzaSpriteSheetCoordinates.json"]

    # SpriteSheets item names
    turtle_walk = ["walk1", "walk2", "walk3", "walk4"]
    turtle_jump = "jump"
    turtle_attack = ["attack1", "attack2", "attack3"]
    turtle_walk_reverse = ["walk1_reverse", "walk2_reverse", "walk3_reverse", "walk4_reverse"]
    turtle_jump_reverse = "jump_reverse"
    turtle_attack_reverse = ["attack1_reverse", "attack2_reverse", "attack3_reverse"]
    scene_floor = "floor"
    scene_floor_dark = "floor_dark"
    scene_cloud_single = "cloud_single"
    scene_cloud_double = "cloud_double"
    scene_cloud_triple = "cloud_triple"
    scene_mountain_small = "mountain_small"
    scene_mountain_big = "mountain_big"
    scene_bush_single = "bush_single"
    scene_bush_double = "bush_double"
    scene_bush_triple = "bush_triple"
    scene_castle = "castle"
    scene_big_castle = "big_castle"
    scene_pipe_vertical_end = "pipe_vertical_end"
    scene_pipe_vertical_extension = "pipe_vertical_extension"
    scene_pipe_horizontal_end = "pipe_horizontal_end"
    scene_pipe_horizontal_conn = "pipe_horizontal_conn"
    scene_block = "block"
    scene_block_dark = "block_dark"
    scene_final_flag = "final_flag"
    scene_bricks = "bricks"
    scene_bricks_dark = "bricks_dark"
    scene_addon1 = "addon1"
    scene_addon1_disable = "addon1_disable"
    pizza_spinning = ["pizza1", "pizza2", "pizza3", "pizza4", "pizza5", "pizza6"]
    mushroom = ["mushroom_walk1", "mushroom_walk2"]
    mushroom_lying_down = "mushroom_lying_down"
    mushroom_dark = ["mushroom_dark_walk1", "mushroom_dark_walk2"]
    mushroom_dark_lying_down = "mushroom_dark_lying_down"
    turtle = ["turtle_walk1", "turtle_walk2"]
    turtle_reverse = ["turtle_walk1_reverse", "turtle_walk2_reverse"]
    carnivorousPlant = ["carnivorousPlant_open", "carnivorousPlant_close"]
    carnivorousPlant_dark = ["carnivorousPlant_dark_open", "carnivorousPlant_dark_close"]
    scene_tree_trunk_block = "tree_trunk_block"
    scene_tree_top_left_block = "tree_top_left_block"
    scene_tree_top_center_block = "tree_top_center_block"
    scene_tree_top_right_block = "tree_top_right_block"

    # Entities config
    turtle_speed = 0.1
    turtle_max_jumping_height = 80.0
    pizza_speed = 0.075
    foolEnemy_speed = 0.05
    plants_speed = 0.02
    friend_speed = 0.05

    # Scene
    scene = [
        # Level 1
        {
            "availableTime": 240.0,
            "turtle_initial_position": (15, screen_size[1] - 32 - 24),
            "background_color": (0, 138, 197),
            "floorHoles": [ # Array of objects with syntax (number of floor pieces before hole after last one, number of pieces of hole)
                (70, 2),
                (15, 3),
                (64, 2),
                (69, 0)
            ],
            "floorHoles_dark": [ # Array of objects with syntax (number of floor pieces before hole after last one, number of pieces of hole)
            ],
            "clouds": {
                "single": [ # Array of coordinates
                    (9 * 16 + 17, 150 + 27),
                    (19 * 16 + 17, 150),
                    (56 * 16 + 17, 150 + 27),
                    (66 * 16 + 17, 150),
                    (103 * 16 + 17, 150 + 27),
                    (113 * 16 + 17, 150),
                    (150 * 16 + 17, 150 + 27),
                    (160 * 16 + 17, 150),
                    (193 * 16 + 17, 150 + 27),
                    (203 * 16 + 17, 150)
                ],
                "double": [ # Array of coordinates
                    (35 * 16 + 25, 150),
                    (82 * 16 + 25, 150),
                    (129 * 16 + 25, 150),
                    (176 * 16 + 25, 150),
                    (219 * 16 + 25, 150)
                ],
                "triple": [ # Array of coordinates
                    (26 * 16 + 33, 150 + 27),
                    (73 * 16 + 33, 150 + 27),
                    (120 * 16 + 33, 150 + 27),
                    (167 * 16 + 33, 150 + 27),
                    (210 * 16 + 33, 150 + 27)
                ]
            },
            "mountains": {
                "small": [ # Array of coordinates
                    (16 * 16 + 26, screen_size[1] - 16 * 2 - 10),
                    (64 * 16 + 26, screen_size[1] - 16 * 2 - 10),
                    (112 * 16 + 26, screen_size[1] - 16 * 2 - 10),
                    (160 * 16 + 26, screen_size[1] - 16 * 2 - 10),
                    (208 * 16 + 26, screen_size[1] - 16 * 2 - 10),
                ],
                "big": [ # Array of coordinates
                    (0 * 16 + 43, screen_size[1] - 16 * 2 - 18),
                    (48 * 16 + 43, screen_size[1] - 16 * 2 - 18),
                    (96 * 16 + 43, screen_size[1] - 16 * 2 - 18),
                    (144 * 16 + 43, screen_size[1] - 16 * 2 - 18),
                    (192 * 16 + 43, screen_size[1] - 16 * 2 - 18)
                ]
            },
            "bushs": {
                "single": [ # Array of coordinates
                    (24 * 16 + 17, screen_size[1] - 16 * 2 - 9),
                    (72 * 16 + 17, screen_size[1] - 16 * 2 - 9),
                    (120 * 16 + 17, screen_size[1] - 16 * 2 - 9),
                    (168 * 16 + 17, screen_size[1] - 16 * 2 - 9),
                    (216 * 16 + 17, screen_size[1] - 16 * 2 - 9)
                ],
                "double": [ # Array of coordinates
                    (42 * 16 + 25, screen_size[1] - 16 * 2 - 9),
                    (90 * 16 + 25, screen_size[1] - 16 * 2 - 9),
                    (138 * 16 + 25, screen_size[1] - 16 * 2 - 9)
                ],
                "triple": [ # Array of coordinates
                    (12 * 16 + 34, screen_size[1] - 16 * 2 - 9),
                    (60 * 16 + 34, screen_size[1] - 16 * 2 - 9),
                    (108 * 16 + 34, screen_size[1] - 16 * 2 - 9)
                ]
            },
            "castle": (202 * 16 + 42, screen_size[1] - 16 * 2 - 40),
            "big_castle": (300 * 16 + 42, screen_size[1] - 16 * 2 - 40),
            "pipes": {
                "vertical": [ # Array of objects with syntax (number of floor pieces before pipe, number of pipe extensions)
                    (28, 0),
                    (38, 1),
                    (46, 2),
                    (58, 2),
                    (164, 0),
                    (179, 0)
                ],
                "horizontal": [ # Array of objects with syntax (number of floor pieces before pipe, number of pipe extensions)
                ]
            },
            "blockStructures": [ # Array of objects with syntax (number of floor pieces before blockStructure, width in number of blocks, height in number of blocks, orientationRight 'boolean')
                (134, 4, 4, True),
                (140, 4, 4, False),
                (149, 5, 4, True),
                (156, 4, 4, False),
                (181, 9, 8, True)
            ],
            "blockStructures_dark": [ # Array of objects with syntax (number of floor pieces before hole after last one, number of pieces of hole)
            ],
            "finalFlag": (198 * 16 + 12, screen_size[1] - 16 * 2 - 85),
            "bricks": [ # Array of objects with syntax (number of floor pieces before bricks, width in number of bricks objects, height in number of pieces upper floor)
                (20, 5, 4),
                (77, 3, 4),
                (80, 8, 9),
                (91, 4, 9),
                (94, 1, 4),
                (99, 2, 4),
                (118, 1, 4),
                (121, 3, 9),
                (128, 4, 9),
                (129, 2, 4),
                (168, 4, 4)
            ],
            "bricks_dark": [ # Array of objects with syntax (number of floor pieces before bricks, width in number of bricks objects, height in number of pieces upper floor)
            ],
            "addons": [ # Array of objects with syntax (number of floor pieces before addons, height in number of pieces upper floor)
                (16, 4),
                (21, 4),
                (22, 9),
                (23, 4),
                (78, 4),
                (94, 9),
                (94, 4),
                (105, 4),
                (108, 9),
                (108, 4),
                (111, 4),
                (129, 9),
                (130, 9),
                (170, 4)
            ],
            "pizzaSlices": [ # Array of coordinates
                (1000, screen_size[1] - 150),
                (1025, screen_size[1] - 175),
                (1050, screen_size[1] - 150)
            ],
            "falls": [ # Array of objects with syntax (number of floor pieces before falls, height in number of pieces upper floor)
                (16, 4),
                (22, 9),
                (105, 4),
                (108, 9),
                (108, 4),
                (111, 4)
            ],
            "enemies": [ # Array of objects with syntax (type of enemy, number of floor pieces before enemy, height in number of pieces upper floor)
                ("mushroom", 22, 0),
                ("mushroom", 41, 0),
                ("mushroom", 51, 0),
                ("mushroom", 54, 0),
                ("mushroom", 80, 10),
                ("mushroom", 83, 10),
                ("mushroom", 97, 0),
                ("mushroom", 99, 0),
                ("mushroom", 114, 0),
                ("mushroom", 116, 0),
                ("mushroom", 124, 0),
                ("mushroom", 126, 0),
                ("mushroom", 130, 0),
                ("mushroom", 132, 0),
                ("mushroom", 174, 0),
                ("mushroom", 176, 0)
            ],
            "friends": [ # Array of objects with syntax (type of friend, number of floor pieces before friend, height in number of pieces upper floor)
                ("turtle", 107, 0)
            ],
            "trees": [ # Array of objects with syntax (number of floor pieces before tree trunk, height in number of pieces upper floor, width in number of pieces of tree trunk)
            ]
        },
        # Level 2 - 1
        {
            "availableTime": 240.0,
            "turtle_initial_position": (40, screen_size[1] - 32 - 24),
            "background_color": (0, 138, 197),
            "floorHoles": [ # Array of objects with syntax (number of floor pieces before hole after last one, number of pieces of hole)
                (24, 24)
            ],
            "floorHoles_dark": [ # Array of objects with syntax (number of floor pieces before hole after last one, number of pieces of hole)
            ],
            "clouds": {
                "single": [ # Array of coordinates
                    (10 * 16 + 17, 150 + 27)
                ],
                "double": [ # Array of coordinates
                    (4 * 16 + 25, 150)
                ],
                "triple": [ # Array of coordinates
                    (18 * 16 + 33, 150 + 27)
                ]
            },
            "mountains": {
                "small": [ # Array of coordinates
                ],
                "big": [ # Array of coordinates
                ]
            },
            "bushs": {
                "single": [ # Array of coordinates
                ],
                "double": [ # Array of coordinates
                ],
                "triple": [ # Array of coordinates
                ]
            },
            "castle": (0 + 42, screen_size[1] - 16 * 2 - 40),
            "big_castle": (300 * 16 + 42, screen_size[1] - 16 * 2 - 40),
            "pipes": {
                "vertical": [ # Array of objects with syntax (number of floor pieces before pipe, number of pipe extensions)
                    (12, 2)
                ],
                "horizontal": [ # Array of objects with syntax (number of floor pieces before each horizontal pipe, number of pices of height)
                    (10, 0)
                ]
            },
            "blockStructures": [ # Array of objects with syntax (number of floor pieces before blockStructure, width in number of blocks, height in number of blocks, orientationRight 'boolean')
            ],
            "blockStructures_dark": [ # Array of objects with syntax (number of floor pieces before hole after last one, number of pieces of hole)
            ],
            "finalFlag": (1000, screen_size[1] - 16 * 2 - 85),
            "bricks": [ # Array of objects with syntax (number of floor pieces before bricks, width in number of bricks objects, height in number of pieces upper floor)
            ],
            "bricks_dark": [ # Array of objects with syntax (number of floor pieces before bricks, width in number of bricks objects, height in number of pieces upper floor)
            ],
            "addons": [ # Array of objects with syntax (number of floor pieces before addons, height in number of pieces upper floor)
            ],
            "pizzaSlices": [ # Array of coordinates
            ],
            "falls": [ # Array of objects with syntax (number of floor pieces before falls, height in number of pieces upper floor)
            ],
            "enemies": [ # Array of objects with syntax (type of enemy, number of floor pieces before enemy, height in number of pieces upper floor)
            ],
            "friends": [ # Array of objects with syntax (type of friend, number of floor pieces before friend, height in number of pieces upper floor)
            ],
            "trees": [ # Array of objects with syntax (number of floor pieces before tree trunk, height in number of pieces upper floor, width in number of pieces of tree trunk)
            ]
        },
        # Level 2 - 2
        {
            "availableTime": 240.0,
            "turtle_initial_position": (50, screen_size[1] - 32 - 24),
            "background_color": (0, 0, 0),
            "floorHoles": [ # Array of objects with syntax (number of floor pieces before hole after last one, number of pieces of hole)
            ],
            "floorHoles_dark": [ # Array of objects with syntax (number of floor pieces before hole after last one, number of pieces of hole)
                (80, 3),
                (37, 2),
                (2, 2),
                (12, 8),
                (8, 8),
                (30, 0)
            ],
            "clouds": {
                "single": [ # Array of coordinates
                ],
                "double": [ # Array of coordinates
                ],
                "triple": [ # Array of coordinates
                ]
            },
            "mountains": {
                "small": [ # Array of coordinates
                ],
                "big": [ # Array of coordinates
                ]
            },
            "bushs": {
                "single": [ # Array of coordinates
                ],
                "double": [ # Array of coordinates
                ],
                "triple": [ # Array of coordinates
                ]
            },
            "castle": (5000, screen_size[1] - 16 * 2 - 40),
            "big_castle": (300 * 16 + 42, screen_size[1] - 16 * 2 - 40),
            "pipes": {
                "vertical": [ # Array of objects with syntax (number of floor pieces before pipe, number of pipe extensions)
                    (103, 1),
                    (109, 2),
                    (115, 0),
                    (171, 40)
                ],
                "horizontal": [ # Array of objects with syntax (number of floor pieces before each horizontal pipe, number of pices of height)
                    (169, 3)
                ]
            },
            "blockStructures": [ # Array of objects with syntax (number of floor pieces before hole after last one, number of pieces of hole)
            ],
            "blockStructures_dark": [ # Array of objects with syntax (number of floor pieces before blockStructure, width in number of blocks, height in number of blocks, orientationRight 'boolean')
                (17, 1, 1, True),
                (19, 1, 2, True),
                (21, 1, 3, True),
                (23, 1, 4, True),
                (25, 1, 4, True),
                (27, 1, 3, True),
                (31, 1, 3, True),
                (33, 1, 2, True),
                (133, 5, 4, True)
            ],
            "finalFlag": (5000, screen_size[1] - 16 * 2 - 85),
            "bricks": [ # Array of objects with syntax (number of floor pieces before bricks, width in number of bricks objects, height in number of pieces upper floor)
            ],
            "bricks_dark": [ # Array of objects with syntax (number of floor pieces before bricks, width in number of bricks objects, height in number of pieces upper floor)
                (0, 1, 0),
                (0, 1, 1),
                (0, 1, 2),
                (0, 1, 3),
                (0, 1, 4),
                (0, 1, 5),
                (0, 1, 6),
                (0, 1, 7),
                (0, 1, 8),
                (0, 1, 9),
                (0, 1, 10),
                (0, 1, 11),
                (0, 1, 12),
                (0, 1, 13),
                (0, 1, 14),
                (0, 1, 15),
                (0, 1, 16),
                (0, 1, 17),
                (0, 1, 18),
                (0, 1, 19),
                (6, 150, 19),
                (39, 3, 4),
                (39, 1, 5),
                (39, 1, 6),
                (41, 1, 5),
                (41, 4, 6),
                (44, 1, 5),
                (44, 3, 4),
                (46, 1, 5),
                (46, 1, 6),
                (51, 4, 4),
                (51, 2, 5),
                (51, 2, 6),
                (51, 2, 7),
                (51, 2, 8),
                (51, 2, 9),
                (53, 2, 10),
                (53, 2, 11),
                (53, 2, 12),
                (53, 2, 13),
                (53, 2, 14),
                (53, 2, 15),
                (53, 2, 16),
                (53, 2, 17),
                (53, 2, 18),
                (53, 2, 19),
                (57, 6, 19),
                (57, 6, 18),
                (57, 6, 17),
                (57, 6, 16),
                (57, 6, 15),
                (57, 6, 14),
                (57, 6, 13),
                (57, 6, 12),
                (57, 6, 11),
                (57, 6, 10),
                (61, 2, 9),
                (61, 2, 8),
                (61, 2, 7),
                (61, 2, 6),
                (61, 2, 5),
                (57, 6, 4),
                (65, 4, 19),
                (65, 4, 18),
                (65, 4, 17),
                (65, 4, 16),
                (65, 4, 15),
                (65, 4, 14),
                (65, 4, 13),
                (65, 4, 12),
                (65, 4, 11),
                (65, 4, 10),
                (66, 1, 9),
                (66, 1, 8),
                (66, 1, 7),
                (66, 1, 6),
                (66, 1, 5),
                (66, 3, 4),
                (68, 1, 5),
                (71, 2, 9),
                (71, 2, 8),
                (71, 2, 7),
                (71, 2, 6),
                (71, 2, 5),
                (71, 2, 4),
                (75, 4, 4),
                (75, 4, 10),
                (75, 4, 11),
                (75, 4, 12),
                (75, 4, 13),
                (75, 4, 14),
                (75, 4, 15),
                (75, 4, 16),
                (75, 4, 17),
                (75, 4, 18),
                (75, 4, 19),
                (84, 6, 5),
                (84, 6, 6),
                (122, 2, 0),
                (122, 2, 1),
                (122, 2, 2),
                (146, 7, 4),
                (162, 30, 0),
                (162, 30, 1),
                (162, 30, 2),
                (173, 20, 3),
                (173, 20, 4),
                (173, 20, 5),
                (173, 20, 6),
                (173, 20, 7),
                (173, 20, 8),
                (173, 20, 9),
                (173, 20, 10),
                (173, 20, 11),
                (173, 20, 12),
                (173, 20, 13),
                (173, 20, 14),
                (173, 20, 15),
                (173, 20, 16),
                (173, 20, 17),
                (173, 20, 18),
                (173, 20, 19)
            ],
            "addons": [ # Array of objects with syntax (number of floor pieces before addons, height in number of pieces upper floor)
                (10, 4),
                (11, 4),
                (12, 4),
                (13, 4),
                (14, 4),
            ],
            "pizzaSlices": [ # Array of coordinates
                (39 * 16 + 9, screen_size[1] - 9 * 16 - 13),
                (41 * 16 + 9, screen_size[1] - 9 * 16 - 13),
                (43 * 16 + 9, screen_size[1] - 9 * 16 - 13),
                (45 * 16 + 9, screen_size[1] - 9 * 16 - 13),
                (56 * 16 + 9, screen_size[1] - 7 * 16 - 13),
                (58 * 16 + 9, screen_size[1] - 7 * 16 - 13),
                (67 * 16 + 9, screen_size[1] - 8 * 16 - 13),
                (82 * 16 + 9, screen_size[1] - 10 * 16 - 13),
                (84 * 16 + 9, screen_size[1] - 10 * 16 - 13),
                (86 * 16 + 9, screen_size[1] - 10 * 16 - 13),
                (88 * 16 + 9, screen_size[1] - 10 * 16 - 13)
            ],
            "falls": [ # Array of objects with syntax (number of floor pieces before falls, height in number of pieces upper floor)
                (8, 5),
                (16, 5)
            ],
            "enemies": [ # Array of objects with syntax (type of enemy, number of floor pieces before enemy, height in number of pieces upper floor)
                ("mushroom_dark", 12, 0),
                ("mushroom_dark", 14, 0),
                ("mushroom_dark", 29, 0),
                ("mushroom_dark", 63, 0),
                ("mushroom_dark", 65, 0),
                ("mushroom_dark", 72, 10),
                ("mushroom_dark", 76, 5),
                ("mushroom_dark", 78, 5),
                ("mushroom_dark", 97, 0),
                ("mushroom_dark", 99, 0),
                ("mushroom_dark", 101, 0),
                ("mushroom_dark", 113, 0),
                ("carnivorousPlant_dark", 104, 3),
                ("carnivorousPlant_dark", 110, 4),
                ("carnivorousPlant_dark", 116, 2)
            ],
            "friends": [ # Array of objects with syntax (type of friend, number of floor pieces before friend, height in number of pieces upper floor)
                ("turtle", 45, 0),
                ("turtle", 47, 0),
                ("turtle", 67, 0)
            ],
            "trees": [ # Array of objects with syntax (number of floor pieces before tree trunk, height in number of pieces upper floor, width in number of pieces of tree trunk)
            ]
        },
        # Level 2 - 3
        {
            "availableTime": 240.0,
            "turtle_initial_position": (65, screen_size[1] - 32 - 32 - 24),
            "background_color": (0, 138, 197),
            "floorHoles": [ # Array of objects with syntax (number of floor pieces before hole after last one, number of pieces of hole)
                (55, 0)
            ],
            "floorHoles_dark": [ # Array of objects with syntax (number of floor pieces before hole after last one, number of pieces of hole)
            ],
            "clouds": {
                "single": [ # Array of coordinates
                    (25 * 16 + 17, 150 + 27),
                    (36 * 16 + 17, 150)
                ],
                "double": [ # Array of coordinates
                    (5 * 16 + 25, 150)
                ],
                "triple": [ # Array of coordinates
                ]
            },
            "mountains": {
                "small": [ # Array of coordinates
                    (32 * 16 + 26, screen_size[1] - 16 * 2 - 10)
                ],
                "big": [ # Array of coordinates
                    (16 * 16 + 43, screen_size[1] - 16 * 2 - 18)
                ]
            },
            "bushs": {
                "single": [ # Array of coordinates
                    (40 * 16 + 17, screen_size[1] - 32 - 9)
                ],
                "double": [ # Array of coordinates
                ],
                "triple": [ # Array of coordinates
                ]
            },
            "castle": (26 * 16 + 42, screen_size[1] - 16 * 2 - 40),
            "big_castle": (300 * 16 + 42, screen_size[1] - 16 * 2 - 40),
            "pipes": {
                "vertical": [ # Array of objects with syntax (number of floor pieces before pipe, number of pipe extensions)
                    (3, 0)
                ],
                "horizontal": [ # Array of objects with syntax (number of floor pieces before each horizontal pipe, number of pices of height)
                ]
            },
            "blockStructures": [ # Array of objects with syntax (number of floor pieces before blockStructure, width in number of blocks, height in number of blocks, orientationRight 'boolean')
                (5, 9, 8, True)
            ],
            "blockStructures_dark": [ # Array of objects with syntax (number of floor pieces before hole after last one, number of pieces of hole)
            ],
            "finalFlag": (23 * 16, screen_size[1] - 16 * 2 - 85),
            "bricks": [ # Array of objects with syntax (number of floor pieces before bricks, width in number of bricks objects, height in number of pieces upper floor)
            ],
            "bricks_dark": [ # Array of objects with syntax (number of floor pieces before bricks, width in number of bricks objects, height in number of pieces upper floor)
            ],
            "addons": [ # Array of objects with syntax (number of floor pieces before addons, height in number of pieces upper floor)
            ],
            "pizzaSlices": [ # Array of coordinates
            ],
            "falls": [ # Array of objects with syntax (number of floor pieces before falls, height in number of pieces upper floor)
            ],
            "enemies": [ # Array of objects with syntax (type of enemy, number of floor pieces before enemy, height in number of pieces upper floor)
            ],
            "friends": [ # Array of objects with syntax (type of friend, number of floor pieces before friend, height in number of pieces upper floor)
            ],
            "trees": [ # Array of objects with syntax (number of floor pieces before tree trunk, height in number of pieces upper floor, width in number of pieces of tree trunk)
            ]
        },
        # Level 3
        {
            "availableTime": 240.0,
            "turtle_initial_position": (40, screen_size[1] - 32 - 24),
            "background_color": (0, 138, 197),
            "floorHoles": [ # Array of objects with syntax (number of floor pieces before hole after last one, number of pieces of hole)
                (16, 200)
            ],
            "floorHoles_dark": [ # Array of objects with syntax (number of floor pieces before hole after last one, number of pieces of hole)
            ],
            "clouds": {
                "single": [ # Array of coordinates
                    (9 * 16 + 17, 150 + 127),
                    (36 * 16 + 17, 150 + 127),
                    (40 * 16 + 17, 150 + 100),
                    (48 * 16 + 17, 150 + 160),
                    (60 * 16 + 17, 150 + 127),
                    (87 * 16 + 17, 150 + 127),
                    (91 * 16 + 17, 150 + 100),
                    (99 * 16 + 17, 150 + 160),
                    (111 * 16 + 17, 150 + 127),
                    (138 * 16 + 17, 150 + 127),
                    (142 * 16 + 17, 150 + 100),
                    (150 * 16 + 17, 150 + 160),
                    (162 * 16 + 17, 150 + 127),
                    (189 * 16 + 17, 150 + 127),
                    (193 * 16 + 17, 150 + 100),
                    (201 * 16 + 17, 150 + 160),
                ],
                "double": [ # Array of coordinates
                    (3 * 16 + 25, 150 + 27),
                    (19 * 16 + 25, 150),
                    (54 * 16 + 25, 150 + 27),
                    (70 * 16 + 25, 150),
                    (105 * 16 + 25, 150 + 27),
                    (121 * 16 + 25, 150),
                    (156 * 16 + 25, 150 + 27),
                    (172 * 16 + 25, 150)
                ],
                "triple": [ # Array of coordinates
                ]
            },
            "mountains": {
                "small": [ # Array of coordinates
                ],
                "big": [ # Array of coordinates
                ]
            },
            "bushs": {
                "single": [ # Array of coordinates
                ],
                "double": [ # Array of coordinates
                ],
                "triple": [ # Array of coordinates
                ]
            },
            "castle": (0 + 42, screen_size[1] - 16 * 2 - 40),
            "big_castle": (300 * 16 + 75, screen_size[1] - 16 * 2 - 87),
            "pipes": {
                "vertical": [ # Array of objects with syntax (number of floor pieces before pipe, number of pipe extensions)
                ],
                "horizontal": [ # Array of objects with syntax (number of floor pieces before each horizontal pipe, number of pices of height)
                ]
            },
            "blockStructures": [ # Array of objects with syntax (number of floor pieces before blockStructure, width in number of blocks, height in number of blocks, orientationRight 'boolean')
            ],
            "blockStructures_dark": [ # Array of objects with syntax (number of floor pieces before hole after last one, number of pieces of hole)
            ],
            "finalFlag": (1000, screen_size[1] - 16 * 2 - 85),
            "bricks": [ # Array of objects with syntax (number of floor pieces before bricks, width in number of bricks objects, height in number of pieces upper floor)
            ],
            "bricks_dark": [ # Array of objects with syntax (number of floor pieces before bricks, width in number of bricks objects, height in number of pieces upper floor)
            ],
            "addons": [ # Array of objects with syntax (number of floor pieces before addons, height in number of pieces upper floor)
            ],
            "pizzaSlices": [ # Array of coordinates
            ],
            "falls": [ # Array of objects with syntax (number of floor pieces before falls, height in number of pieces upper floor)
            ],
            "enemies": [ # Array of objects with syntax (type of enemy, number of floor pieces before enemy, height in number of pieces upper floor)
            ],
            "friends": [ # Array of objects with syntax (type of friend, number of floor pieces before friend, height in number of pieces upper floor)
            ],
            "trees": [ # Array of objects with syntax (number of floor pieces before tree trunk, height in number of pieces upper floor, width in number of pieces of tree trunk)
                (19, 3, 2),
                (27, 10, 3),
                (25, 6, 6)
            ]
        }
    ]

    # Scores
    pizza_slice_score = 100
    mushroom_killed_score = 200

    # explosion_name = "explosion"
    # explosion_image_filename = ["turtlerevenge", "assets", "images", "explosion.png"]
    # explosion_size = (4,4)
    # explosion_time_per_sequence = 40

    # jungle_name = "jungle"
    # jungle_image_filename = ["turtlerevenge", "assets", "images", "jungle.png"]
    # jungle_speed = 0.3
    # clouds_name = "clouds"
    # clouds_image_filename = ["turtlerevenge", "assets", "images", "clouds.png"]
    # clouds_speed = 0.4

    # allied_gunfire_name = "allied_gunfire"
    # allied_gunfire_filename = ["turtlerevenge", "assets", "sfx", "allied_gunfire.wav"]
    # enemy_gunfire_name = "enemy_gunfire"
    # enemy_gunfire_filename = ["turtlerevenge", "assets", "sfx", "enemy_gunfire.wav"]
    # explosion1_name = "explosion1"
    # explosion1_filename = ["turtlerevenge", "assets", "sfx", "explosion1.wav"]
    # explosion2_name = "explosion2"
    # explosion2_filename = ["turtlerevenge", "assets", "sfx", "explosion2.wav"]

    # mission_theme_name = "mission"
    # mission_theme_filename = ["turtlerevenge", "assets", "music", "mission.ogg"]

    # allied_bullet_velocity = (0.0, -0.3)

    # Debug configuration
    fps = 60
    time_per_frame = 1000.0 / fps
    refresh_stats_time = 1000.0
    fps_stats_pos = (0, 2)
    debug = False
    debug_collider_color = (0, 255, 255)
    debug_render_color = (0, 0, 255)

    # debug_way_point_color = (0,255,0)
    # waypoints_area = (screen_size[0], screen_size[1] / 2)
    # waypoints_separation = (120, 100)

    # enemies_spawn_probability = 0.01
    # enemies_max_waypoints = 5
    # enemies_projectile_speed_range = (0.1, 0.4)
    # enemies_kamikaze_probability = 0.3
    # enemies_data = {
    #     "raptor" : { "fire_rate" : 0.005, "speed" : 0.1, "acceleration" : 0.005},
    #     "avenger" : { "fire_rate" : 0.01, "speed" : 0.12, "acceleration" : 0.005} }

    # enemies_spawn_points = [(-100, 0),
    #                         (100, -100),
    #                         (screen_size[0]/2, -100),
    #                         (screen_size[0] - 100 , -100),
    #                         (screen_size[0] + 100, 0)]

    # enemies_end_points = [(-100, 0),
    #                         (100, -100),
    #                         (-100, screen_size[1]),
    #                         (100, screen_size[1] + 100),
    #                         (screen_size[0]/2, screen_size[1] + 100),
    #                         (screen_size[0] - 100 , screen_size[1] + 100),
    #                         (screen_size[0] + 100, screen_size[1])]

    def __init__(self):
        pass
