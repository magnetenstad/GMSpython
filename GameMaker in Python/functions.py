import pygame
import os
from PIL import Image, ImageSequence

def asset_load(file, path):
    if file.endswith(".png"):
        return [pygame.image.load(os.path.join(path, file))]
    if file.endswith(".wav"):
        return pygame.mixer.Sound(os.path.join(path, file))
    if file.endswith(".gif"):
        gif = ImageSequence.Iterator(Image.open(os.path.join(path, file)))
        return [pygame.image.fromstring(i.tobytes(), i.size, i.mode) for i in gif]

def get_assets(path_assets):
    asset_list = [asset_load(os.path.join(path_assets, path), path_assets) for path in sorted(os.listdir(path_assets))]
    name_list = [os.path.basename(path) for path in sorted(os.listdir(path_assets))]
    dictionary = {}
    for i in range(len(asset_list)):
        dictionary[name_list[i]] = asset_list[i]
    return dictionary
