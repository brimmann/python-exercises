class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def _area(self):
        return self.width * self.height
    area = property(fget = _area)

    def __rep__(self):
        return "Rectangle(%d, %d" % (self.width, self.height)
    
