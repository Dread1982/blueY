import math


class Line(object):

    '''
    classdocs
    '''

    def __init__(self, fromPoint, toPoint):
        '''
        Constructor
        '''
        self.startPoint = fromPoint
        self.endPoint = toPoint

    def length(self):
        x_diff = self.startPoint.getX() - self.endPoint.getX()
        y_diff = self.startPoint.getY() - self.endPoint.getY()
        return math.sqrt(x_diff * x_diff + y_diff * y_diff)

    def slope(self):
        if self.is_vertical():
            return None
        else:
            run = self.startPoint.getX() - self.endPoint.getX()
            rise = self.startPoint.getY() - self.endPoint.getY()
            return rise / float(run)

    def is_vertical(self):
        return self.startPoint.getX() == self.endPoint.getX()

    def is_horizontal(self):
        return self.startPoint.getY() == self.endPoint.getY()

    def shift(self, x, y):
        self.startPoint.shift(x, y)
        self.endPoint.shift(x, y)

    def get_start_point(self):
        return self.startPoint

    def get_end_point(self):
        return self.endPoint
