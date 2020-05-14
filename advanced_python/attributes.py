class color():
    def __init__(self):
        self.red = 100
        self.green = 150
        self.blue = 200

    def retrieve_colors(self):
        print(self.red, self.green, self.blue)

    def __getattr__(self,attr):
        if attr == "rgbcolor":
            return (self.red, self.green, self.blue)
        elif attr == "hexcode":
            return "#{0:02x}{1:02x}{2:02x}".format(self.red, self.green, self.blue)
        else:
            raise AttributeError

    def __setattr__(self,attr,val):
        if attr == "rgbcolor":
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            super().__setattr__(attr,val)

bright = color()
bright.retrieve_colors()
print(bright.rgbcolor)
print(bright.hexcode)

bright.rgbcolor = (10, 20, 50)
print(bright.rgbcolor)
print(bright.hexcode)