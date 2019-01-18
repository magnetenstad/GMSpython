import pygame
import os
from PIL import Image, ImageSequence


def load_gif(path):
    frames = ImageSequence.Iterator(Image.open(path))
    return [pygame.image.fromstring(frame.convert("RGBA").tobytes(), frame.size, "RGBA") for frame in frames]


def load_asset(path):
    ext = os.path.splitext(path)[1]
    return {
        '.png': lambda path: [pygame.image.load(path)],
        '.wav': pygame.mixer.Sound,
        '.gif': load_gif,
    }[ext](path)


def get_assets(assets_path):
    return dict(
        (os.path.basename(filename), load_asset(os.path.join(assets_path, filename)))
        for filename in sorted(os.listdir(assets_path))
    )


def instance_place(instance, x, y, instance_list):
    rect = instance.rect.move(x - instance.rect.x, y - instance.rect.y)
    for i in instance_list:
        if rect.colliderect(i.rect):
            return i
    return False


def instance_find(list, var, val):
    return [i for i in list if hasattr(i, var) and getattr(i, var) == val]
