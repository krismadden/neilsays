#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#raspberry pi turn on led https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins
#text converter https://www.dcode.fr/multitap-abc-cipher 

import pygame, sys, time, math
from pygame.locals import *
import os
import RPi.GPIO as GPIO
import pickle

from pygame_functions import *




#LED setup
GPIO.setmode(GPIO.BCM) #sets to pin number position
GPIO.setwarnings(False)


GPIO.setup(21,GPIO.OUT) # #
GPIO.setup(20,GPIO.OUT) # 0
GPIO.setup(16,GPIO.OUT) # *
GPIO.setup(12,GPIO.OUT) # 9
GPIO.setup(7,GPIO.OUT) # 8
GPIO.setup(8,GPIO.OUT) # 7
GPIO.setup(25,GPIO.OUT) # 6
GPIO.setup(24,GPIO.OUT) # 5
GPIO.setup(23,GPIO.OUT) # 4
GPIO.setup(18,GPIO.OUT) # 3
GPIO.setup(15,GPIO.OUT) # 2
GPIO.setup(14,GPIO.OUT) # 1

def allOff():
    pass
    GPIO.output(21,GPIO.LOW) # #
    GPIO.output(20,GPIO.LOW) # 0
    GPIO.output(16,GPIO.LOW) # *
    GPIO.output(12,GPIO.LOW) # 9
    GPIO.output(7,GPIO.LOW) # 8
    GPIO.output(8,GPIO.LOW) # 7
    GPIO.output(25,GPIO.LOW) # 6
    GPIO.output(24,GPIO.LOW) # 5
    GPIO.output(23,GPIO.LOW) # 4
    GPIO.output(18,GPIO.LOW) # 3
    GPIO.output(15,GPIO.LOW) # 2
    GPIO.output(14,GPIO.LOW) # 1
    print("allOff()")

def allOn():
    print("allOn()")
    GPIO.output(21,GPIO.HIGH) # #
    GPIO.output(20,GPIO.HIGH) # 0
    GPIO.output(16,GPIO.HIGH) # *
    GPIO.output(12,GPIO.HIGH) # 9
    GPIO.output(7,GPIO.HIGH) # 8
    GPIO.output(8,GPIO.HIGH) # 7
    GPIO.output(25,GPIO.HIGH) # 6
    GPIO.output(24,GPIO.HIGH) # 5
    GPIO.output(23,GPIO.HIGH) # 4
    GPIO.output(18,GPIO.HIGH) # 3
    GPIO.output(15,GPIO.HIGH) # 2
    GPIO.output(14,GPIO.HIGH) # 1

allOff()

