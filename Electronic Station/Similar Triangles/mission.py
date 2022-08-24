from typing import List, Tuple

Coords = List[Tuple[int, int]]


def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:
    t_1 = []
    t_2 = []
    d_1, d_2 = [], []
    for i in coords_1:
        t_1.append([i[0], i[1]])
    for i in coords_2:
        t_2.append([i[0], i[1]])
    for i in [t_1, t_2]:
        if i is t_1:
            d_1.append(round(((i[0][0] - i[1][0]) ** 2 + (i[0][1] - i[1][1]) ** 2) ** 0.5,5))
            d_1.append(round(((i[0][0] - i[2][0]) ** 2 + (i[0][1] - i[2][1]) ** 2) ** 0.5,5))
            d_1.append(round(((i[1][0] - i[2][0]) ** 2 + (i[1][1] - i[2][1]) ** 2) ** 0.5,5))
        else:
            d_2.append(round(((i[0][0] - i[1][0]) ** 2 + (i[0][1] - i[1][1]) ** 2) ** 0.5,5))
            d_2.append(round(((i[0][0] - i[2][0]) ** 2 + (i[0][1] - i[2][1]) ** 2) ** 0.5,5))
            d_2.append(round(((i[1][0] - i[2][0]) ** 2 + (i[1][1] - i[2][1]) ** 2) ** 0.5,5))
    d_1.sort(),d_2.sort()
    print(d_1,d_2)
    for i in range(1,len(d_1)):
        if round(d_1[i]/d_2[i],3) != round(d_1[0]/d_2[0],3):
            return False
    return True


if __name__ == '__main__':
    print("Example:")
    print(similar_triangles([(-5, 0), (-1, -1), (1, 4)], [(2, -9), (-10, 9), (5, 3)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
    assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
    assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
    assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'
    print("Coding complete? Click 'Check' to earn cool rewards!")
