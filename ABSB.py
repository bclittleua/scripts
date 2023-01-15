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

gamepad = InputDevice('/dev/input/event0')
pygame.mixer.pre_init(frequency=44100, channels=2)

print ('COLONEL PANIC & THE BLUE WIZARDS\nArcade Sound Board v0.1')
time.sleep(2)
print ('Listening...')

for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        keyevent = categorize(event)
        if keyevent.keystate == KeyEvent.key_down:
            if keyevent.scancode == 288:
                print('Button 00: Bruteforce air_raid.wav')
                pygame.mixer.init()
                sound = pygame.mixer.Sound('/home/pi/bin/sounds/air_raid.wav')
                sound.play()
            elif keyevent.scancode == 289:
                print ('Button 01: Paint the Town Red BGFX')
                pygame.mixer.init()
                sound = pygame.mixer.Sound('/home/pi/bin/sounds/paint_the_town_bgfx.wav')
                sound.play()
            elif keyevent.scancode == 290:
                print ("Button 02: Blackwolf's Dark Army pt. 1 BGFX")
                pygame.mixer.init()
                sound = pygame.mixer.Sound('/home/pi/bin/sounds/blackwolf_pt1_bgfx.wav')
                sound.play()
            elif keyevent.scancode == 291:
                print ('Button 03: unassigned')
            elif keyevent.scancode == 292:
                print ('Button 04: unassigned')
            elif keyevent.scancode == 293:
                print ('Button 05: unassigned')
            elif keyevent.scancode == 294:
                print ('Button 06: unassigned')
            elif keyevent.scancode == 295:
                print ('Button 07: unassigned')
            elif keyevent.scancode == 296:
                print ('Button 08: unassigned')
            elif keyevent.scancode == 297:
                print ('Button 09: unassigned')
            elif keyevent.scancode == 298:
                print ('Button 10: fetching current parameters...')
                print (pygame.mixer.get_init())
            elif keyevent.scancode == 299: # RED Button
                if pygame.mixer.get_init() is not None:
                    print ('Button 11: Fading out all channels in 5 seconds...')
                    print ('(pressing a button now will fuck shit up!)')
                    pygame.mixer.fadeout(5000)
                    time.sleep(5)
                    pygame.mixer.quit()
                    print ('...done.')
                else:
                    print ('Button 11: mixer not initialized')
