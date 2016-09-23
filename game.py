import pygame #the game
from hero import Hero #bring in the hero class with all its methods
from monster import Monster
from settings import Settings
import game_functions as gf
from pygame.sprite import Group, groupcollide
from start_button import Play_button



#set up the main core function
def run_game():
	pygame.init() #initialize all the pygame modules
	game_settings = Settings()#create an instance of settings class
	screen = pygame.display.set_mode(game_settings.screen_size) # set the screen size with set_mode
	pygame.display.set_caption("Monster Attack") #set the message on the status bar
	play_button = Play_button(screen, 'Press Play')

	pygame.mixer.music.load('sounds/music.wav')
	pygame.mixer.music.play(-1)
	hero = Hero(screen) #set a variable equal to the class and pass it the screen
	monster = Monster(screen, game_settings)
	bullets = Group() #set the bullets to group

	while 1: #run this loop forever
		gf.check_events(hero, bullets, game_settings, screen, monster, play_button) #call gf (aliased from game_functions module) and get the check_events method
		gf.update_screen(game_settings, screen, hero, bullets, monster, play_button) # call the update_screen method which updates updating the screen
		if game_settings.game_active:
			hero.update() #update the hero flags
			monster.update()
			bullets.update() #call the update method in the while loop
			# the Dict = groupcollide(enemies, bullets, True, True)
			# if(theDict):
			# 	print "you hit the monster. play some type of music"
			for bullet in bullets: #get rid of bullets that are off the screen
				if bullet.rect.bottom <= 0: #bullet bottom is at the top of the screen
					bullets.remove(bullet)
				if bullet.rect.top == monster.rect.bottom:
					bullets.remove(bullet)
					monster.speed = -2


run_game() #start the game
