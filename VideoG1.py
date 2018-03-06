#!/usr/bin/python3

'''
Headphone Video Control
'''

from video_player import * #make sure video_player.py file is also on the same folder
from gpiozero import Button
from time import sleep
import pygame
import sys
import time

pygame.init()
pygame.mouse.set_visible(False)
infoObject = pygame.display.Info()
screen=pygame.display.set_mode((infoObject.current_w, infoObject.current_h),pygame.NOFRAME)

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 50)

'''
BASE_DIR = '/home/pi/Desktop/pi_video_control_test'
FILENAME =  'HD.mp4'
BASE_DIR_NOT_PRESSED = '/home/pi/Desktop/pi_video_control_test'
FILENAME_NOT =  'DJI.mp4'
'''
BASE_DIR = '/home/pi/Desktop/pi_video_control_test/'
FILENAME_PRESSED =  'Video Portrait_5secs_Pressed.mp4'
BASE_DIR_NOT_PRESSED = '/home/pi/Desktop/pi_video_control_test/'
FILENAME_NOT_PRESSED =  'Video Portrait_30sec_Lifted.mp4'

image_path='/home/pi/pi_video_control/bck.jpg'
lifted_transition_image='/home/pi/Desktop/pi_video_control_test/Transition.jpg'
pressed_transition_image='/home/pi/Desktop/pi_video_control_test/Transition_done.jpg'

play_path_video_is_pressed = ''.join([BASE_DIR, FILENAME_PRESSED])
play_path_video_is_lifted = ''.join([BASE_DIR_NOT_PRESSED, FILENAME_NOT_PRESSED])

headphone_switch = 3
turnoff_switch = 2
exit_switch = 13
is_lifted_playing = False
first_time = True
is_pressed_playing = False

headphone_button = Button(headphone_switch)
turnoff_button = Button(turnoff_switch)
exit_button = Button(exit_switch)
play_pressed = Player(play_path_video_is_pressed)
play_lifted = Player(play_path_video_is_lifted)

pressed_transition = Player(pressed_transition_image)
lifted_transition = Player(lifted_transition_image)
      
def pressed_load_image():
	screen.fill((255,255,255))
	#screen.get_rect(center=(infoObject.current_w/2, 9*infoObject.current_h/10))
	picture=pygame.image.load(pressed_transition_image).convert()
	clock = pygame.time.Clock()
	#screen.blit(picture,(0,0))
	#pygame.display.update()
	for i in range(0,255,5):
            screen.fill((0,0,0))
            picture.set_alpha(255-i)
            screen.blit(picture, (0,0))
            pygame.display.flip()
            clock.tick(50)
                
def lifted_load_image():
	screen.fill((255,255,255))
	#screen.get_rect(center=(infoObject.current_w/2, 9*infoObject.current_h/10))
	picture=pygame.image.load(lifted_transition_image).convert()
	clock = pygame.time.Clock()
	#screen.blit(picture,(0,0))
	#pygame.display.update()
	for i in range(0,255,5):
            screen.fill((0,0,0))
            picture.set_alpha(i)
            screen.blit(picture, (0,0))
            pygame.display.flip()
            clock.tick(50)
            
def display_text(text):
	screen.fill((255,255,255))
	picture=pygame.image.load(transition_image)
	screen.blit(picture,(0,0))
	textsurface = myfont.render(text, False, (255, 255, 255))
	text_rect = textsurface.get_rect(center=(infoObject.current_w/2, 9*infoObject.current_h/10))
	screen.blit(textsurface,text_rect)
	pygame.display.update()
	
def exit_program():
	headphone_button.close()
	turnoff_button.close()
	exit_button.close()
	if play_pressed.status() == 'playing':
		print('Audio is running, terminating now!')
		play_pressed.kill()
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
                if not headphone_button.is_pressed:
                        if is_pressed_playing:
                                if play_pressed.status() == 'playing':
                                    play_pressed.stop()
                                    lifted_load_image()
                                    #sleep(5)
                                is_pressed_playing = False
                                
                        if is_lifted_playing == False:
                            print("Button Lifted")
                            #if first_time:
                            #print('headphone lifted, starting Video')
                            #display_text("Video will Start in few seconds..")
                            #first_time=False
                        #else:
                            #print('Audio will Restart in few seconds..')
                            #text saying Audio will Restart
                            #display_text("Audio will Restart in few seconds..")
                            #sleep(3)
                            #play.play()
                            #display_text("Playing Video")
                            #display_text(" ")
                            play_lifted.play()
                            is_lifted_playing=True
                elif headphone_button.is_pressed:
                        if is_lifted_playing:
                                if play_lifted.status() == 'playing':
                                    play_lifted.stop()
                                    pressed_load_image()
                                    #sleep(5)
                                is_lifted_playing=False
                                
                        if is_pressed_playing == False:
                            print("Button Pressed")
                            #first_time=True
                            play_pressed.play()
                            is_pressed_playing = True
                            
                            #print('Headphone in place')
                            #text-Lift the Headphone to Activate Sound
                            #display_text("Lift the Headphone to Activate Sound")
                '''elif is_lifted_playing == True:
                        if play_lifted.status() == 'done':
                                print(''.join(['done', '\n', '\n']))
                                is_lifted_playing = False
                elif is_pressed_playing == True:
                        if play_pressed.status() == 'done':
                                print(''.join(['done', '\n', '\n']))
                                is_pressed_playing = False'''
                
except KeyboardInterrupt:
	print(''.join([ '\n', '\n', 'INTERRUPTED', '\n']))
	if play_pressed.status() == 'playing':
		print('play_lifted Video is running, terminating now!')
		play_pressed.stop()
		#load_image().stop()
		#play_pressed.kill()
	elif play_lifted.status() == 'playing':
                print('play_lifted Video is running, terminating now!')
                play_lifted.stop()
                #load_image().stop()
	else:
		print('no Video running, exiting now')
	
	headphone_button.close()
	turnoff_button.close()
	exit_button.close()
	
	pygame.quit()
	
	pi_