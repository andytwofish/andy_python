import math 
import pygame
from draw_tool import gameContext


class Class2D:
    def __init__(self, width:int=10, height:int=10 ):
        self.width:int = width
        self.height:int = height
        self.update_pose(0, 0, 0)
        
    def update_pose( self, x:int, y:int, rotation:int ):
        self.x = x
        self.y = y
        self.rotation = rotation
    
    def forward(self, distance=1):
        rad = math.radians(self.rotation)
        x = self.x + distance * math.sin(rad)
        y = self.y - distance * math.cos(rad)
        self.update_pose(x, y, self.rotation )
        
class Image2D(Class2D):
    def __init__(self, img, width:int=10, height:int=10 ):
        super.__init__( width, height )
        self.img = img 
        
    def update_pose( self, x:int, y:int, rotation:int ):
        super().update_pose(x, y, rotation)
        self.original_rect = self.img.get_rect(center=(self.x, self.y))
        self.rotated_image = pygame.transform.rotate(self.img, -rotation)
        self.rotated_rect = self.rotated_image.get_rect(center=self.original_rect.center)
        
    def draw(self):
        gameContext.screen.blit(self.rotated_image, self.rotated_rect.topleft)
        
    def colliderect( self, otherImage2D):
        return self.rotated_rect.colliderect(otherImage2D.rotated_rect)