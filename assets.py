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

anims = {}
def loadAnim(directory, start, end):
    key = directory + str(start) + ".." + str(end)

    if key not in anims:
        frames = []
        for i in range(start,end):
            filename = str(i).zfill(4) + ".png"
            filepath = directory + "/" + filename
            frames.append(loadImage(filepath))

        anims[key] = frames
        return frames
    else:
        return anims[key]