class Director:

    def __init__(self):
        self.sceneActive = "menu"
        self.level = 1
        self.menu = Menu(self)


        #self.screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode((1280, 1000), pygame.FULLSCREEN)
        pygame.display.set_caption("Neil Says")
        self.quit_flag = False
        self.clock = pygame.time.Clock()
        pygame.mouse.set_visible(0)
        self.input = ""

        self.start_time = time.clock()

        self.enterName = ""
        self.tempLetter = ""

        self.cursor_switch_ms = 4000 
        self.cursor_ms_counter = 0
        self.setCharacter = False
        self.keyActive = ""

        self.scores = []
        self.highScores = 'highScores.dat'
        self.add = 0
        self.scoresLength = 0
        self.recentScore = []

        #music # init is in main loop at bottom of code

        pygame.mixer.music.load(os.path.join("music", "8bit_shakeitoff.ogg"))
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        self.button_sound = pygame.mixer.Sound(os.path.join("music", "button_press.wav"))
        self.button_error = pygame.mixer.Sound(os.path.join("music", "error.wav"))



    def loop(self):
        "Main game loop."
 
        while not self.quit_flag:
            #time = self.clock.tick(30) #i put this at the end of the function
 
            # Exit events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    #pygame.mixer.Sound.play(self.button_sound)
                    print(self.input)
                    if event.key == pygame.K_ESCAPE:
                        self.quit()
                    if event.key == K_q:
                        self.leadLevel = LoadLevel(self)
                        self.change_scene(self.leadLevel)
                        print("hi mom")
                    if event.key == K_UP: #1 - arrow up
                        if self.sceneActive == "menu":
                            pygame.mixer.Sound.play(self.button_sound)
                            if self.menu.menuButtonActive == "play":
                                self.menu.menuButtonActive = "about"
                            elif self.menu.menuButtonActive == "rules":
                                self.menu.menuButtonActive = "play"
                            elif self.menu.menuButtonActive == "high":
                                self.menu.menuButtonActive = "rules"
                            elif self.menu.menuButtonActive == "about":
                                self.menu.menuButtonActive = "high"
                        elif self.sceneActive =="GamePlay":
                            pygame.mixer.Sound.play(self.button_sound)
                            print("1")
                            self.input = self.input + "1"
                        elif self.sceneActive == "Name":
                            pygame.mixer.Sound.play(self.button_sound)
                            if self.keyActive != "1":
                                self.setCharacter = True
                            if self.enterName == "":
                                pass
                            else:
                                # first time you run this, "high_scores.dat" won't exist
                                #   so we need to check for its existence before we load 
                                #   our "database"
                                if os.path.exists(self.highScores):
                                    # "with" statements are very handy for opening files. 
                                    with open(self.highScores,'rb') as rfp: 
                                        self.scores = pickle.load(rfp)
                                    # Notice that there's no "rfp.close()"
                                    #   ... the "with" clause calls close() automatically! 

                                self.high_scores = [self.level - 1, self.enterName]
                                self.recentScore = [self.level - 1, self.enterName]
                                self.scores.append(self.high_scores)
                                # Now we "sync" our database
                                with open(self.highScores,'wb') as wfp:
                                    pickle.dump(self.scores, wfp)

                                self.high = High(self)
                                self.change_scene(self.high)

                    if event.key == K_DOWN: #2 - arrow down
                        if self.sceneActive == "menu":
                            pygame.mixer.Sound.play(self.button_sound)
                            if self.menu.menuButtonActive == "play":
                                self.leadLevel = LoadLevel(self)
                                self.change_scene(self.leadLevel)
                            elif self.menu.menuButtonActive == "rules":
                                self.rules = Rules(self)
                                self.change_scene(self.rules)
                            elif self.menu.menuButtonActive == "high":
                                self.high_menu = High_Menu(self)
                                self.change_scene(self.high_menu)
                            elif self.menu.menuButtonActive == "about":
                                self.about = About(self)
                                self.change_scene(self.about)
                        elif self.sceneActive =="GamePlay":
                            pygame.mixer.Sound.play(self.button_sound)
                            print("2")
                            self.input = self.input + "2"
                        elif self.sceneActive == "Name":
                            pygame.mixer.Sound.play(self.button_sound)
                            self.cursor_ms_counter = 0
                            self.setCharacter = False
                            if self.keyActive != "2":
                                self.setCharacter = True
                            self.keyActive = "2"
                            if self.tempLetter == "":
                                self.tempLetter = "a"
                            elif self.tempLetter == "a":
                                self.tempLetter = "b"
                            elif self.tempLetter == "b":
                                self.tempLetter = "c"
                            elif self.tempLetter == "c":
                                self.tempLetter = "2"
                            elif self.tempLetter == "2":
                                self.tempLetter = "a"
                    if event.key == K_RIGHT: #3 - arrow right 
                        if self.sceneActive == "menu":
                            pygame.mixer.Sound.play(self.button_sound)
                            if self.menu.menuButtonActive == "play":
                                self.menu.menuButtonActive = "rules"
                            elif self.menu.menuButtonActive == "rules":
                                self.menu.menuButtonActive = "high"
                            elif self.menu.menuButtonActive == "high":
                                self.menu.menuButtonActive = "about"
                            elif self.menu.menuButtonActive == "about":
                                self.menu.menuButtonActive = "play"
                        elif self.sceneActive =="GamePlay":
                            pygame.mixer.Sound.play(self.button_sound)
                            print("3")
                            self.input = self.input + "3"
                        elif self.sceneActive == "Name":
                            pygame.mixer.Sound.play(self.button_sound)
                            self.cursor_ms_counter = 0
                            self.setCharacter = False
                            if self.keyActive != "3":
                                self.setCharacter = True
                            self.keyActive = "3"
                            if self.tempLetter == "":
                                self.tempLetter = "d"
                            elif self.tempLetter == "d":
                                self.tempLetter = "e"
                            elif self.tempLetter == "e":
                                self.tempLetter = "f"
                            elif self.tempLetter == "f":
                                self.tempLetter = "3"
                            elif self.tempLetter == "3":
                                self.tempLetter = "d"
                        elif self.sceneActive == "High":
                            pass
                            # self.scoresLength = len("scoresarraylengthhere")
                            # self.something = math.floor(self.scoresLength/10)
                            # if self.add > self.something:
                            #     self.add += 1
                            # else:
                            #     self.add = 0

                    if event.key == K_LEFT: #4 - arrow left
                        if self.sceneActive == "menu":
                            pygame.mixer.Sound.play(self.button_error)
                        elif self.sceneActive =="GamePlay":
                            pygame.mixer.Sound.play(self.button_sound)
                            print("4")
                            self.input = self.input + "4"
                        elif self.sceneActive == "Name":
                            pygame.mixer.Sound.play(self.button_sound)
                            self.cursor_ms_counter = 0
                            self.setCharacter = False
                            if self.keyActive != "4":
                                self.setCharacter = True
                            self.keyActive = "4"
                            if self.tempLetter == "":
                                self.tempLetter = "g"
                            elif self.tempLetter == "g":
                                self.tempLetter = "h"
                            elif self.tempLetter == "h":
                                self.tempLetter = "i"
                            elif self.tempLetter == "i":
                                self.tempLetter = "4"
                            elif self.tempLetter == "4":
                                self.tempLetter = "g"
                    if event.key == K_SPACE: #5 - space
                        if self.sceneActive == "menu":
                            pygame.mixer.Sound.play(self.button_error)
                        elif self.sceneActive =="GamePlay":
                            pygame.mixer.Sound.play(self.button_sound)
                            print("5")
                            self.input = self.input + "5"
                    if event.key == K_w: #6 - w
                        if self.sceneActive == "menu":
                            pygame.mixer.Sound.play(self.button_error)
                        elif self.sceneActive =="GamePlay":
                            pygame.mixer.Sound.play(self.button_sound)
                            print("6")
                            self.input = self.input + "6"
                    if event.key == K_a: #7 - a
                        if self.sceneActive == "menu":
                            pygame.mixer.Sound.play(self.button_error)
                        elif self.sceneActive =="GamePlay":
                            pygame.mixer.Sound.play(self.button_sound)
                            print("7")
                            self.input = self.input + "7"
                    if event.key == K_s: #8 - s
                        if self.sceneActive == "menu":
                            pygame.mixer.Sound.play(self.button_error)
                        elif self.sceneActive =="GamePlay":
                            pygame.mixer.Sound.play(self.button_sound)
                            print("8")
                            self.input = self.input + "8"
                    if event.key == K_d: #9 -  d
                        if self.sceneActive == "menu":
                            pygame.mixer.Sound.play(self.button_error)
                        elif self.sceneActive =="GamePlay":
                            pygame.mixer.Sound.play(self.button_sound)
                            print("9")
                            self.input = self.input + "9"
                    if event.key == K_f: #* - f
                        if self.sceneActive == "menu":
                            pygame.mixer.Sound.play(self.button_error)
                        elif self.sceneActive =="GamePlay":
                            pygame.mixer.Sound.play(self.button_sound)
                            print("*")
                            self.input = self.input + "*"
                    if event.key == K_g: #0 - g
                        if self.sceneActive == "menu":
                            pygame.mixer.Sound.play(self.button_error)
                        elif self.sceneActive =="GamePlay":
                            pygame.mixer.Sound.play(self.button_sound)
                            print("0")
                            self.input = self.input + "0"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: ## - left click
                        if self.sceneActive == "menu":
                            pygame.mixer.Sound.play(self.button_error)
                        elif self.sceneActive =="GamePlay":
                            pygame.mixer.Sound.play(self.button_sound)
                            print("#")
                            self.input = self.input + "#"

            if self.sceneActive == "Name":
                self.cursor_ms_counter += self.clock.get_time()
                if self.cursor_ms_counter >= self.cursor_switch_ms:
                    self.cursor_ms_counter %= self.cursor_switch_ms
                    if self.tempLetter  != "":
                        self.setCharacter = True
                    print("temp letter " + str(self.tempLetter))
                if self.setCharacter:
                    self.enterName += self.tempLetter
                    self.tempLetter = ""
                    self.setCharacter = False


 
            # Detect events
            self.scene.on_event()
 
            # Update scene
            self.scene.on_update(self.menu.menuButtonActive)
 
            # Draw the screen
            self.scene.on_draw(self.screen, self)
            pygame.display.flip()

            if self.scene.changeScene == True :
                if self.scene.changeScene == "None":
                    pass
                elif self.scene.sceneMessage == "Game Play":
                    self.gamePlay = GamePlay(self)
                    self.change_scene(self.gamePlay)
                elif self.scene.sceneMessage == "Load Level":
                    self.leadLevel = LoadLevel(self)
                    self.change_scene(self.leadLevel)
                elif self.scene.sceneMessage == "Name":
                    self.name = Name(self)
                    self.change_scene(self.name)


            time = self.clock.tick(30)
 
    def change_scene(self, scene):
        "Changes the current scene."
        self.scene = scene
 
    def quit(self):
        self.quit_flag = True



