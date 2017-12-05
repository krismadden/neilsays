#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#raspberry pi turn on led https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins
#text converter https://www.dcode.fr/multitap-abc-cipher 

import pygame, sys, time
from pygame.locals import *
import os

from pygame_functions import *



class Director:
    """Represents the main object of the game.
 
    The Director object keeps the game on, and takes care of updating it,
    drawing it and propagate events.
 
    This object must be used with Scene objects that are defined later."""

    def __init__(self):
        self.sceneActive = "menu"
        self.level = 1
        self.menu = Menu(self)


        self.screen = pygame.display.set_mode((1000,561), pygame.FULLSCREEN)
        pygame.display.set_caption("Neil Says")
        self.quit_flag = False
        self.clock = pygame.time.Clock()
        pygame.mouse.set_visible(0)
        self.input = ""


    def loop(self):
        "Main game loop."
 
        while not self.quit_flag:
            #time = self.clock.tick(30) #i put this at the end of the function
 
            # Exit events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    print(self.input)
                    if event.key == pygame.K_ESCAPE:
                        self.quit()
                    if event.key == K_q:
                        self.leadLevel = LoadLevel(self)
                        self.change_scene(self.leadLevel)
                        print("hi mom")
                    if event.key == K_UP: #1 - arrow up
                        if self.sceneActive == "menu":
                            if self.menu.menuButtonActive == "play":
                                self.menu.menuButtonActive = "about"
                            elif self.menu.menuButtonActive == "rules":
                                self.menu.menuButtonActive = "play"
                            elif self.menu.menuButtonActive == "high":
                                self.menu.menuButtonActive = "rules"
                            elif self.menu.menuButtonActive == "about":
                                self.menu.menuButtonActive = "high"
                            ##pygame.display.update()
                        elif self.sceneActive =="GamePlay":
                            print("1")
                            self.input = self.input + "1"
                    if event.key == K_DOWN: #2 - arrow down
                        if self.sceneActive == "menu":
                            if self.menu.menuButtonActive == "play":
                                self.leadLevel = LoadLevel(self)
                                self.change_scene(self.leadLevel)
                            elif self.menu.menuButtonActive == "rules":
                                self.rules = Rules(self)
                                self.change_scene(self.rules)
                            elif self.menu.menuButtonActive == "high":
                                self.high = High(self)
                                self.change_scene(self.high)
                            elif self.menu.menuButtonActive == "about":
                                self.about = About(self)
                                self.change_scene(self.about)
                        elif self.sceneActive =="GamePlay":
                            print("2")
                            self.input = self.input + "2"
                    if event.key == K_RIGHT: #3 - arrow right 
                        if self.sceneActive == "menu":
                            if self.menu.menuButtonActive == "play":
                                self.menu.menuButtonActive = "rules"
                            elif self.menu.menuButtonActive == "rules":
                                self.menu.menuButtonActive = "high"
                            elif self.menu.menuButtonActive == "high":
                                self.menu.menuButtonActive = "about"
                            elif self.menu.menuButtonActive == "about":
                                self.menu.menuButtonActive = "play"
                        elif self.sceneActive =="GamePlay":
                            print("3")
                            self.input = self.input + "3"
                    if event.key == K_LEFT: #4 - arrow left
                        if self.sceneActive == "menu":
                            pass
                        elif self.sceneActive =="GamePlay":
                            print("4")
                            self.input = self.input + "4"
                    if event.key == K_SPACE: #5 - space
                        if self.sceneActive == "menu":
                            pass
                        elif self.sceneActive =="GamePlay":
                            print("5")
                            self.input = self.input + "5"
                    if event.key == K_w: #6 - w
                        if self.sceneActive == "menu":
                            pass
                        elif self.sceneActive =="GamePlay":
                            print("6")
                            self.input = self.input + "6"
                    if event.key == K_a: #7 - a
                        if self.sceneActive == "menu":
                            pass
                        elif self.sceneActive =="GamePlay":
                            print("7")
                            self.input = self.input + "7"
                    if event.key == K_s: #8 - s
                        if self.sceneActive == "menu":
                            pass
                        elif self.sceneActive =="GamePlay":
                            print("8")
                            self.input = self.input + "8"
                    if event.key == K_d: #9 -  d
                        if self.sceneActive == "menu":
                            pass
                        elif self.sceneActive =="GamePlay":
                            print("9")
                            self.input = self.input + "9"
                    if event.key == K_f: #* - f
                        if self.sceneActive == "menu":
                            pass
                        elif self.sceneActive =="GamePlay":
                            print("*")
                            self.input = self.input + "*"
                    if event.key == K_g: #0 - g
                        if self.sceneActive == "menu":
                            pass
                        elif self.sceneActive =="GamePlay":
                            print("0")
                            self.input = self.input + "0"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: ## - left click
                        if self.sceneActive == "menu":
                            pass
                        elif self.sceneActive =="GamePlay":
                            print("#")
                            self.input = self.input + "#"

 
            # Detect events
            self.scene.on_event()
 
            # Update scene
            self.scene.on_update(self.menu.menuButtonActive)
 
            # Draw the screen
            self.scene.on_draw(self.screen, self)
            pygame.display.flip()
            #print(self.menu.menuButtonActive)

            if self.scene.changeScene == True :
                if self.scene.changeScene == "None":
                    pass
                elif self.scene.sceneMessage == "Game Play":
                    self.gamePlay = GamePlay(self)
                    self.change_scene(self.gamePlay)


            time = self.clock.tick(30)
 
    def change_scene(self, scene):
        "Changes the current scene."
        self.scene = scene
 
    def quit(self):
        self.quit_flag = True



