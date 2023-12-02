class PathLines:
    def __init__(self, *args):
        self.lineList = [x for x in args]

    def get_path(self):
        return self.lineList

    def get_length(self):
        lineLength = 0
        currentCoord_x = 0
        currentCoord_y = 0
        for line in self.lineList:
            lineLength += ((line.x - currentCoord_x)**2 + (line.y - currentCoord_y)**2)**0.5
            currentCoord_x = line.x
            currentCoord_y = line.y
        return lineLength

    def add_line(self, line):
        self.lineList.append(line)


class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = PathLines(LineTo(10, 20), LineTo(10, 30))
p.add_line(LineTo(20, -10))
print(p.get_length())