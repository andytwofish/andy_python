
import pygame
from draw_tool import gameContext

class TimeList:
    def __init__(self,left,top):
        self.left = left
        self.top = top
        self.BookStartX = 10 
        self.BookStartY = 200  
        self.BookTimeX = 300 
        self.BookTimeY = 40
        self.BookBoxX = 100 
        self.BookBoxY = 150
        self.BookAllTimeX = 100 
        self.BookAllTimeY = 50        

    def mainLoop(self):
        font = pygame.font.SysFont("Microsoft JhengHei", 25)
        #直線
        
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+self.BookStartX, self.top+self.BookStartY), (self.left+self.BookStartX+60, self.top+self.BookStartY), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+self.BookStartX+60, self.top+self.BookStartY), (self.left+self.BookStartX+60, self.top+self.BookStartY+100), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+self.BookStartX+60, self.top+self.BookStartY+100), (self.left+self.BookStartX, self.top+self.BookStartY+100), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+self.BookStartX, self.top+self.BookStartY+100), (self.left+self.BookStartX, self.top+self.BookStartY), 2)
        text_surface = font.render("Start", True, (0, 0, 0)) 
        gameContext.screen.blit(text_surface, (self.left+self.BookStartX+5, self.top+self.BookStartY))  
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+self.BookTimeX, self.top+self.BookTimeY), (self.left+self.BookTimeX+80, self.top+self.BookTimeY), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+self.BookTimeX+80, self.top+self.BookTimeY), (self.left+self.BookTimeX+80, self.top+self.BookTimeY+40), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+self.BookTimeX+80, self.top+self.BookTimeY+40), (self.left+self.BookTimeX, self.top+self.BookTimeY+40), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+self.BookTimeX, self.top+self.BookTimeY+40), (self.left+self.BookTimeX, self.top+self.BookTimeY), 2)
        text_surface = font.render("Time", True, (0, 0, 0)) 
        gameContext.screen.blit(text_surface, (self.left+self.BookTimeX+5, self.top+self.BookTimeY))  
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+self.BookBoxX, self.top+self.BookBoxY), (self.left+self.BookBoxX+250, self.top+self.BookBoxY), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+self.BookBoxX+250, self.top+self.BookBoxY), (self.left+self.BookBoxX+250, self.top+self.BookBoxY+300), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+self.BookBoxX+250, self.top+self.BookBoxY+300), (self.left+self.BookBoxX, self.top+self.BookBoxY+300), 2)
        pygame.draw.line(gameContext.screen, (0, 0, 0), (self.left+self.BookBoxX, self.top+self.BookBoxY+300), (self.left+self.BookBoxX, self.top+self.BookBoxY), 2)
        text_surface = font.render("Time", True, (0, 0, 0)) 
        gameContext.screen.blit(text_surface, (self.left+self.BookBoxX+5, self.top+self.BookBoxY))  
        
        text_surface = font.render("已累積時間", True, (0, 0, 0)) 
        gameContext.screen.blit(text_surface, (self.left+self.BookAllTimeX, self.top+self.BookAllTimeY))  
       


