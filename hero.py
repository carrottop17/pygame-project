import pygame

class Hero(object):
	def __init__(self, screen):
		self.screen = screen #give the hero the ability to control the screen

		# Load the hero image, get its rect
		self.image = pygame.image.load('images/hero.png')
		self.rect = self.image.get_rect() #pygame makes gives us get_rect on any object so we can get
		self.screen_rect = screen.get_rect() # assign a var so the hero class knows how big

		self.rect.centerx = self.screen_rect.centerx #this will put the middle of the hero at the middle of the screen
		self.rect.bottom = self.screen_rect.bottom #this will put our hero "bottom" at the bottom of the screen
		#not self.rect.centery because we want the bottom on bottom, not the center

	def draw_me(self):
		self.screen.blit(self.image, self.rect)#draw the surface, the image, the where