class Scene:

    def __init__(self, director):
        self.director = director
        #self.screen = pygame.display.set_mode((1920, 1080),pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode((1280, 1000), pygame.FULLSCREEN)
        self.menuButtonActive = ""

        self.screenWidth = self.screen.get_rect().width
        self.screenHeight = self.screen.get_rect().height

        self.level = 1
        self.changeScene = False

        self.white = (255, 255, 255)
        self.black = (0,0,0)

        self.h0 = 200
        self.h1 = 150 #font size
        self.h3 = 70
        self.top = 175

    def on_update(self,state=""):
        "Called from the director and defined on the subclass."
        raise NotImplemented("on_update abstract method must be defined in subclass.")

    def on_event(self, event):
        "Called when a specific event is detected in the loop."
        raise NotImplemented("on_event abstract method must be defined in subclass.")

    def on_draw(self, screen, director):
        "Called when you want to draw the screen."
        raise NotImplemented("on_draw abstract method must be defined in subclass.")

    def text_to_screen(self, screen, text, x1, y1, size, color, font_type = "fonts/Roboto/Roboto-Light.ttf"):
        try:

            text = str(text)
            font = pygame.font.Font(font_type, size)
            text = font.render(text, True, color)
            x2 = x1 - text.get_rect().width/2
            y2 = y1 - text.get_rect().height/2 
            self.screen.blit(text, (x2, y2))

        except Exception as e:
            print('Font Error, saw it coming')
            raise e

    def text_to_screen_left(self, screen, text, x1, y1, size, color, font_type = "fonts/Roboto/Roboto-Light.ttf"):
        try:

            text = str(text)
            font = pygame.font.Font(font_type, size)
            text = font.render(text, True, color)
            y2 = y1 - text.get_rect().height/2 
            self.screen.blit(text, (x1, y2))

        except Exception as e:
            print('Font Error, saw it coming')
            raise e


