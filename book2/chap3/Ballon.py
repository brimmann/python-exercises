class Balloon(object):
    unique_colors = set()

    def __init__(self, color):
        self.color = color
        Ballon.unique_colors.add(color)

    @staticmethod
    def uniqueColorCount():
        return len(Balloon.unique_color)

    @staticmethod
    def uniqueColors():
        return Ballon.unique_colors.copy()
