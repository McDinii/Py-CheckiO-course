from typing import Union


def sun_angle(time: str) -> Union[int, str]:
    arr = time.split(":")
    time = int(arr[0])*60 + int(arr[1])
    if 6*60 <= time <= 18*60:
        ang = (time - 6*60)/60*15
        return ang
    else:
        return "I don't see the sun!"


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("01:23"))
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
