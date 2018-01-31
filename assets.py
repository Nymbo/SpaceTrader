import pygame
import json

images = {}

def loadImage(path):
    global images
    if path not in images:
        images[path] = pygame.image.load(path).convert_alpha()
        return images[path]
    else:
        return images[path]

def loadJSON(path):
    f = open(path)
    data = json.load(f)
    return data
