from lib.game import game

def instance_find_tag(tag):
	return [i for i in game.objects if tag in i.tags]

def instance_place(instance, x, y, instance_list):
	rect = instance.rect.move(x - instance.rect.x, y - instance.rect.y)
	for i in instance_list:
		if rect.colliderect(i.rect):
			return i
	return False

def instance_place_list(instance, x, y, instance_list):
	collisions = []
	rect = instance.rect.move(x - instance.rect.x, y - instance.rect.y)
	for i in instance_list:
		if rect.colliderect(i.rect):
			collisions.append(i)
	return collisions

def instance_find(list, var, val):
	return [i for i in list if hasattr(i, var) and getattr(i, var) == val]

def rect_from_sprite(instance, sprite_index):
	return game.application_surface.blit(game.assets[sprite_index][0], (instance.rect.x, instance.rect.y))

def draw_text(string, x, y):
	game.application_surface.blit(game.font.render(string, False, (255, 255, 255)),
									(x - game.camera.x, y - game.camera.y))

def draw_sprite(sprite_index, image_index, x, y):
	game.application_surface.blit(game.assets[sprite_index][int(image_index)],
									(x - game.camera.x, y - game.camera.y))

def draw_instance(instance):
	draw_sprite(instance.sprite_index,
						instance.image_index, instance.rect.x, instance.rect.y)

def draw_text_gui(string, x, y):
	game.application_surface.blit(game.font.render(
		string, False, (255, 255, 255)), (x, y))

def keyboard_check(key):
	return key in game.input.key
	
def keyboard_check_pressed(key):
	return key in game.input.key_pressed

def keyboard_check_released(key):
	return key in game.input.key_released