class Menu(Scene):
    

    def __init__(self, director):


        Scene.__init__(self, director)

        director.sceneActive = "menu"
        self.menuButtonActive = "play"

        self.buttonColor = (35,108,135)
        self.buttonColorActive = (18,49,96)
        self.buttonTextColor = (255,255,255)
        self.buttonTextColorActive = (203,219,220)
        self.buttonFontSize = 80
        
        self.buttonWidth = self.screenWidth/2
        self.buttonHeight = self.screenHeight/6
        self.buttonX = self.screen.get_rect().width/2 - self.buttonWidth/2
        self.vSpacing = 37.4
        self.vOffset = (1080 - (self.buttonHeight*4 + self.vSpacing*3))/2

        self.screen.fill((98,200,196))
        
       
    def on_update(self,state):
        #pass
        if state == "play":
            self.playButton("active")
            self.rulesButton("inactive")
            self.highButton("inactive")
            self.aboutButton("inactive")
        elif state == "rules":
            self.playButton("inactive")
            self.rulesButton("active")
            self.highButton("inactive")
            self.aboutButton("inactive")
        elif state == "high":
            self.playButton("inactive")
            self.rulesButton("inactive")
            self.highButton("active")
            self.aboutButton("inactive")
        elif state == "about":
            self.playButton("inactive")
            self.rulesButton("inactive")
            self.highButton("inactive")
            self.aboutButton("active")

    def on_event(self):
        pass

    def on_draw(self, screen, director):
        pass

            
    def playButton(self, state):
        if state == "active":
            buttonY = self.vOffset
            playBTN = pygame.draw.rect(self.screen, self.buttonColorActive, [self.buttonX, buttonY, self.buttonWidth, self.buttonHeight])
            playText = self.text_to_screen(self.screen, 'Play', self.buttonWidth, (self.buttonHeight/2 + buttonY), self.buttonFontSize, self.buttonTextColorActive)
        elif state =="inactive":
            buttonY = self.vOffset
            playBTN = pygame.draw.rect(self.screen, self.buttonColor, [self.buttonX, buttonY, self.buttonWidth, self.buttonHeight])
            playText = self.text_to_screen(self.screen, 'Play', self.buttonWidth, (self.buttonHeight/2 + buttonY), self.buttonFontSize, self.buttonTextColor)


    def rulesButton(self, state):
        if state == "active":
            buttonY = self.buttonHeight*1 + self.vSpacing*1 + self.vOffset
            rulesBTN = pygame.draw.rect(self.screen, self.buttonColorActive, [self.buttonX, buttonY, self.buttonWidth, self.buttonHeight])
            rulesText = self.text_to_screen(self.screen, 'Rules', self.buttonWidth, (self.buttonHeight/2 + buttonY), self.buttonFontSize, self.buttonTextColorActive)
        elif state =="inactive":
            buttonY = self.buttonHeight*1 + self.vSpacing*1 + self.vOffset
            rulesBTN = pygame.draw.rect(self.screen, self.buttonColor, [self.buttonX, buttonY, self.buttonWidth, self.buttonHeight])
            rulesText = self.text_to_screen(self.screen, 'Rules', self.buttonWidth, (self.buttonHeight/2 + buttonY), self.buttonFontSize, self.buttonTextColor)
            
    def highButton(self, state):
        if state == "active":
            buttonY = self.buttonHeight*2 + self.vSpacing*2 + self.vOffset
            highBTN = pygame.draw.rect(self.screen, self.buttonColorActive, [self.buttonX, buttonY, self.buttonWidth, self.buttonHeight])
            highText = self.text_to_screen(self.screen, 'High Scores', self.buttonWidth, (self.buttonHeight/2 + buttonY), self.buttonFontSize, self.buttonTextColorActive)
        elif state =="inactive":
            buttonY = self.buttonHeight*2 + self.vSpacing*2 + self.vOffset
            highBTN = pygame.draw.rect(self.screen, self.buttonColor, [self.buttonX, buttonY, self.buttonWidth, self.buttonHeight])
            highText = self.text_to_screen(self.screen, 'High Scores', self.buttonWidth, (self.buttonHeight/2 + buttonY), self.buttonFontSize, self.buttonTextColor)


    def aboutButton(self, state):
        if state == "active":
            buttonY = self.buttonHeight*3 + self.vSpacing*3 + self.vOffset
            aboutBTN = pygame.draw.rect(self.screen, self.buttonColorActive, [self.buttonX, buttonY, self.buttonWidth, self.buttonHeight])
            aboutText = self.text_to_screen(self.screen, 'About', self.buttonWidth, (self.buttonHeight/2 + buttonY), self.buttonFontSize, self.buttonTextColorActive)
        elif state =="inactive":
            buttonY = self.buttonHeight*3 + self.vSpacing*3 + self.vOffset
            aboutBTN = pygame.draw.rect(self.screen, self.buttonColor, [self.buttonX, buttonY, self.buttonWidth, self.buttonHeight])
            aboutText = self.text_to_screen(self.screen, 'About', self.buttonWidth, (self.buttonHeight/2 + buttonY), self.buttonFontSize, self.buttonTextColor)
        

    

