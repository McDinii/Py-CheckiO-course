from typing import Tuple


def sum_by_types(items: list) -> tuple[str, int]:
    sum_int=0
    sum_str=""
    for i in items:
        if isinstance(i,int):
            sum_int += i
        else:
            sum_str += i
    return sum_str,sum_int


if __name__ == "__main__":
    print("Example:")
    print(sum_by_types(["size", 12, "in", 45, 0]))
    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_by_types([]) == ("", 0)
    assert sum_by_types([1, 2, 3]) == ("", 6)
    assert sum_by_types(["1", 2, 3]) == ("1", 5)
    assert sum_by_types(["1", "2", 3]) == ("12", 3)
    assert sum_by_types(["1", "2", "3"]) == ("123", 0)
    assert sum_by_types(["size", 12, "in", 45, 0]) == ("sizein", 57)
    print("Coding complete? Click 'Check' to earn cool rewards!")
