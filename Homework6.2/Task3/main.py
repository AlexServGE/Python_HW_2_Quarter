import math


def find_farthest_orbit(some_list):
    pi = math.pi
    func_list = list(filter(lambda x: x[0] != x[1], some_list))
    result = list(map(lambda x: x[0] * x[1] * pi, func_list))
    return some_list[result.index(max(result))]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(find_farthest_orbit(orbits))
