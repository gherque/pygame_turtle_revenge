#!/usr/bin/env python3

class Config:

    # Main configuration
    screen_size = (640, 480)
    game_title = "Turtle Revenge"
    background_color = (0, 0, 0)
    gaming_background_color = (0, 138, 197)
    current_level = 0
    total_levels = 3
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

    # Sounds
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
    scene_cloud_single = "cloud_single"
    scene_cloud_double = "cloud_double"
    scene_cloud_triple = "cloud_triple"
    scene_mountain_small = "mountain_small"
    scene_mountain_big = "mountain_big"
    scene_bush_single = "bush_single"
    scene_bush_double = "bush_double"
    scene_bush_triple = "bush_triple"
    scene_castle = "castle"
    scene_pipe_vertical_end = "pipe_vertical_end"
    scene_pipe_vertical_extension = "pipe_vertical_extension"
    scene_block = "block"
    scene_final_flag = "final_flag"
    scene_bricks = "bricks"
    scene_addon1 = "addon1"
    scene_addon1_disable = "addon1_disable"
    pizza_spinning = ["pizza1", "pizza2", "pizza3", "pizza4", "pizza5", "pizza6"]
    mushroom = ["mushroom_walk1", "mushroom_walk2"]
    mushroom_lying_down = "mushroom_lying_down"
    turtle = ["turtle_walk1", "turtle_walk2"]
    turtle_reverse = ["turtle_walk1_reverse", "turtle_walk2_reverse"]

    # Entities config
    turtle_speed = 0.1
    turtle_max_jumping_height = 80.0
    turtle_initial_position = (15, screen_size[1] - 32 - 24)
    pizza_speed = 0.075
    foolEnemy_speed = 0.05
    friend_speed = 0.05

    # Scene
    scene = [
        # Level 0
        {
            "floorHoles": [ # Array of objects with syntax (number of floor pieces before hole after last one, number of pieces of hole)
                (70, 2),
                (15, 3),
                (64, 2),
                (69, 0)
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
            "pipes": {
                "vertical": [ # Array of objects with syntax (number of floor pieces before pipe, number of pipe extensions)
                    (28, 0),
                    (38, 1),
                    (46, 2),
                    (58, 2),
                    (164, 0),
                    (179, 0)
                ]
            },
            "blockStructures": [ # Array of objects with syntax (number of floor pieces before blockStructure, width in number of blocks, height in number of blocks, orientationRight 'boolean')
                (134, 4, 4, True),
                (140, 4, 4, False),
                (149, 5, 4, True),
                (156, 4, 4, False),
                (181, 9, 8, True)
            ],
            "finalFlag": (198 * 16 + 12, screen_size[1] - 16 * 2 - 85),
            "bricks": [ # Array of objects with syntax (number of floor pieces before bricks, width in number of bricks objects, height in number of pieces upper floor)
                (20, 5, 4),
                (77, 3, 4),
                (80, 8, 8),
                (91, 4, 8),
                (94, 1, 4),
                (99, 2, 4),
                (118, 1, 4),
                (121, 3, 8),
                (128, 4, 8),
                (129, 2, 4),
                (168, 4, 4)
            ],
            "addons": [ # Array of objects with syntax (number of floor pieces before addons, height in number of pieces upper floor)
                (16, 4),
                (21, 4),
                (22, 8),
                (23, 4),
                (78, 4),
                (94, 8),
                (94, 4),
                (105, 4),
                (108, 8),
                (108, 4),
                (111, 4),
                (129, 8),
                (130, 8),
                (170, 4)
            ],
            "pizzaSlices": [ # Array of coordinates
                (1000, screen_size[1] - 150),
                (1025, screen_size[1] - 175),
                (1050, screen_size[1] - 150)
            ],
            "falls": [ # Array of objects with syntax (number of floor pieces before falls, height in number of pieces upper floor)
                (16, 4),
                (22, 8),
                (105, 4),
                (108, 8),
                (108, 4),
                (111, 4)
            ],
            "enemies": [ # Array of objects with syntax (type of enemy, number of floor pieces before enemy, height in number of pieces upper floor)
                ("mushroom", 22, 0),
                ("mushroom", 41, 0),
                ("mushroom", 51, 0),
                ("mushroom", 54, 0),
                ("mushroom", 80, 9),
                ("mushroom", 83, 9),
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
