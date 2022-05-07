from math import pi
import pygame as pg

class Constants:
    def __init__(self):
        pg.init()

        self.init_fps()
        self.init_masses()
        self.init_numbers()
        self.init_radii()
        self.init_colors()
        self.init_speeds()
        self.init_damage()
        self.init_probabilities()
        self.init_powerups()
        self.init_sounds()

        # constrains
        self.horizontal_constrain = 50
        self.vertical_constrain = 20

        # artifact
        self.artifact_width = 15

    def init_fps(self):
        self.fps = 120
        self.dt = 1 / self.fps

    def init_masses(self):
        self.density = 0.0001
        self.nucleon_mass = 1
        self.electron_mass = 0.2

        self.max_enemy_mass = 4
        self.min_enemy_mass = 0.33

    def init_numbers(self):
        self.max_nucleons = 12
        self.max_electrons = 6
        self.max_nuclear_radius = pow(self.max_nucleons * self.nucleon_mass / (4 * pi * self.density), 1/3)
        self.max_mass = self.max_nucleons * self.nucleon_mass + self.max_electrons * self.electron_mass

    def init_radii(self):
        self.electron_radius = 6
        self.projectile_radius = 4

        self.higgs_radius = 50

    def init_speeds(self):
        self.scroll_speed = 300
        self.atom_speed_front = 150
        self.atom_speed_back = 200
        self.atom_speed_vertical = 300
        self.nucleus_speed_front = 240
        self.nucleus_speed_back = 300
        self.nucleus_speed_vertical = 480
        self.projectile_speed = 600
        self.enemy_speed = 150
        self.artifact_slide_speed = 100

    def init_colors(self):
        self.normal_nucleus_color = pg.Color("#1f51ff")
        self.normal_electron_color = pg.Color("white")
        self.anti_nucleus_color = pg.Color("red")
        self.anti_electron_color = pg.Color("purple")
        self.ripples_color = pg.Color("green")
        self.artifact_color = pg.Color("yellow")
        self.annihilation_color = pg.Color("white")

    def init_damage(self):
        # damage intensities
        self.damage_to_enemy = 1
        self.damage_to_player = 1

        # damage parameters
        self.collision_collateral = 0.2
        self.mass_absorption = 0.5

        # enemy fire cycle
        self.enemy_fire_cycle = 100

        # energy parameters
        self.mass_energy_refill = 1
        self.energy_increase_cycle =100
        self.max_energy = 100
        self.energy_per_shot = 5
        self.energy_replenish_rate = 0.5

    def init_probabilities(self):
        self.enemy_probability = 0.7
        self.artifact_probability = 0.6
        self.higgs_probability = 0.25

    def init_powerups(self):
        self.higgs_mass_cutoff = 0.4 * self.max_mass
        self.higgs_mass_gain = 0.25 * self.max_mass

    def init_sounds(self):
        self.button_clicked_sound = pg.mixer.Sound("sounds/button_press.wav")
        self.start_game_sound = pg.mixer.Sound("sounds/start_game.wav")
        self.main_menu_sound = pg.mixer.Sound("sounds/main_menu.wav")
        self.pause_menu_sound = pg.mixer.Sound("sounds/pause_menu.wav")

    def set_screen_size(self, screen):
        self.screen_width, self.screen_height = screen.get_size()

        # quantities that required screen size for calculation
        self.border_thickness = self.screen_height / 20
        self.artifact_height = self.screen_height / 4
        
        self.init_ui()

    def set_dt(self, dt):
        self.dt = dt

    def init_ui(self):
        # font size
        self.title_font_size = int(self.screen_height / 25)
        self.indicator_font_size = int(self.screen_height / 40)

        # progress bar
        self.progress_bar_thickness = 10

        # buttons
        self.button_font_size = self.screen_height // 30
        self.button_width = self.screen_width // 5
        self.button_height = self.screen_height // 15

consts = Constants()