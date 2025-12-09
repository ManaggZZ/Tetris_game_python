class Colors:
    dark_grey = (26, 31, 40)       # color of empty cell
    green = (47, 230, 23)
    red = (232, 18, 18)
    orange = (226, 116, 17)
    yellow = (237, 234, 4)
    purple = (116, 0, 247)
    cyan = (21, 204, 209)
    blue = (13, 64, 216)
    white = (255, 255, 255)
    dark_blue = (44, 44, 127)
    light_blue = (59, 85, 162)

    @classmethod
    def get_cell_colors(cls):       #! CLS is a reference to the class itself and it allows us to access the class level attributes and methods. It is similar to using self to access instant level attributes and methods but CLS is used for the class level.
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]
        #! we will us ethe index of this list of colors to get the color.
