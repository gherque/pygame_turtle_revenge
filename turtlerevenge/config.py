#!/usr/bin/env python3

class Config:

    # Main configuration
    screen_size = (640, 480)
    game_title = "Turtle Revenge"
    background_color = (0, 0, 0)
    gaming_background_color = (0, 138, 197)
    current_level = 0

    # Font info
    font_filename = ["turtlerevenge", "assets", "fonts", "Turtles.ttf"]
    font_name_huge = "font_turtlesTitles"
    font_name_massive = "font_gameover"
    font_name_small = "font_turtles"
    font_size_small = 12
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

    # Hero config
    turtle_speed = 0.15
    turtle_fire_cooldown = 300
    turtle_max_jumping_height = 100.0
    turtle_initial_position = (15, screen_size[1] - 48 - 32 + 24)

    # Scene
    scene = [
        # Level 0
        {
            "floorHoles": [ # Array of objects with syntax (number of floor pieces before hole without corner, number of pieces of hole)
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
                    (223 * 16 + 25, 150)
                ],
                "triple": [ # Array of coordinates
                    (26 * 16 + 33, 150 + 27),
                    (73 * 16 + 33, 150 + 27),
                    (110 * 16 + 33, 150 + 27),
                    (147 * 16 + 33, 150 + 27),
                    (184 * 16 + 33, 150 + 27)
                ]
            },
            "mountains": {
                "small": [ # Array of coordinates
                    (16 * 16 + 26, screen_size[1] - 16 * 2 - 10)
                ],
                "big": [ # Array of coordinates
                    (0 * 16 + 43, screen_size[1] - 16 * 2 - 18)
                ]
            }
        }
    ]

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

    # enemy_raptor_name = "raptor"
    # enemy_avenger_name = "avenger"

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

    game_over_time = 5000
    end_game_time = 1000

    def __init__(self):
        pass
