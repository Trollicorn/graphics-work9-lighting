from matrix import *
from functools import map
  # IMPORANT NOTE

  # Ambient light is represented by a color value

  # Point light sources are 2D arrays of doubles.
  #      - The fist index (LOCATION) represents the vector to the light.
  #      - The second index (COLOR) represents the color.

  # Reflection constants (ka, kd, ks) are represened as arrays of
  # doubles (red, green, blue)

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4


#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    return limit_color(calculate_ambient(ambient,areflect) +
                       calculate_diffuse(light,dreflect,normal) +
                       calculate_specular(light,sreflect,view,normal))

def calculate_ambient(alight, areflect):


def calculate_diffuse(light, dreflect, normal):
    pass

def calculate_specular(light, sreflect, view, normal):
    pass

def limit_color(color):
    for c in range(len(color)):
        color[c] = 
