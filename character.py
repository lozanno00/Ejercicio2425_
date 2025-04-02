class character(entity):
    def __init__(self, x, y, image, lives):
        super().__init__(x, y, image)
        self.lives = lives
        self.is_alive = True

    def shoot(self):
        return Shot(self.x + 20, self.y, RED if isinstance(self, Player) else BLUE)

    def collide(self, shot):
        if self.x < shot.x < self.x + 40 and self.y < shot.y < self.y + 40:
            self.lives -= 1
            if self.lives <= 0:
                self.is_alive = False
            return True
        return False