class LoadLevel(Scene):

    def __init__(self, director):
        self.director = director

        self.sceneMessage = "None"

        Scene.__init__(self, director)
        director.sceneActive = "LoadLevel"

        self.screen.fill((35,108,135))
        ##pygame.display.update()

        self.text_to_screen(self.screen, 'Level', self.screenWidth/2, self.top, self.h1, (0, 000, 000))

        self.levelNumber = self.text_to_screen(self.screen, str(self.director.level), self.screenWidth/2, self.screenHeight/2, self.h0, self.white)

        allOff()

    def on_update(self,state):
        pass

    def on_event(self):
        pass

    def on_draw(self, screen, director):
        #pass
        thetime = float(time.clock() - director.start_time)

        self.screen.fill((35,108,135))
        self.levelNumber = self.text_to_screen(self.screen, str(self.director.level), self.screenWidth/2, self.screenHeight/2, self.h0, self.white)

        self.text_to_screen(self.screen, 'Level', self.screenWidth/2, self.top, self.h1, self.white)
        

        if(thetime >= 0.6):
            self.changeScene = True
            self.sceneMessage = "Game Play"


class GamePlay(Scene):

    def __init__(self, director):
        self.director = director
        self.words=[['error arrays start at 1'],['45','2','GJ','Good Job'],['46','2','GM','Good Move'],['68','2','MT','Empty'],['72','2','PA','Parent Alert'],['77','2','PP','Personal Problem'],['93','2','WD','Well Done'],['299','3','ax','across'],['344','3','DH','Dear Husband'],['355','3','DK',"Don't Know"]]
        self.answer = self.words[self.director.level][3]
        self.updateInput = self.director.input
        self.bColor = (35,108,135)


        Scene.__init__(self, director)
        director.sceneActive = "GamePlay"
        
        self.screen.fill(self.bColor)

        self.text_to_screen(self.screen, 'Neil Says...', self.screenWidth/2, self.top, self.h1, self.white)
        self.answer = self.text_to_screen(self.screen, self.answer, self.screenWidth/2, self.screenHeight/2, 100, self.white)
        self.displayInput = self.text_to_screen(self.screen, self.updateInput, self.screenWidth/2, self.screenHeight/2 + 200, 50, self.white)
        
        self.lightsDone = False
    def on_update(self,state):
        pass

    def on_event(self):
        pass

    def on_draw(self, screen, director):
        self.director = director
        self.answer = self.words[self.director.level][3]

        self.raw = list(self.words[self.director.level][0])
        
        while not self.lightsDone:
            time.sleep(1)
            for x in range(0, len(self.raw)):
                if self.raw[x] == "2":
                    allOff()
                    if x != 0 and self.raw[x-1] == self.raw[x]:
                        time.sleep(1)
                    GPIO.output(15,GPIO.HIGH) # 2
                    time.sleep(1)
                elif self.raw[x] == "3":
                    allOff()
                    if x != 0 and self.raw[x-1] == self.raw[x]:
                        time.sleep(1)
                    GPIO.output(18,GPIO.HIGH) # 3
                    time.sleep(1)
                elif self.raw[x] == "4":
                    allOff()
                    if x != 0 and self.raw[x-1] == self.raw[x]:
                        time.sleep(1)
                    GPIO.output(23,GPIO.HIGH) # 4
                    time.sleep(1)
                elif self.raw[x] == "5":
                    allOff()
                    if x != 0 and self.raw[x-1] == self.raw[x]:
                        time.sleep(1)
                    GPIO.output(24,GPIO.HIGH) # 5
                    time.sleep(1)
                elif self.raw[x] == "6":
                    allOff()
                    if x != 0 and self.raw[x-1] == self.raw[x]:
                        time.sleep(1)
                    GPIO.output(25,GPIO.HIGH) # 6
                    time.sleep(1)
                elif self.raw[x] == "7":
                    allOff()
                    if x != 0 and self.raw[x-1] == self.raw[x]:
                        time.sleep(1)
                    GPIO.output(8,GPIO.HIGH) # 7
                    time.sleep(1)
                elif self.raw[x] == "8":
                    allOff()
                    if x != 0 and self.raw[x-1] == self.raw[x]:
                        time.sleep(1)
                    GPIO.output(7,GPIO.HIGH) # 8
                    time.sleep(1)
                elif self.raw[x] == "9":
                    allOff()
                    if x != 0 and self.raw[x-1] == self.raw[x]:
                        time.sleep(1)
                    GPIO.output(12,GPIO.HIGH) # 9
                    time.sleep(1)
                elif self.raw[x] == "0":
                    allOff()
                    if x != 0 and self.raw[x-1] == self.raw[x]:
                        time.sleep(1)
                    GPIO.output(20,GPIO.HIGH) # 0
                    time.sleep(1)
                elif self.raw[x] == "*":
                    allOff()
                    if x != 0 and self.raw[x-1] == self.raw[x]:
                        time.sleep(1)
                    GPIO.output(16,GPIO.HIGH) # *
                    time.sleep(1)
                elif self.raw[x] == "#":
                    allOff()
                    if x != 0 and self.raw[x-1] == self.raw[x]:
                        time.sleep(1)
                    GPIO.output(21,GPIO.HIGH) # #
                    time.sleep(1)
                elif self.raw[x] == "1":
                    allOff()
                    if x != 0 and self.raw[x-1] == self.raw[x]:
                        time.sleep(1)
                    GPIO.output(14,GPIO.HIGH) # 1
                    time.sleep(1)
            if x == len(self.raw) - 1:
                if x != 0 and self.raw[x-1] == self.raw[x]:
                        time.sleep(1)
                self.lightsDone = True
                allOff()
                self.director.input = ""


        if len(self.updateInput) == len(self.words[self.director.level][0]):
            if self.updateInput == self.words[self.director.level][0]:
                self.bColor = ((101,196,121)) #GREEN
                self.screen.fill(self.bColor)
                self.answer = self.words[self.director.level][2]

                self.text_to_screen(self.screen, 'Neil Says...', self.screenWidth/2, self.top, self.h1, self.black)
                self.answer = self.text_to_screen(self.screen, self.answer, self.screenWidth/2, self.screenHeight/2, 100, self.white)
                self.displayInput = self.text_to_screen(self.screen, self.updateInput, self.screenWidth/2, self.screenHeight/2 + 200, 50, self.white)
    
                print("correct! " + self.words[self.director.level][1])
                pygame.display.update()
                pause(2000)
                self.director.input = ""
                director.start_time = time.clock()
                self.director.level = self.director.level + 1
                self.changeScene = True
                self.sceneMessage = "Load Level"
                self.bColor = (35,108,135)
            else:
                self.bColor = ((196,105,101)) #RED
                self.screen.fill(self.bColor)
                self.answer = self.words[self.director.level][2]

                self.text_to_screen(self.screen, 'Game Play', self.screenWidth/2, self.top, self.h1, self.white)
                self.answer = self.text_to_screen(self.screen, self.answer, self.screenWidth/2, self.screenHeight/2, 100, self.white)
                self.displayInput = self.text_to_screen(self.screen, self.updateInput, self.screenWidth/2, self.screenHeight/2 + 200, 50, self.white)
    
                print("wrong! " + self.words[self.director.level][1])
                pygame.display.update()
                pause(2000)
                self.director.input = ""
                director.start_time = time.clock()
                self.changeScene = True
                self.sceneMessage = "Name"
                self.bColor = (35,108,135)
     


        self.updateInput = self.director.input
        self.screen.fill(self.bColor)
    
        self.text_to_screen(self.screen, 'Neil Says...', self.screenWidth/2, self.top, self.h1, self.white)
        self.answer = self.text_to_screen(self.screen, self.answer, self.screenWidth/2, self.screenHeight/2, 100, self.white)
        self.displayInput = self.text_to_screen(self.screen, self.updateInput, self.screenWidth/2, self.screenHeight/2 + 200, 50, self.white)


