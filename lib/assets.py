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
