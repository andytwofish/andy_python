 
import pygame
from draw_tool import gameContext

class TimeList:
    START_STATE="Start"
    STOP_STATE="Stop"
    START_X = 10 
    START_Y = 200  
    TIME_X = 300 
    TIME_Y = 40
    BOX_X = 100 
    BOX_Y = 150
    ALLTIME_X = 100 
    ALLTIME_Y = 50  
    COUNT_X = 140
    COUNT_Y = 120
    def __init__(self,left,top):
        self.left = left
        self.top = top
        self.StartState = TimeList.STOP_STATE
        self.startTime = 0 
        self.stopTime = 0 
        self.oneTime = 0 
    def mouseClick(self,x:int,y:int):
        import datetime
        import time
        if ( x>=self.left+TimeList.START_X and x<=self.left+TimeList.START_X+60 and y>=self.top+ TimeList.START_Y and y<=self.top+ TimeList.START_Y+100 ):
            if(self.StartState == TimeList.START_STATE):
                self.StartState = TimeList.STOP_STATE 
            else:
                self.StartState = TimeList.START_STATE
                now = datetime.datetime.now()
                self.startTime = now
    def mainLoop(self):
        #直線s
        font = pygame.font.SysFont("Microsoft JhengHei", 25)
        import datetime
        import time
        if (self.StartState == TimeList.START_STATE):
            now = datetime.datetime.now()
            self.stopTime = now
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
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+ TimeList.TIME_X, self.top+ TimeList.TIME_Y), (self.left+ TimeList.TIME_X+80, self.top+ TimeList.TIME_Y), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+ TimeList.TIME_X+80, self.top+ TimeList.TIME_Y), (self.left+ TimeList.TIME_X+80, self.top+ TimeList.TIME_Y+40), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+ TimeList.TIME_X+80, self.top+ TimeList.TIME_Y+40), (self.left+ TimeList.TIME_X, self.top+ TimeList.TIME_Y+40), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+ TimeList.TIME_X, self.top+ TimeList.TIME_Y+40), (self.left+ TimeList.TIME_X, self.top+ TimeList.TIME_Y), 2)
        text_surface = font.render("time", True, (0, 0, 0)) 
        gameContext.screen.blit(text_surface, (self.left+ TimeList.TIME_X+5, self.top+ TimeList.TIME_Y))  
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+ TimeList.BOX_X, self.top+ TimeList.BOX_Y), (self.left+ TimeList.BOX_X+250, self.top+ TimeList.BOX_Y), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+ TimeList.BOX_X+250, self.top+ TimeList.BOX_Y), (self.left+ TimeList.BOX_X+250, self.top+ TimeList.BOX_Y+300), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+ TimeList.BOX_X+250, self.top+ TimeList.BOX_Y+300), (self.left+ TimeList.BOX_X, self.top+ TimeList.BOX_Y+300), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+ TimeList.BOX_X, self.top+ TimeList.BOX_Y+300), (self.left+ TimeList.BOX_X, self.top+ TimeList.BOX_Y), 2)
        text_surface = font.render("", True, (0, 0, 0)) 
        gameContext.screen.blit(text_surface, (self.left+ TimeList.BOX_X+5, self.top+ TimeList.BOX_Y))  
        
        text_surface = font.render("已累積時間", True, (0, 0, 0)) 
        gameContext.screen.blit(text_surface, (self.left+ TimeList.ALLTIME_X, self.top+ TimeList.ALLTIME_Y))

       


