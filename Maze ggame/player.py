import pygame
import random
class Player:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.player_sizex = 10
        self.player_sizey = 16
        self.rect = pygame.Rect(self.x, self.y, self.player_sizex, self.player_sizey)
        self.color = (250, 120, 60)
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 2
        self.walkRight = pygame.image.load('img/kanan.png')
        self.walkLeft = pygame.image.load('img/kiri.png')
        self.walkDown = pygame.image.load('img/depan.png')
        self.walkUp = pygame.image.load('img/belakang.png')

    def get_current_cell(self, x, y, grid_cells):
        for cell in grid_cells:
            if cell.x == x and cell.y == y:
                return cell
            
    def check_move(self, tile, grid_cells, thickness):
        current_cell_x, current_cell_y = self.x // tile, self.y // tile
        current_cell = self.get_current_cell(current_cell_x, current_cell_y, grid_cells)
        current_cell_abs_x, current_cell_abs_y = current_cell_x * tile, current_cell_y * tile
        if self.left_pressed:
            if current_cell.walls['left']:
                if self.x <= current_cell_abs_x + thickness:
                    self.left_pressed = False
        if self.right_pressed:
            if current_cell.walls['right']:
                if self.x >= current_cell_abs_x + tile - (self.player_sizex + thickness):
                    self.right_pressed = False
        if self.up_pressed:
            if current_cell.walls['top']:
                if self.y <= current_cell_abs_y + thickness:
                    self.up_pressed = False
        if self.down_pressed:
            if current_cell.walls['bottom']:
                if self.y >= current_cell_abs_y + tile - (self.player_sizey + thickness):
                    self.down_pressed = False

    #drawing player on the screen
    def draw(self, screen):
        #pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.walkDown,(self.x,self.y))
        
    # updates player position while moving
    def update(self, screen):
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed:
            screen.blit(self.walkLeft,(self.x,self.y))
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            screen.blit(self.walkRight,(self.x,self.y))
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed:
            screen.blit(self.walkUp,(self.x,self.y))
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            screen.blit(self.walkDown,(self.x,self.y))
            self.velY = self.speed
        self.x += self.velX
        self.y += self.velY
        #self.rect = pygame.Rect(int(self.x), int(self.y), self.player_sizex, self.player_sizey)


 
 
class Enemy:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 16
        self.speed = 2
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.left_pressed = True
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.color = (250, 120, 60)
        

    def get_current_cell(self, x, y, grid_cells):
        for cell in grid_cells:
            if cell.x == x and cell.y == y:
                return cell
        
    def draw(self,screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def change_direction(self):
        directions = ['left', 'right', 'up', 'down']
        self.left_pressed = True
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        chosen_direction = random.choice(directions)
        if chosen_direction == 'left':
            self.left_pressed = True
        elif chosen_direction == 'right':
            self.right_pressed = True
        elif chosen_direction == 'up':
            self.up_pressed = True
        elif chosen_direction == 'down':
            self.down_pressed = True

    def check_move(self, tile, grid_cells, thickness):
        current_cell_x, current_cell_y = self.x // tile, self.y // tile
        current_cell = self.get_current_cell(current_cell_x, current_cell_y, grid_cells)
        current_cell_abs_x, current_cell_abs_y = current_cell_x * tile, current_cell_y * tile
        if self.left_pressed:
            if current_cell.walls['left']:
                if self.x <= current_cell_abs_x + thickness:
                    self.down_pressed = True
                    self.left_pressed = False
                    if current_cell.walls['top']:
                        if self.y <= current_cell_abs_y + thickness:
                            self.down_pressed = True
                            self.up_pressed = False
                    if current_cell.walls['bottom']:
                        if self.y >= current_cell_abs_y + tile - (self.height + thickness):
                            self.up_pressed = True
                            self.down_pressed = False
        if self.right_pressed:
            if current_cell.walls['right']:
                if self.x >= current_cell_abs_x + tile - (self.width + thickness):
                    self.up_pressed = True
                    self.right_pressed = False
                    if current_cell.walls['top']:
                        if self.y <= current_cell_abs_y + thickness:
                            self.down_pressed = True
                            self.up_pressed = False
                    if current_cell.walls['bottom']:
                        if self.y >= current_cell_abs_y + tile - (self.height + thickness):
                            self.up_pressed = True
                            self.down_pressed = False
        if self.up_pressed:
            if current_cell.walls['top']:
                if self.y <= current_cell_abs_y + thickness:
                    self.right_pressed = True
                    self.up_pressed = False
                    if current_cell.walls['left']:
                        if self.x <= current_cell_abs_x + thickness:
                            self.right_pressed = True
                            self.up_pressed = False
                    if current_cell.walls['right']:
                        if self.x >= current_cell_abs_x + tile - (self.width + thickness):
                            self.left_pressed = True
                            self.right_pressed = False        
        if self.down_pressed:
            if current_cell.walls['bottom']:
                if self.y >= current_cell_abs_y + tile - (self.height + thickness):
                    self.left_pressed = True
                    self.down_pressed = False
                    if current_cell.walls['left']:
                        if self.x <= current_cell_abs_x + thickness:
                            self.right_pressed = True
                            self.left_pressed = False
                    if current_cell.walls['right']:
                        if self.x >= current_cell_abs_x + tile - (self.width + thickness):
                            self.left_pressed = True
                            self.right_pressed = False
    def move(self):
        self.velX = 0
        self.velY = 0
        if self.left_pressed:
            self.velX = -self.speed
        if self.right_pressed:
            self.velX = self.speed
        if self.up_pressed:
            self.velY = -self.speed
        if self.down_pressed:
            self.velY = self.speed
        self.x += self.velX
        self.y += self.velY
        self.rect = pygame.Rect(int(self.x), int(self.y), self.width, self.height)

