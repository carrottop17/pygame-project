#we will put all main game functions here
import sys
import pygame
from bullets import Bullet # we don't care about the update or draw functions

def check_events(hero, bullets, game_settings, screen):
	for event in pygame.event.get(): #run through all pygame events
		if event.type == pygame.QUIT: #if the event is the quit event then quit
			sys.exit() #quit
		elif event.type == pygame.KEYDOWN: #the user pushed a key and its down
			if event.key == pygame.K_RIGHT: # the user pressed right
				hero.moving_right = True #set the flag
			elif event.key == pygame.K_LEFT:
				hero.moving_left = True #set the flag
			# elif event.key == pygame.K_UP:
			# 	hero.moving_up = True #set the flag
			# elif event.key == pygame.K_DOWN:
			# 	hero.moving_down = True #set the flag
			elif event.key == pygame.K_SPACE: #user pushed the space bar
				new_bullet = Bullet(screen, hero, game_settings)
				bullets.add(new_bullet)
		elif event.type == pygame.KEYUP: #the user let go of the key
			if event.key == pygame.K_RIGHT:
				hero.moving_right = False
			elif event.key == pygame.K_LEFT:
				hero.moving_left = False
			elif event.key == pygame.K_UP:
				hero.moving_up = False
			elif event.key == pygame.K_DOWN:
				hero.moving_down = False


#handle all the screen updates
def update_screen(settings, screen, hero, bullets):
	screen.fill(settings.bg_color)#fill the background with our green
	hero.draw_me() #call the draw method and put the hero on the screen
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	pygame.display.flip()