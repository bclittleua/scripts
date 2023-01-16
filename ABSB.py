#!/bin/python
#               .__                       .__                        .__           ____
#    ____  ____ |  |   ____   ____   ____ |  |   ___________    ____ |__| ____    /  _ \
#  _/ ___\/  _ \|  |  /  _ \ /    \_/ __ \|  |   \____ \__  \  /    \|  |/ ___\   >  _ </\
#  \  \__(  <_> )  |_(  <_> )   |  \  ___/|  |__ |  |_> > __ \|   |  \  \  \___  /  <_\ \/
#   \___  >____/|____/\____/|___|  /\___  >____/ |   __(____  /___|  /__|\___  > \_____\ \
#       \/                       \/     \/       |__|       \/     \/        \/         \/
#  __  .__             ___.   .__                          .__                         .___
#_/  |_|  |__   ____   \_ |__ |  |  __ __   ____   __  _  _|__|____________ _______  __| _/______
#\   __\  |  \_/ __ \   | __ \|  | |  |  \_/ __ \  \ \/ \/ /  \___   /\__  \\_  __ \/ __ |/  ___/
# |  | |   Y  \  ___/   | \_\ \  |_|  |  /\  ___/   \     /|  |/    /  / __ \|  | \/ /_/ |\___ \
# |__| |___|  /\___  >  |___  /____/____/  \___  >   \/\_/ |__/_____ \(____  /__|  \____ /____  >
#           \/     \/       \/                 \/                   \/     \/           \/    \/
# COLONEL PANIC & THE BLUE WIZARDS: Arcade Button Sound Board v0.1
# non-default dependencies: evdev
# RPi MUST add the following to /boot/cmdline.txt for DragonRise USB encoders: usbhid.quirks=0x0079:0x0006:0x00000400

from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame, time
from evdev import InputDevice, categorize, ecodes, KeyEvent
pygame.mixer.pre_init(frequency=44100)

gamepad = InputDevice('/dev/input/event0')

tr_status = 0
br_status = 0
ty_status = 0
by_status = 0
tg_status = 0
bg_status = 0
tb_status = 0
bb_status = 0
p1_status = 0
p2_status = 0

print ('COLONEL PANIC & THE BLUE WIZARDS\nArcade Sound Board v0.1')
time.sleep(1)
print ('Listening...')

def reset_all():
    global tr_status, br_status, ty_status, by_status, tg_status, bg_status, tb_status, bb_status, p1_status, p2_status
    tr_status = 0
    br_status = 0
    ty_status = 0
    by_status = 0
    tg_status = 0
    bg_status = 0
    tb_status = 0
    bb_status = 0
    p1_status = 0
    p2_status = 0

# scancodes 288-299
def t_red():
    global tr_status
    chan = 1
    title = 'BGFX Paint the Town'
    path = '/home/pi/bin/sounds/paint_the_town_bgfx.wav'
    if tr_status == 0:
        print ('Starting Channel {0}: {1}'.format(chan, title))
        pygame.mixer.init()
        pygame.mixer.set_num_channels(16)
        sound = pygame.mixer.Sound(path)
        pygame.mixer.Channel(chan).play(sound)
        tr_status = 1
    elif tr_status == 1:
        print ('Killing Channel {0}'.format(chan))
        pygame.mixer.Channel(chan).stop()
        tr_status = 0

def b_red():
    global br_status
    chan = 2
    title = 'void'
    path = '/path/to/sound.wav'
    if br_status == 0:
        print ('Starting Channel {0}: {1}'.format(chan, title))
        pygame.mixer.init()
        pygame.mixer.set_num_channels(16)
        sound = pygame.mixer.Sound(path)
        pygame.mixer.Channel(chan).play(sound)
        br_status = 1
    if br_status == 1:
        print ('Killing Channel {0}'.format(chan))
        pygame.mixer.Channel(chan).stop()
        br_status = 0

def t_yellow():
    global ty_status
    chan = 3
    title = 'wake BGFX'
    path = '/home/pi/bin/sounds/wake_bgfx.wav'
    if ty_status == 0:
        print ('Starting Channel {0}: {1}'.format(chan, title))
        pygame.mixer.init()
        pygame.mixer.set_num_channels(16)
        sound = pygame.mixer.Sound(path)
        pygame.mixer.Channel(chan).play(sound)
        ty_status = 1
    elif ty_status == 1:
        print ('Killing Channel {0}'.format(chan))
        pygame.mixer.Channel(chan).stop()
        ty_status = 0

