import pygame
import os
from PIL import Image, ImageSequence

def asset_load(file, path):
    if file.endswith(".png"):
        return [pygame.image.load(os.path.join(path, file))]
    if file.endswith(".wav"):
        return pygame.mixer.Sound(os.path.join(path, file))
    if file.endswith(".gif"):
        return [pygame.image.fromstring(i.convert("RGBA").tobytes(), i.size, "RGBA") for i in ImageSequence.Iterator(Image.open(os.path.join(path, file)))]

def get_assets(path_assets):
    asset_list = [asset_load(os.path.join(path_assets, path), path_assets) for path in sorted(os.listdir(path_assets))]
    name_list = [os.path.basename(path) for path in sorted(os.listdir(path_assets))]
    dictionary = {}
    for i in range(len(asset_list)):
        dictionary[name_list[i]] = asset_list[i]
    return dictionary

def instance_place(instance, x, y, instance_list):
    rect = instance.rect.move(x - instance.rect.x, y - instance.rect.y)
    for i in instance_list:
        if rect.colliderect(i.rect):
            return i
    return False

def instance_find(list, var, val):
    return [i for i in list if hasattr(i, var) and getattr(i, var) == val]