class Name(Scene):

    def __init__(self, director):

        Scene.__init__(self, director)
        director.sceneActive = "Name"

        self.screen.fill((35,108,135))

        self.text_to_screen(self.screen, 'Use Keypad to Enter Name', self.screenWidth/2, 100, 50, self.white)
        
        
        self.cursor_switch_ms = 500 # /|\
        self.cursor_ms_counter = 0
        self.cursor_visible = True # So the user sees where he writes

        
        self.cursor = "|"
        director.enterName = ""
        self.nameBox = self.text_to_screen(self.screen, director.enterName, self.screenWidth/2, 300, 50, self.white)

    def on_update(self,state):
        pass


    def on_event(self):
        pass

    def on_draw(self, screen, director):
        #pass
        self.text = str(director.enterName)
        self.font = pygame.font.Font("fonts/Roboto/Roboto-Light.ttf", 50)
        self.text = self.font.render(self.text, True, self.white)
        self.nameBoxWidth = self.text.get_rect().width

        self.screen.fill((35,108,135))
        self.text_to_screen(self.screen, 'Use Keypad to Enter Name', self.screenWidth/2, 100, 50, self.white)
        self.text_to_screen(self.screen, self.cursor, self.screenWidth/2 + self.nameBoxWidth/2, 300, 50, self.white)
        self.text_to_screen(self.screen, " " + str(director.tempLetter), self.screenWidth/2 + self.nameBoxWidth/2 + 10, 300, 50, self.white)
        self.nameBox = self.text_to_screen(self.screen, director.enterName, self.screenWidth/2, 300, 50, self.white)

        self.cursor_ms_counter += director.clock.get_time()
        if self.cursor_ms_counter >= self.cursor_switch_ms:
            self.cursor_ms_counter %= self.cursor_switch_ms
            self.cursor_visible = not self.cursor_visible

        if self.cursor_visible:
            self.cursor = "|"
        else:
            self.cursor = ""

