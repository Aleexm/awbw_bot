from dicts import TERRAIN_DICT
from consts import *
from weather import Weather
import pygame
import enum

class Terrain(pygame.sprite.Sprite):
    def __init__(self, id, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.id = id
        self.set_sprite(self.id)
        self.rect = self.image.get_rect()
        self.type = self.get_type()
        self.coordinates = (x, y)
        self.country = self.get_country()

    def set_sprite(self, id):
        temp = pygame.image.load(TERRAIN_DICT[id]).convert()
        self.image = pygame.transform.scale(temp, (temp.get_size()[0]*SCALER,
                                                   temp.get_size()[1]*SCALER))

    def get_type(self):
        "Remaps AWBW ids to actual terrain Types"
        if self.id == 1:
            return Plain()
        if self.id == 2:
            return Mountain()
        if self.id == 3:
            return Wood()
        if self.id in list(range(4,15)):
            return River()
        if self.id in list(range(15,26)):
            return Road()
        if self.id in [26, 27]:
            return Bridge()
        if self.id == 28:
            return Sea()
        if self.id in list(range(29,33)):
            return Shoal()
        if self.id == 33:
            return Reef()
        if self.id in [34, 38, 43, 48, 53, 81, 86, 91, 96, 119, 124, 151, 158, 165, 172, 183, 190]:
            return City()
        if self.id in [35, 39, 44, 49, 54, 82, 87, 92, 97, 118, 123, 150, 157, 164, 171, 182, 189]:
            return Base()
        if self.id in [36, 40, 45, 50, 55, 83, 88, 93, 98, 117, 122, 149, 156, 163, 170, 181, 188]:
            return Airport()
        if self.id in [37, 41, 46, 51, 56, 84, 89, 94, 99, 121, 126, 155, 162, 169, 176, 187, 194]:
            return Port()
        if self.id in [127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 152, 159, 166, 173, 184, 191]:
            return Comtower()
        if self.id in [138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 154, 161, 168, 175, 186, 193]:
            return Lab()
        if self.id in [42, 47, 52, 57, 85, 90, 95, 100, 120, 125, 153, 160, 167, 174, 185, 192]:
            return HQ()
        if self.id in list(range(101, 111)):
            return Pipe()
        if self.id in [113, 114]:
            return Pipeseam()
        if self.id in [115, 116]:
            return Rubble()
        if self.id in [111, 112]:
            return Missile()

    def get_country(self):
        "see https://awbw.amarriner.com/countries.php"
        if self.id in [34,35,36,37,133,145]: #Neutral
            return 0
        if self.id in [38,39,40,41,42,134,146]: #OS
            return 1
        if self.id in [43,44,45,46,47,129,140]: #BM etc
            return 2
        if self.id in [48,49,50,51,52,131,142]:
            return 3
        if self.id in [53,54,55,56,57,136,148]:
            return 4
        if self.id in [91,92,93,94,95,128,139]:
            return 5
        if self.id in [81,82,83,84,85,135,147]:
            return 6
        if self.id in [86,87,88,89,90,137,143]:
            return 7
        if self.id in [96,97,98,99,100,130,141]:
            return 8
        if self.id in [117,118,119,120,121,127,138]:
            return 9
        if self.id in [122,123,124,125,126,132,144]:
            return 10
        if self.id in [149,150,151,152,153,154,155]:
            return 11
        if self.id in [156,157,158,159,160,161,162]:
            return 12
        if self.id in [163,164,165,166,167,168,169]:
            return 13
        if self.id in [170,171,172,173,174,175,176]:
            return 14
        if self.id in [181,182,183,184,185,186,187]:
            return 15
        if self.id in [188,189,190,191,192,193,194]:
            return 16
        return -1 # Just a terrain tile, no country
        return country

class Plain(Terrain):
    def __init__(self):
        self.defense = 1
        self.movement = {
            Weather.Clear : [1 ,1 ,1 ,2 ,1 ,0 ,0 ,0],
            Weather.Rain  : [1 ,1 ,2 ,3 ,1 ,0 ,0 ,0],
            Weather.Snow  : [2 ,1 ,2 ,3 ,2 ,0 ,0 ,0]
        }

    def __repr__(self):
        return 'plain'

class Mountain(Terrain):
    def __init__(self):
        self.defense = 4
        self.movement = {
            Weather.Clear : [2 ,1 ,0 ,0 ,1 ,0 ,0 ,0],
            Weather.Rain  : [2 ,1 ,0 ,0 ,1 ,0 ,0 ,0],
            Weather.Snow  : [4 ,2 ,0 ,0 ,2 ,0 ,0 ,0]
        }

    def __repr__(self):
        return 'mountain'

class Wood(Terrain):
    def __init__(self):
        self.defense = 2
        self.movement = {
            Weather.Clear : [1 ,1 ,2 ,3 ,1 ,0 ,0 ,0],
            Weather.Rain  : [1 ,1 ,3 ,4 ,1 ,0 ,0 ,0],
            Weather.Snow  : [2 ,1 ,2 ,3 ,2 ,0 ,0 ,0]
        }

    def __repr__(self):
        return 'wood'

class River(Terrain):
    def __init__(self):
        self.defense = 0
        self.movement = {
            Weather.Clear : [2 ,1 ,0 ,0 ,1 ,0 ,0 ,0],
            Weather.Rain  : [2 ,1 ,0 ,0 ,1 ,0 ,0 ,0],
            Weather.Snow  : [2 ,1 ,0 ,0 ,2 ,0 ,0 ,0]
        }

    def __repr__(self):
        return 'river'

class Road(Terrain):
    def __init__(self):
        self.defense = 0
        self.movement = {
            Weather.Clear : [1 ,1 ,1 ,1 ,1 ,0 ,0 ,0],
            Weather.Rain  : [1 ,1 ,1 ,1 ,1 ,0 ,0 ,0],
            Weather.Snow  : [1 ,1 ,1 ,1 ,2 ,0 ,0 ,0]
        }

    def __repr__(self):
        return 'road'

class Bridge(Terrain):
    def __init__(self):
        self.defense = 0
        self.movement = {
            Weather.Clear : [1 ,1 ,1 ,1 ,1 ,0 ,0 ,0],
            Weather.Rain  : [1 ,1 ,1 ,1 ,1 ,0 ,0 ,0],
            Weather.Snow  : [1 ,1 ,1 ,1 ,2 ,0 ,0 ,0]
        }

    def __repr__(self):
        return 'bridge'

class Sea(Terrain):
    def __init__(self):
        self.defense = 0
        self.movement = {
            Weather.Clear : [0 ,0 ,0 ,0 ,1 ,1 ,1 ,0],
            Weather.Rain  : [0 ,0 ,0 ,0 ,1 ,1 ,1 ,0],
            Weather.Snow  : [0 ,0 ,0 ,0 ,2 ,2 ,2 ,0]
        }

    def __repr__(self):
        return 'sea'

class Shoal(Terrain):
    def __init__(self):
        self.defense = 0
        self.movement = {
            Weather.Clear : [1 ,1 ,1 ,1 ,1 ,0 ,1 ,0],
            Weather.Rain  : [1 ,1 ,1 ,1 ,1 ,0 ,1 ,0],
            Weather.Snow  : [1 ,1 ,1 ,1 ,2 ,0 ,1 ,0]
        }

    def __repr__(self):
        return 'shoal'

class Reef(Terrain):
    def __init__(self):
        self.defense = 1
        self.movement = {
            Weather.Clear : [0 ,0 ,0 ,0 ,1 ,2 ,2 ,0],
            Weather.Rain  : [0 ,0 ,0 ,0 ,1 ,2 ,2 ,0],
            Weather.Snow  : [0 ,0 ,0 ,0 ,2 ,2 ,2 ,0]
        }

    def __repr__(self):
        return 'reef'

class City(Terrain):
    def __init__(self):
        self.defense = 3
        self.movement = {
            Weather.Clear : [1 ,1 ,1 ,1 ,1 ,0 ,0 ,0],
            Weather.Rain  : [1 ,1 ,1 ,1 ,1 ,0 ,0 ,0],
            Weather.Snow  : [1 ,1 ,1 ,1 ,2 ,0 ,0 ,0]
        }

    def __repr__(self):
        return 'city'

class Base(Terrain):
    def __init__(self):
        self.defense = 3
        self.movement = {
            Weather.Clear : [1 ,1 ,1 ,1 ,1 ,0 ,0 ,1],
            Weather.Rain  : [1 ,1 ,1 ,1 ,1 ,0 ,0 ,1],
            Weather.Snow  : [1 ,1 ,1 ,1 ,2 ,0 ,0 ,1]
        }

    def __repr__(self):
        return 'base'

class Airport(Terrain):
    def __init__(self):
        self.defense = 3
        self.movement = {
            Weather.Clear : [1 ,1 ,1 ,1 ,1 ,0 ,0 ,0],
            Weather.Rain  : [1 ,1 ,1 ,1 ,1 ,0 ,0 ,0],
            Weather.Snow  : [1 ,1 ,1 ,1 ,2 ,0 ,0 ,0]
        }

    def __repr__(self):
        return 'airport'

class Port(Terrain):
    def __init__(self):
        self.defense = 3
        self.movement = {
            Weather.Clear : [1 ,1 ,1 ,1 ,1 ,1 ,1 ,0],
            Weather.Rain  : [1 ,1 ,1 ,1 ,1 ,1 ,1 ,0],
            Weather.Snow  : [1 ,1 ,1 ,1 ,2 ,2 ,2 ,0]
        }

    def __repr__(self):
        return 'port'

class HQ(Terrain):
    def __init__(self):
        self.defense = 4
        self.movement = {
            Weather.Clear : [1 ,1 ,1 ,1 ,1 ,0 ,0 ,0],
            Weather.Rain  : [1 ,1 ,1 ,1 ,1 ,0 ,0 ,0],
            Weather.Snow  : [1 ,1 ,1 ,1 ,2 ,0 ,0 ,0]
        }

    def __repr__(self):
        return 'hq'

class Pipe(Terrain):
    def __init__(self):
        self.defense = 0
        self.movement = {
            Weather.Clear : [0 ,0 ,0 ,0 ,0 ,0 ,0 ,1],
            Weather.Rain  : [0 ,0 ,0 ,0 ,0 ,0 ,0 ,1],
            Weather.Snow  : [0 ,0 ,0 ,0 ,0 ,0 ,0 ,1]
        }

    def __repr__(self):
        return 'pipe'

class Pipeseam(Terrain):
    def __init__(self):
        self.defense = 0
        self.movement = {
            Weather.Clear : [0 ,0 ,0 ,0 ,0 ,0 ,0 ,1],
            Weather.Rain  : [0 ,0 ,0 ,0 ,0 ,0 ,0 ,1],
            Weather.Snow  : [0 ,0 ,0 ,0 ,0 ,0 ,0 ,1]
        }

    def __repr__(self):
        return 'pipeseam'

class Rubble(Terrain):
    def __init__(self):
        self.defense = 1
        self.movement = {
            Weather.Clear : [1 ,1 ,1 ,2 ,1 ,0 ,0 ,0],
            Weather.Rain  : [1 ,1 ,2 ,3 ,1 ,0 ,0 ,0],
            Weather.Snow  : [2 ,1 ,2 ,3 ,2 ,0 ,0 ,0]
        }

    def __repr__(self):
        return 'rubble'

class Missile(Terrain):
    def __init__(self):
        self.defense = 3
        self.movement = {
            Weather.Clear : [1 ,1 ,1 ,1 ,1 ,0 ,0 ,0],
            Weather.Rain  : [1 ,1 ,1 ,1 ,1 ,0 ,0 ,0],
            Weather.Snow  : [1 ,1 ,1 ,1 ,2 ,0 ,0 ,0]
        }

    def __repr__(self):
        return 'missile'

class Comtower(Terrain):
    def __init__(self):
        self.defense = 3
        self.movement = {
            Weather.Clear : [1 ,1 ,1 ,1 ,1 ,0 ,0 ,0],
            Weather.Rain  : [1 ,1 ,1 ,1 ,1 ,0 ,0 ,0],
            Weather.Snow  : [1 ,1 ,1 ,1 ,2 ,0 ,0 ,0]
        }

    def __repr__(self):
        return 'comtower'

class Lab(Terrain):
    def __init__(self):
        self.defense = 3
        self.movement = {
            Weather.Clear : [1 ,1 ,1 ,1 ,1 ,0 ,0 ,0],
            Weather.Rain  : [1 ,1 ,1 ,1 ,1 ,0 ,0 ,0],
            Weather.Snow  : [1 ,1 ,1 ,1 ,2 ,0 ,0 ,0]
        }

    def __repr__(self):
        return 'lab'
