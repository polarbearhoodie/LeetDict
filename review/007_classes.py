# here things start to get a bit funky, since I never really bothered 
# with the minutia of classes - 
# especially after Java, with types so strong they strangle you
# I botched an interview after I spent time trying to return a tuple
# and needed to return a custom tuple class 
# and ended up creating a tuple getter, setter, tuple factory 

class PointClass:
    def __init__(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos

    def origin_displacement(self):
        return (self.x**2 + self.y**2)**0.5

point = PointClass(3, 4)
print(str(point.origin_displacement()))
    
