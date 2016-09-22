import pygame #the game
from hero import Hero #bring in the hero class with all its methods
from monster import Monster
from settings import Settings
import game_functions as gf
from pygame.sprite import Group


#set up the main core function
def run_game():
	pygame.init() #initialize all the pygame modules
	game_settings = Settings()#create an instance of settings class
	screen = pygame.display.set_mode(game_settings.screen_size) # set the screen size with set_mode
	pygame.display.set_caption("Monster Attack") #set the message on the status bar
	hero = Hero(screen) #set a variable equal to the class and pass it the screen
	monster = Monster(screen, game_settings)
	bullets = Group() #set the bullets to group

	while 1: #runt this loop forever
		gf.check_events(hero, bullets, game_settings, screen, monster) #call gf (aliased from game_functions module) and get the check_events method
		hero.update() #update the hero flags
		monster.update()
		bullets.update() #call the update method in the while loop
		gf.update_screen(game_settings, screen, hero, bullets, monster) # call the update_screen method which updates updating the screen
		for bullet in bullets: #get rid of bullets that are off the screen
			if bullet.rect.bottom <= 0: #bullet bottom is at the top of the screen
				bullets.remove(bullet)
				

run_game() #start the game