class Rules(Scene):

    def __init__(self, director):

        Scene.__init__(self, director)
        director.sceneActive = "LoadLevel"

        self.screen.fill((35,108,135))
        ##pygame.display.update()

        self.text_to_screen(self.screen, 'Rules', self.screenWidth/2, self.top, self.h1, self.white)

        allOff()

    def on_update(self,state):
        pass

    def on_event(self):
        pass

    def on_draw(self, screen, director):
        pass



class High(Scene):

    def __init__(self, director):

        Scene.__init__(self, director)
        director.sceneActive = "High"

        self.screen.fill((35,108,135))
        
        ##save high scores to external file. maybe txt? or maybe and array in a .py (so the array can be ordered)
        self.text_to_screen(self.screen, 'High Scores', self.screenWidth/2, self.top, self.h1, self.white)
        

       



        # Re-load our database
        with open(director.highScores,'rb') as rfp:
            director.scores = pickle.load(rfp)

        print(director.scores)
        

        # sort list with key
        director.scores.sort(key=self.takeSecond, reverse=True)
        print(director.scores)
        director.add = 0
        self.vSpacing = 70
        self.vOffset = self.top + 150


        allOn()
    def takeSecond(self,elem):
            return elem[0]

    def on_update(self,state):
        pass

    def on_event(self):
        pass

    def on_draw(self, screen, director):
        #pass
        self.screen.fill((35,108,135))
        
        ##save high scores to external file. maybe txt? or maybe and array in a .py (so the array can be ordered)
        self.text_to_screen(self.screen, 'High Scores', self.screenWidth/2, self.top, self.h1, self.white)

        for x in range(0, 10):
            #self.text_to_screen(self.screen, str(director.scores[x][0]) + "....." + str(director.scores[x][1]), self.screenWidth/2, self.vOffset + self.vSpacing*x, self.h3, self.white)
            if x < 9:
                self.text_to_screen_left(self.screen, str(director.scores[x][0]), self.screenWidth/2 - 125, self.vOffset + self.vSpacing*x, self.h3, self.white)
                self.text_to_screen_left(self.screen, str(director.scores[x][1]), self.screenWidth/2 + 100, self.vOffset + self.vSpacing*x, self.h3, self.white)
            else:
                self.text_to_screen_left(self.screen, str(director.recentScore[0]), self.screenWidth/2 - 125, self.vOffset + self.vSpacing*x, self.h3, self.black)
                self.text_to_screen_left(self.screen, str(director.recentScore[1]), self.screenWidth/2 + 100, self.vOffset + self.vSpacing*x, self.h3, self.black)
            
