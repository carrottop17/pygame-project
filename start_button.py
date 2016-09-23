import pygame.font

class Play_button(object):
	def __init__(self, screen, button_text):
		self.screen = screen
		self.screen_rect = screen.get_rect()

		#set the width of the button image
		self.width = 250
		self.height = 100
		self.button_color = 0,200,150
		self.text_color = 255,255,255
		self.font = pygame.font.Font(None, 52)
		# Set the rect of the button
		self.rect = pygame.Rect(0,0,self.width, self.height)
		#set the location of the button.  The location will be the center of the screen
		self.rect.center = self.screen_rect.center
		self.setup_message(button_text)

	def setup_message(self, button_text):
		# render the image inside of image_message. button is being turned into an image
		self.image_message = self.font.render(button_text, True, self.text_color)
		self.image_message_rect = self.image_message.get_rect()
		self.image_message_rect.center = self.rect.center


	def draw_button(self):
		# actually load up the image text so that its ready to draw
		self.screen.fill(self.button_color, self.rect)
		# actually draw it
		self.screen.blit(self.image_message, self.image_message_rect)
