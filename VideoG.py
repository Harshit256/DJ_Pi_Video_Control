#!/usr/bin/python3

'''
Headphone Video Control
'''

from video_player import * #make sure video_player.py file is also on the same folder
from gpiozero import Button
from time import sleep
import pygame
import sys

pygame.init()
infoObject = pygame.display.Info()
screen=pygame.display.set_mode((infoObject.current_w, infoObject.current_h),pygame.NOFRAME)


pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 50)

'''
BASE_DIR = '/home/pi/Desktop/pi_video_control_test'
FILENAME =  'test2.mp4'

BASE_DIR_NOT = '/home/pi/Desktop/pi_video_control_test'
FILENAME_NOT =  'test1.mp4'''

BASE_DIR = '/home/pi/pi_video_control/'
FILENAME_PRESSED =  'test2.mp4'
BASE_DIR_NOT = '/home/pi/pi_video_control'
FILENAME_NOT_PRESSED =  'test1.mp4'

image_path='/home/pi/pi_video_control/bck.jpg'

play_path_audio_is_pressed = ''.join([BASE_DIR, FILENAME_PRESSED])
play_path_audio_is_not_pressed = ''.join([BASE_DIR_NOT, FILENAME_NOT_PRESSED])

headphone_switch = 3
turnoff_switch = 2
exit_switch = 13
is_playing = False
first_time = True
is_not_playing = False

headphone_button = Button(headphone_switch)
turnoff_button = Button(turnoff_switch)
exit_button = Button(exit_switch)
play = Player(play_path_audio_is_pressed)
play_not = Player(play_path_audio_is_not_pressed)

def load_image():
	screen.fill((255,255,255))
	picture=pygame.image.load(image_path)
	screen.blit(picture,(0,0))
	pygame.display.update()
def display_text(text):
	screen.fill((255,255,255))
	picture=pygame.image.load(image_path)
	screen.blit(picture,(0,0))
	textsurface = myfont.render(text, False, (255, 255, 255))
	text_rect = textsurface.get_rect(center=(infoObject.current_w/2, 9*infoObject.current_h/10))
	screen.blit(textsurface,text_rect)
	pygame.display.update()
	
def exit_program():
	headphone_button.close()
	turnoff_button.close()
	exit_button.close()
	if play.status() == 'playing':
		print('Audio is running, terminating now!')
		play.kill()
	elif play_not.status() == 'playing':
                print('Audio is running, terminating now!')
                play_not.kill()
	else:
		print('no Audio running, exiting now')
	pygame.quit()	
def shutdown():
	os.system("sudo shutdown -h now")
	#text-shutting down
	display_text("shutting down..")
	exit_program()
	
#load image first here
#load_image()
try:
	while True:
		if exit_button.is_pressed:
			exit_program()
		elif turnoff_button.is_pressed:
			shutdown()
		else:
			if is_playing == False and not headphone_button.is_pressed:
				print("Button Lifted")
				if first_time:
					print('headphone lifted, starting Audio')
					display_text("Audio will Start in few seconds..")
					first_time=False
				else:
					print('Audio will Restart in few seconds..')
					#text saying Audio will Restart
					display_text("Audio will Restart in few seconds..")
				#sleep(1)
				play.play()
				is_playing = True
				display_text("Playing Audio")
				if is_not_playing:
                                        play_not.stop()
                                #play.play()
                                #display_text("Playing Audio")
			elif headphone_button.is_pressed and is_not_playing == False:
                                print("Button Pressed")
                                first_time=True
                                if is_playing:
                                        play.stop()        
                                is_playing=False
                                play_not.play()
                                is_not_playing=True
                                print('Headphone in place')
				#text-Lift the Headphone to Activate Sound
                                display_text("Lift the Headphone to Activate Sound")
			elif is_playing == True:
				if play.status() == 'done':
					print(''.join(['done', '\n']))
					is_playing = False
			elif is_not_playing == True:
				if play_not.status() == 'done':
					print(''.join(['done', '\n']))
					is_not_playing = False

except KeyboardInterrupt:
	print(''.join([ '\n', '\n', 'INTERRUPTED', '\n']))
	headphone_button.close()
	turnoff_button.close()
	exit_button.close()
	if play.status() == 'playing':
		print('Audio is running, terminating now!')
		play.kill()
	else:
		print('no Audio running, exiting now')
	pygame.quit()
	
	pi_