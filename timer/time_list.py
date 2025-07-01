 
import pygame
import datetime
import time
from datetime import timedelta
from agoTime import AgoTime
from draw_tool import gameContext

class TimeList:
    START_STATE="Start"
    STOP_STATE="Stop"
    START_X = 10 
    START_Y = 200  
    TIME_X = 180 
    TIME_Y = 50
    BOX_X = 100 
    BOX_Y = 150
    ALLTIME_X = 40 
    ALLTIME_Y = 50  
    COUNT_X = 140
    COUNT_Y = 120
    def __init__(self,left,top):
        self.agoTime = []
        self.left = left
        self.top = top
        self.StartState = TimeList.STOP_STATE
        self.startTime = 0 
        self.stopTime = 0 
        self.oneTime = 0 
        self.allTimeIds = 0
        self.allTime = timedelta(days=0, hours=0, minutes=0, seconds=0)
    def mouseClick(self,x:int,y:int):
        if ( x>=self.left+TimeList.START_X and x<=self.left+TimeList.START_X+60 and y>=self.top+ TimeList.START_Y and y<=self.top+ TimeList.START_Y+100 ):
            if(self.StartState == TimeList.START_STATE):
                self.oneTime = self.stopTime-self.startTime
                self.allTime = self.allTime + self.oneTime 
                self.StartState = TimeList.STOP_STATE
                print (self.allTime)
                new_value = AgoTime(
                    self.left + self.BOX_X + 20,
                    self.top + self.BOX_Y + self.allTimeIds * 30,
                    self.startTime,
                    self.stopTime
                )
                self.agoTime.append(new_value)
                self.allTimeIds+= 1
            else:
                self.StartState = TimeList.START_STATE

                self.startTime = datetime.datetime.now()
                
                
    def mainLoop(self):
        #直線s
        for i in range(len(self.agoTime)):
            self.agoTime[i].draw()
        
        font = pygame.font.SysFont("Microsoft JhengHei", 25)
        if (self.StartState == TimeList.START_STATE):
            self.stopTime = datetime.datetime.now()
            delta = self.stopTime-self.startTime
            seconds = delta.total_seconds()
            text_surface = font.render (str(delta), True, (0, 100, 0)) 
            gameContext.screen.blit(text_surface, (self.left+TimeList.COUNT_X+5, self.top+ TimeList.COUNT_Y))  
        
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+TimeList.START_X, self.top+ TimeList.START_Y), (self.left+TimeList.START_X+60, self.top+ TimeList.START_Y), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+TimeList.START_X+60, self.top+ TimeList.START_Y), (self.left+TimeList.START_X+60, self.top+ TimeList.START_Y+100), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+TimeList.START_X+60, self.top+ TimeList.START_Y+100), (self.left+TimeList.START_X, self.top+ TimeList.START_Y+100), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+TimeList.START_X, self.top+ TimeList.START_Y+100), (self.left+TimeList.START_X, self.top+ TimeList.START_Y), 2)
        text_surface = font.render(self.StartState, True, (0, 0, 0)) 
        gameContext.screen.blit(text_surface, (self.left+TimeList.START_X+5, self.top+ TimeList.START_Y))  
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+ TimeList.TIME_X, self.top+ TimeList.TIME_Y), (self.left+ TimeList.TIME_X+200, self.top+ TimeList.TIME_Y), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+ TimeList.TIME_X+200, self.top+ TimeList.TIME_Y), (self.left+ TimeList.TIME_X+200, self.top+ TimeList.TIME_Y+40), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+ TimeList.TIME_X+200, self.top+ TimeList.TIME_Y+40), (self.left+ TimeList.TIME_X, self.top+ TimeList.TIME_Y+40), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+ TimeList.TIME_X, self.top+ TimeList.TIME_Y+40), (self.left+ TimeList.TIME_X, self.top+ TimeList.TIME_Y), 2)
        text_surface = font.render(str(self.allTime), True, (255, 0, 0)) 
        gameContext.screen.blit(text_surface, (self.left+ TimeList.TIME_X+5, self.top+ TimeList.TIME_Y))  
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+ TimeList.BOX_X, self.top+ TimeList.BOX_Y), (self.left+ TimeList.BOX_X+250, self.top+ TimeList.BOX_Y), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+ TimeList.BOX_X+250, self.top+ TimeList.BOX_Y), (self.left+ TimeList.BOX_X+250, self.top+ TimeList.BOX_Y+300), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+ TimeList.BOX_X+250, self.top+ TimeList.BOX_Y+300), (self.left+ TimeList.BOX_X, self.top+ TimeList.BOX_Y+300), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+ TimeList.BOX_X, self.top+ TimeList.BOX_Y+300), (self.left+ TimeList.BOX_X, self.top+ TimeList.BOX_Y), 2)
        text_surface = font.render("", True, (0, 0, 0)) 
        gameContext.screen.blit(text_surface, (self.left+ TimeList.BOX_X+5, self.top+ TimeList.BOX_Y))  
        
        text_surface = font.render("已累積時間", True, (0, 0, 0)) 
        gameContext.screen.blit(text_surface, (self.left+ TimeList.ALLTIME_X, self.top+ TimeList.ALLTIME_Y))

       


