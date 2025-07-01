 
import pygame
import datetime
import time
from datetime import timedelta
from draw_tool import gameContext

class AgoTime:
    def __init__(self,left,top,strat,stop):  
        self.left = left
        self.top = top
        self.strat = strat
        self.stop = stop
        
    def draw(self):
        strathour = self.strat.hour
        stratminute = self.strat.minute
        stratsecond = self.strat.second
        stophour = self.stop.hour
        stopminute = self.stop.minute
        stopsecond = self.stop.second
        font = pygame.font.SysFont("Microsoft JhengHei", 25)
        text_surface = font.render(str(strathour)+":"+str(stratminute)+" "+str(stratsecond)+"-"+str(stophour)+":"+str(stopminute)+" "+str(stopsecond), True, (0, 0, 0)) 
        gameContext.screen.blit(text_surface, (self.left,self.top))
        