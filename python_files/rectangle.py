class Rectangle:
    def __init__(self,width=0,height=0) -> None:
        self.__width = width
        self.__height =height

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self,value):
        if type(value) != int:
            raise TypeError ("{}must be an integer".format(value))
        elif value < 0:
            raise ValueError("{} must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self,value):
        if type(value) != int:
            raise TypeError ("{}must be an integer".format(value))
        elif value < 0:
            raise ValueError("{} must be >= 0")
        else:
            self.__height = value

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)