import math 
import pygame
from draw_tool import gameContext


class Class2D:
    def __init__(self, x:int=0, y:int=0, width:int=10, height:int=10, rotation:int=0 ):
        self.x:int = x
        self.y:int = y
        self.rotation:int = rotation
        self.width:int = width
        self.height:int = height
    
    def forward(self, distance=1):
        rad = math.radians(self.rotation)
        self.x += distance * math.sin(rad)
        self.y -= distance * math.cos(rad)
        