def b_yellow():
    global by_status
    chan = 4
    title = 'Wake the Dead full wav'
    path = '/home/pi/bin/sounds/wake_the_dead_full.wav'
    if by_status == 0:
        print ('Starting Channel {0}: {1}'.format(chan, title))
        pygame.mixer.init()
        pygame.mixer.set_num_channels(16)
        sound = pygame.mixer.Sound(path)
        pygame.mixer.Channel(chan).play(sound)
        by_status = 1
    elif by_status == 1:
        print ('Killing Channel {0}'.format(chan))
        pygame.mixer.Channel(chan).stop()
        by_status = 0

def t_green():
    global tg_status
    chan = 5
    title = 'AIR RAID!'
    path = '/home/pi/bin/sounds/air_raid.wav'
    if tg_status == 0:
        print ('Starting Channel {0}: {1}'.format(chan, title))
        pygame.mixer.init()
        pygame.mixer.set_num_channels(16)
        sound = pygame.mixer.Sound(path)
        pygame.mixer.Channel(chan).play(sound)
        tg_status = 1
    elif tg_status == 1:
        print ('Killing Channel {0}'.format(chan))
        pygame.mixer.Channel(chan).stop()
        tg_status = 0

def b_green():
    global bg_status
    chan = 6
    title = 'void'
    path = '/path.wav'
    if bg_status == 0:
        print ('Starting Channel {0}: {1}'.format(chan, title))
        pygame.mixer.init()
        pygame.mixer.set_num_channels(16)
        sound = pygame.mixer.Sound(path)
        pygame.mixer.Channel(chan).play(sound)
        bg_status = 1
    elif bg_status == 1:
        print ('Killing Channel {0}'.format(chan))
        pygame.mixer.Channel(chan).stop()
        bg_status = 0

def t_blue():
    global tb_status
    chan = 7
    title = 'BGFX Dark Army pt1'
    path = '/home/pi/bin/sounds/blackwolf_pt1_bgfx.wav'
    if tb_status == 0:
        print ('Starting Channel {0}: {1}'.format(chan, title))
        pygame.mixer.init()
        pygame.mixer.set_num_channels(16)
        sound = pygame.mixer.Sound(path)
        pygame.mixer.Channel(chan).play(sound)
        tb_status = 1
    elif tb_status == 1:
        print ('Killing Channel {0}'.format(chan))
        pygame.mixer.Channel(chan).stop()
        tb_status = 0

def b_blue():
    global bb_status
    chan = 8
    title = 'Dark Army pt1'
    path = '/home/pi/bin/sounds/dark_army_pt1_full.wav'
    if bb_status == 0:
        print ('Starting Channel {0}: {1}'.format(chan, title))
        pygame.mixer.init()
        pygame.mixer.set_num_channels(16)
        sound = pygame.mixer.Sound(path)
        pygame.mixer.Channel(chan).play(sound)
        bb_status = 1
    elif bb_status == 1:
        print ('Killing Channel {0}'.format(chan))
        pygame.mixer.Channel(chan).stop()
        bb_status = 0

def player1():
    global p1_status
    print ('Button 10: fetching current parameters...')
    print (pygame.mixer.get_init())
    print (pygame.mixer.get_busy())

def player2():
    global p2_status
    if pygame.mixer.get_init() is not None:
        print ('Button 11: Fading out all channels in 5 seconds...')
        print ('(pressing a button now will fuck shit up!)')
        pygame.mixer.fadeout(5000) #this is in miliseconds
        time.sleep(5) #this is in seconds, just how the two libs work...
        pygame.mixer.quit()
        reset_all()
        print ('...done.')
    else:
        print ('Button 11: mixer not initialized')

#meanwhile, in the for loop...
for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        keyevent = categorize(event)
        if keyevent.keystate == KeyEvent.key_down:
            if keyevent.scancode == 288: #T-RED
                t_red()
            elif keyevent.scancode == 289: #B-RED
                b_red()
            elif keyevent.scancode == 290: #T-YELLOW
                t_yellow()
            elif keyevent.scancode == 291: #B-YELLOW
                b_yellow()
            elif keyevent.scancode == 292: #T-GREEN
                t_green()
            elif keyevent.scancode == 293: #B-GREEN
                b_green()
            elif keyevent.scancode == 294: #T-BLUE
                t_blue()
            elif keyevent.scancode == 295: #B-BLUE
                b_blue()
            #elif keyevent.scancode == 296: #not connected... yet
            #elif keyevent.scancode == 297: #not connected... yet
            elif keyevent.scancode == 298: #PLAYER1
                player1()
            elif keyevent.scancode == 299: #PLAYER2
                player2()
