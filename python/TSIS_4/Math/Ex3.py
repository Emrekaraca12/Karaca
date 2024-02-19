def area_of_polygon(sides, length) -> float:
    from math import tanh
    distance_between_center_and_side = length / (2 * tanh(180/sides))
    perimeter = sides * length
    Area = perimeter * distance_between_center_and_side / 2
    return Area

print(area_of_polygon(4, 25))