class Scene:

    def __init__(self, director):
        self.director = director
        self.screen = pygame.display.set_mode((1000,561), pygame.FULLSCREEN)
        self.menuButtonActive = ""

        self.screenWidth = self.screen.get_rect().width
        self.screenHeight = self.screen.get_rect().height

        self.level = 1
        self.changeScene = False

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


class Menu(Scene):
    

    def __init__(self, director):


        Scene.__init__(self, director)

        director.sceneActive = "menu"
        self.menuButtonActive = "play"

        self.buttonColor = (35,108,135)
        self.buttonColorActive = (18,49,96)
        self.buttonTextColor = (255,255,255)
        self.buttonTextColorActive = (203,219,220)
        self.buttonFontSize = 50
        
        self.buttonWidth = self.screenWidth/2
        self.buttonHeight = self.screenHeight/6
        self.buttonX = self.screen.get_rect().width/2 - self.buttonWidth/2
        self.vSpacing = 37.4

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
            ##pygame.display.update()
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
            buttonY = self.vSpacing
            playBTN = pygame.draw.rect(self.screen, self.buttonColorActive, [self.buttonX, buttonY, self.buttonWidth, self.buttonHeight])
            playText = self.text_to_screen(self.screen, 'PLAY', self.buttonWidth, (self.buttonHeight/2 + buttonY), self.buttonFontSize, self.buttonTextColorActive)
        elif state =="inactive":
            buttonY = self.vSpacing
            playBTN = pygame.draw.rect(self.screen, self.buttonColor, [self.buttonX, buttonY, self.buttonWidth, self.buttonHeight])
            playText = self.text_to_screen(self.screen, 'PLAY', self.buttonWidth, (self.buttonHeight/2 + buttonY), self.buttonFontSize, self.buttonTextColor)

    def rulesButton(self, state):
        if state == "active":
            buttonY = self.buttonHeight*1 + self.vSpacing*2
            rulesBTN = pygame.draw.rect(self.screen, self.buttonColorActive, [self.buttonX, buttonY, self.buttonWidth, self.buttonHeight])
            rulesText = self.text_to_screen(self.screen, 'RULES', self.buttonWidth, (self.buttonHeight/2 + buttonY), self.buttonFontSize, self.buttonTextColorActive)
        elif state =="inactive":
            buttonY = self.buttonHeight*1 + self.vSpacing*2
            rulesBTN = pygame.draw.rect(self.screen, self.buttonColor, [self.buttonX, buttonY, self.buttonWidth, self.buttonHeight])
            rulesText = self.text_to_screen(self.screen, 'RULES', self.buttonWidth, (self.buttonHeight/2 + buttonY), self.buttonFontSize, self.buttonTextColor)
            
    def highButton(self, state):
        if state == "active":
            buttonY = self.buttonHeight*2 + self.vSpacing*3
            highBTN = pygame.draw.rect(self.screen, self.buttonColorActive, [self.buttonX, buttonY, self.buttonWidth, self.buttonHeight])
            highText = self.text_to_screen(self.screen, 'HIGH SCORES', self.buttonWidth, (self.buttonHeight/2 + buttonY), self.buttonFontSize, self.buttonTextColorActive)
        elif state =="inactive":
            buttonY = self.buttonHeight*2 + self.vSpacing*3
            highBTN = pygame.draw.rect(self.screen, self.buttonColor, [self.buttonX, buttonY, self.buttonWidth, self.buttonHeight])
            highText = self.text_to_screen(self.screen, 'HIGH SCORES', self.buttonWidth, (self.buttonHeight/2 + buttonY), self.buttonFontSize, self.buttonTextColor)


    def aboutButton(self, state):
        if state == "active":
            buttonY = self.buttonHeight*3 + self.vSpacing*4
            aboutBTN = pygame.draw.rect(self.screen, self.buttonColorActive, [self.buttonX, buttonY, self.buttonWidth, self.buttonHeight])
            aboutText = self.text_to_screen(self.screen, 'ABOUT', self.buttonWidth, (self.buttonHeight/2 + buttonY), self.buttonFontSize, self.buttonTextColorActive)
        elif state =="inactive":
            buttonY = self.buttonHeight*3 + self.vSpacing*4
            aboutBTN = pygame.draw.rect(self.screen, self.buttonColor, [self.buttonX, buttonY, self.buttonWidth, self.buttonHeight])
            aboutText = self.text_to_screen(self.screen, 'ABOUT', self.buttonWidth, (self.buttonHeight/2 + buttonY), self.buttonFontSize, self.buttonTextColor)
        

    

