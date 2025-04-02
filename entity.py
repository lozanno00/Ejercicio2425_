class entity:
    def __innit__(self,x,y,image):
        self.x = x
        self.y = y
        self.image = image

        def move(self, dx, dy):
            self.x += dx
            self.y += dy

        def __str__(self):
            return f"Entity at ({self.x}, {self.y}) with image {self.image}"
        
        def get_image(self):
            return self.image
        