class High_Menu(Scene):

    def __init__(self, director):

        Scene.__init__(self, director)
        director.sceneActive = "High Menu"

        self.screen.fill((35,108,135))
        
        ##save high scores to external file. maybe txt? or maybe and array in a .py (so the array can be ordered)
        self.text_to_screen(self.screen, 'High Scores', self.screenWidth/2, self.top, self.h1, self.white)
        

       



        # Re-load our database
        with open(director.highScores,'rb') as rfp:
            director.scores = pickle.load(rfp)

        print(director.scores)
        

        # sort list with key
        director.scores.sort(key=self.takeSecond, reverse=True)
        print(director.scores)
        director.add = 0
        self.vSpacing = 70
        self.vOffset = self.top + 150


        allOn()
    def takeSecond(self,elem):
            return elem[0]

    def on_update(self,state):
        pass

    def on_event(self):
        pass

    def on_draw(self, screen, director):
        #pass
        self.screen.fill((35,108,135))
        
        ##save high scores to external file. maybe txt? or maybe and array in a .py (so the array can be ordered)
        self.text_to_screen(self.screen, 'High Scores', self.screenWidth/2, self.top, self.h1, self.white)

        for x in range(0, 10):
            #self.text_to_screen(self.screen, str(director.scores[x][0]) + "....." + str(director.scores[x][1]), self.screenWidth/2, self.vOffset + self.vSpacing*x, self.h3, self.white)
            
            self.text_to_screen_left(self.screen, str(director.scores[x][0]), self.screenWidth/2 - 125, self.vOffset + self.vSpacing*x, self.h3, self.white)
            self.text_to_screen_left(self.screen, str(director.scores[x][1]), self.screenWidth/2 + 100, self.vOffset + self.vSpacing*x, self.h3, self.white)


class About(Scene):

    def __init__(self, director):

        Scene.__init__(self, director)
        director.sceneActive = "About"

        self.screen.fill((35,108,135))

        self.text_to_screen(self.screen, 'About', self.screenWidth/2, self.top, self.h1, self.white)

        allOff()
    def on_update(self,state):
        pass

    def on_event(self):
        pass

    def on_draw(self, screen, director):
        pass
# ---------------------------------------------------------------------

# Functions
# ---------------------------------------------------------------------



# ---------------------------------------------------------------------

def main():
    dir = Director()
    scene = Menu(dir)
    dir.change_scene(scene)
    dir.loop()


if __name__ == '__main__':
    pygame.mixer.pre_init(44100,16,2,4096)
    pygame.init()
    main()