class LoadLevel(Scene):

    def __init__(self, director):
        self.director = director

        self.sceneMessage = "None"
        self.start_time = time.clock()

        Scene.__init__(self, director)
        director.sceneActive = "LoadLevel"

        self.screen.fill((35,108,135))
        ##pygame.display.update()

        self.text_to_screen(self.screen, 'Level', self.screenWidth/2, 100, 100, (0, 000, 000))

        self.levelNumber = self.text_to_screen(self.screen, str(self.director.level), self.screenWidth/2, self.screenHeight/2, 200, (0, 000, 000))
       
    def on_update(self,state):
        pass

    def on_event(self):
        pass

    def on_draw(self, screen, director):
        #pass
        thetime = int(time.clock() - self.start_time)
        if(thetime >= 0.1):
            self.changeScene = True
            self.sceneMessage = "Game Play"


class GamePlay(Scene):

    def __init__(self, director):
        self.director = director
        self.words=[['error arrays start at 1'],['45','2','GJ','Good Job'],['46','2','GM','Good Move'],['68','2','MT','Empty'],['72','2','PA','Parent Alert'],['77','2','PP','Personal Problem'],['93','2','WD','Well Done'],['299','3','ax','across'],['344','3','DH','Dear Husband'],['355','3','DK',"Don't Know"]]
        self.answer = self.words[self.director.level][3]
        self.updateInput = self.director.input
        self.bColor = (35,108,135)
        print(self.updateInput)

        Scene.__init__(self, director)
        director.sceneActive = "GamePlay"
        
        self.screen.fill(bColor)
        ##pygame.display.update()

        self.text_to_screen(self.screen, 'Game Play', self.screenWidth/2, 100, 100, (0, 000, 000))

        self.answer = self.text_to_screen(self.screen, self.answer, self.screenWidth/2, self.screenHeight/2, 100, (0, 000, 000))

        self.displayInput = self.text_to_screen(self.screen, self.updateInput, self.screenWidth/2, self.screenHeight/2 + 200, 50, (0, 000, 000))
    def on_update(self,state):
        pass

    def on_event(self):
        pass

    def on_draw(self, screen, director):
        self.director = director
        self.answer = self.words[self.director.level][3]


        if len(self.updateInput) == len(self.words[self.director.level][0]):
            if self.updateInput == self.words[self.director.level][0]:
                self.bColor = (0,255,0)
                self.answer = self.words[self.director.level][2]
                print("correct! " + self.words[self.director.level][1])
                pause(1000)
                self.director.input = ""
                self.director.level = self.director.level + 1
                director.change_scene(director.leadLevel)
                self.bColor = (35,108,135)
            else:
                self.bColor(255,0,0)
                self.answer = self.words[self.director.level][2]
                print("wrong! " + self.words[self.director.level][1])
                pause(1000)
                self.director.input = ""
                self.director.level = self.director.level + 1
                director.change_scene(director.leadLevel) 
                self.bColor = (35,108,135)
     


        self.updateInput = self.director.input
        self.screen.fill(self.bColor)
    
        self.text_to_screen(self.screen, 'Game Play', self.screenWidth/2, 100, 100, (0, 000, 000))
        self.answer = self.text_to_screen(self.screen, self.answer, self.screenWidth/2, self.screenHeight/2, 100, (0, 000, 000))
        self.displayInput = self.text_to_screen(self.screen, self.updateInput, self.screenWidth/2, self.screenHeight/2 + 200, 50, (0, 000, 000))


class Rules(Scene):

    def __init__(self, director):

        Scene.__init__(self, director)
        director.sceneActive = "LoadLevel"

        self.screen.fill((35,108,135))
        ##pygame.display.update()

        self.text_to_screen(self.screen, 'Rules', self.screenWidth/2, 100, 100, (0, 000, 000))

    def on_update(self,state):
        pass

    def on_event(self):
        pass

    def on_draw(self, screen, director):
        pass


class High(Scene):

    def __init__(self, director):

        Scene.__init__(self, director)
        director.sceneActive = "LoadLevel"

        self.screen.fill((35,108,135))
        ##pygame.display.update()

        self.text_to_screen(self.screen, 'High Scores', self.screenWidth/2, 100, 100, (0, 000, 000))

    def on_update(self,state):
        pass

    def on_event(self):
        pass

    def on_draw(self, screen, director):
        pass

class About(Scene):

    def __init__(self, director):

        Scene.__init__(self, director)
        director.sceneActive = "LoadLevel"

        self.screen.fill((35,108,135))
        ##pygame.display.update()

        self.text_to_screen(self.screen, 'About', self.screenWidth/2, 100, 100, (0, 000, 000))

       
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
    pygame.init()
    main()