class Shape:
    class Square:
        def __init__(self, length) -> None:
            self.length = length

        def area(self) -> int:
            shapes_area = self.length * self.length
            print(shapes_area)
    
    def area(self) -> int:
        shapes_area = 0
        print(shapes_area)