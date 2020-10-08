from lib.game import game

def instance_find_tag(tag):
    return [i for i in game.object_list if tag in i.tags]

def instance_place(instance, x, y, instance_list):
    rect = instance.rect.move(x - instance.rect.x, y - instance.rect.y)
    for i in instance_list:
        if rect.colliderect(i.rect):
            return i
    return False

def instance_find(list, var, val):
    return [i for i in list if hasattr(i, var) and getattr(i, var) == val]
