#Date Format 20210913

date_num = 20213433

def BreakUpDate(date):
    y = date // 10000

    date %= 10000

    m = date // 100

    date  %= 100

    d = date


    return y,m,d

def ConvertMonth(m):
    mon = "Jan"

    if m == 2:
        mon = "Feb"    
    elif m == 3:
        mon = "Mar"
    elif m == 4:
        mon = "Apr"
    elif m == 5:
        mon = "May"
    elif m == 6:
        mon = "Jun"
    elif m == 7:
        mon = "Jul"
    elif m == 8:
        mon = "Aug"
    elif m == 9:
        mon = "Sep"
    elif m == 10:
        mon = "Oct"
    elif m == 11:
        mon = "Nov"
    else:
        mon = "Dec"

    return mon



year, month, day = BreakUpDate(date_num)

result = ConvertMonth(month) + ' ' + str(day) + ', ' + str(year)

print(result)

