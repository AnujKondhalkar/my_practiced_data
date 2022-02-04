#calendar.weekday(year, month, day)
import calendar
def find_day(STDin):
    days =["Monday", "Tuesday", "Wednesday", "Thursday",
                        "Friday", "Saturday", "Sunday"]
    a=[int(x) for x in STDin]
    #08 05 2015 : MM DD YYYY in STDin
    a=calendar.weekday(a[2],a[0],a[1])
    return days[a]

if __name__ == '__main__':
    STDin=input().split(' ')
    print(find_day(STDin).upper())
