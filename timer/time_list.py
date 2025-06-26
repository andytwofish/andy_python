 
import pygame
from draw_tool import gameContext

class TimeList:
    START_STATE=1
    STOP_STATE=2
    START_X = 10 
    START_Y = 200  
    TIME_X = 300 
    TIME_Y = 40
    BOX_X = 100 
    BOX_Y = 150
    ALLTIME_X = 100 
    ALLTIME_Y = 50  
    def __init__(self,left,top):
        self.left = left
        self.top = top
        self.StartState = TimeList.START_STATE

    def mouseClick(self,x:int,y:int):
        if ( x>=self.left+TimeList.START_X and x<=self.left+TimeList.START_X+60 and y>=self.top+ TimeList.START_Y and y<=self.top+ TimeList.START_Y+100 ):
            if(self.StartState = TimeList.START_STATE):
                            
            print("start")
    def mainLoop(self):
        font = pygame.font.SysFont("Microsoft JhengHei", 25)
        #直線
        
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+TimeList.START_X, self.top+ TimeList.START_Y), (self.left+TimeList.START_X+60, self.top+ TimeList.START_Y), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+TimeList.START_X+60, self.top+ TimeList.START_Y), (self.left+TimeList.START_X+60, self.top+ TimeList.START_Y+100), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+TimeList.START_X+60, self.top+ TimeList.START_Y+100), (self.left+TimeList.START_X, self.top+ TimeList.START_Y+100), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+TimeList.START_X, self.top+ TimeList.START_Y+100), (self.left+TimeList.START_X, self.top+ TimeList.START_Y), 2)
        text_surface = font.render("Start", True, (0, 0, 0)) 
        gameContext.screen.blit(text_surface, (self.left+TimeList.START_X+5, self.top+ TimeList.START_Y))  
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+ TimeList.TIME_X, self.top+ TimeList.TIME_Y), (self.left+ TimeList.TIME_X+80, self.top+ TimeList.TIME_Y), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+ TimeList.TIME_X+80, self.top+ TimeList.TIME_Y), (self.left+ TimeList.TIME_X+80, self.top+ TimeList.TIME_Y+40), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+ TimeList.TIME_X+80, self.top+ TimeList.TIME_Y+40), (self.left+ TimeList.TIME_X, self.top+ TimeList.TIME_Y+40), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+ TimeList.TIME_X, self.top+ TimeList.TIME_Y+40), (self.left+ TimeList.TIME_X, self.top+ TimeList.TIME_Y), 2)
        text_surface = font.render("Time", True, (0, 0, 0)) 
        gameContext.screen.blit(text_surface, (self.left+ TimeList.TIME_X+5, self.top+ TimeList.TIME_Y))  
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+ TimeList.BOX_X, self.top+ TimeList.BOX_Y), (self.left+ TimeList.BOX_X+250, self.top+ TimeList.BOX_Y), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+ TimeList.BOX_X+250, self.top+ TimeList.BOX_Y), (self.left+ TimeList.BOX_X+250, self.top+ TimeList.BOX_Y+300), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+ TimeList.BOX_X+250, self.top+ TimeList.BOX_Y+300), (self.left+ TimeList.BOX_X, self.top+ TimeList.BOX_Y+300), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+ TimeList.BOX_X, self.top+ TimeList.BOX_Y+300), (self.left+ TimeList.BOX_X, self.top+ TimeList.BOX_Y), 2)
        text_surface = font.render("Time", True, (0, 0, 0)) 
        gameContext.screen.blit(text_surface, (self.left+ TimeList.BOX_X+5, self.top+ TimeList.BOX_Y))  
        
        text_surface = font.render("已累積時間", True, (0, 0, 0)) 
        gameContext.screen.blit(text_surface, (self.left+ TimeList.ALLTIME_X, self.top+ TimeList.ALLTIME_Y)) 
       


