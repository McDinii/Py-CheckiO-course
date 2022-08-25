def time_converter(time):
    time = time.split(":")
    if int(time[0]) < 12 or int(time[0])==00:
        if int(time[0])==00:
            time = "12" + ":" + time[1] + " a.m."
        else:
            time = str(int(time[0])) + ":"+time[1] + " a.m."
    else:
        if time[0] != "12":
            time = str(int(time[0])-12) +":"+ time[1] +" p.m."
        else:
            time = time[0] +":"+ time[1]+ " p.m."
    return time

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
