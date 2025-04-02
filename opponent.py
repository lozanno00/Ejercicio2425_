class Opponent(Character):
    def __init__(self, x, y, image):
        super().__init__(x, y, image, lives=1)
        self.is_star = False

    def move(self):
        self.y += 2
        if self.y > HEIGHT:
            self.y = 0
            self.x = random.randint(0, WIDTH - 40)