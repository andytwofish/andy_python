import pygame
import math

class GameContext:
    def __init__(self):
        self.screen = None
        pass
        
    def create(self, width:int=800, height:int=600, title:str="" ):
        pygame.init()
        pygame.display.set_caption( title )
        self.screen = pygame.display.set_mode((width, height))  
    
    
class DrawTool:
        
    @staticmethod
    def drawImg( img, x:int, y:int, rotation:int ):
        original_rect = img.get_rect(center=(x, y))
        rotated_image = pygame.transform.rotate(img, -rotation )
        rotated_rect = rotated_image.get_rect(center=original_rect.center)
        gameContext.screen.blit(rotated_image, rotated_rect.topleft)
        
    @staticmethod    
    def get_rotated_rect(img, x, y, rotation):
        original_rect = img.get_rect(center=(x, y))
        rotated_image = pygame.transform.rotate(img, -rotation)
        rotated_rect = rotated_image.get_rect(center=original_rect.center)
        return rotated_rect  # 這個 rect 是實際畫在畫面的位置
        
gameContext = GameContext()
