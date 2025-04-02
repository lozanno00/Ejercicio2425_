class player(character):
    def __innit__(self,x,y,image)
        super().__innit__(x,y,image, lives=3)
        self.score = 0

        def move(self, dx):
        self.x += dx
        self.x = max(0, min(WIDTH - 40, self.x))