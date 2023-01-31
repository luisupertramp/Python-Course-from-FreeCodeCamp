class Rectangle :

    def __init__(self, width, height) :
        self.width = width
        self.height = height

    def __str__(self) :
        shapeName = self.__class__.__name__
        return shapeName + '(width=' + str(self.width) + ', height=' + str(self.height) + ')'

    def set_width(self, newWidth) : 
        self.width = newWidth

    def set_height(self, newHeight) :
        self.height = newHeight

    def get_area(self) :
        return self.width * self.height

    def get_perimeter(self) :
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self) :
        return ((self.width ** 2 + self.height ** 2) ** .5)
    
    def get_picture(self) :
        picture = ''
        if self.width < 50 and self.height < 50 :
            for i in range(self.height) :
                picture += self.width * '*' + ('\n' if i < self.height else '')    
        else: 
            picture = "Too big for picture"

        return picture

    def get_amount_inside(self, newShape) :
        if newShape.width <= self.width and newShape.height <= self.height :
            timesWidth = divmod(self.width/newShape.width, 1)
            timesHeight = divmod(self.height/newShape.height, 1)
            return int(timesWidth[0]) * int(timesHeight[0])
        else : 
            return 0


class Square(Rectangle) :
    
    def __init__(self, side) :
        self.width = side
        self.height = side

    def __str__(self) :
        shapeName = self.__class__.__name__
        return shapeName + '(side=' + str(self.width) + ')'

    def set_side(self, side) : 
        super().set_height(side)
        super().set_width(side)

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)

print(rect.get_amount_inside(sq))