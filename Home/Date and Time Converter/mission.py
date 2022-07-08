def date_time(time: str) -> str:
    mon = [' January', ' February', ' March', ' April', ' May', ' June', ' July', ' August', ' September', ' October', ' November',
     ' December']
    time = time.split()
    day = int(time[0][:2])
    month = mon[int(time[0][3:5])- 1]
    year = time[0][6:] + ' year'
    hours = str(int(time[1][:2])) + " hour" if time[1][:2] == "01" else str(int(time[1][:2])) + " hours"
    minutes = str(int(time[1][3:])) + " minute" if time[1][3:] == "01" else str(int(time[1][3:])) + " minutes"
    return str(day) + month + " "+ year +" " + hours + " "  + minutes


if __name__ == "__main__":
    print("Example:")
    print(date_time("01.01.2000 00:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert (
        date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
    ), "Millenium"
    assert (
        date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes"
    ), "Victory"
    assert (
        date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes"
    ), "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
