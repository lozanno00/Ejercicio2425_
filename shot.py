class shot(entity):
    def __init__(self,x,y,color):
        super().__init__(x,y,color)
        self.color = color

    def move(self):
        self.y -= 5 if self.color == RED else -5

    def draw(self,screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 5, 10))