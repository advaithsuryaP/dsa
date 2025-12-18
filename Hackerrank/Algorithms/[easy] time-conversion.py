'''
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example:
- s = '12:01:00PM'
- return '12:01:00'
- s = '12:01:00AM'
- return '00:01:00'
- s = '07:05:45PM'
- return '19:05:45'
- s = '07:05:45AM'
- return '07:05:45'
- s = '12:40:22AM'
- return '00:40:22'
'''

def timeConversion(s: str) -> str:
    hours, minutes, seconds = s.split(":")
    am_pm: str = seconds[2:]
    new_hours: str = ""
    new_seconds: str = seconds[:2]
    if(am_pm == 'AM'):
        if(int(hours) == 12):
            new_hours = format((int(hours) - 12), "02d")
        else:
            new_hours = format(int(hours), "02d")
    else: 
        if(int(hours) != 12):          
            new_hours = format((int(hours) + 12), "02d")
        else: 
            new_hours = format(int(hours), "02d") 
    return new_hours+":"+minutes+":"+new_seconds


print(timeConversion("12:01:00PM")) # 12:01:00
print(timeConversion("12:01:00AM")) # 00:01:00
print(timeConversion("07:05:45PM")) # 19:05:45
print(timeConversion("07:05:45AM")) # 07:05:45
print(timeConversion("12:40:22AM")) # 00:40:22

'''
Solution:
The trick is to convert the hours to a 24-hour format and obviously there are two cases to consider.AM and PM with a edge cases to
consider for 12:00:00AM and 12:00:00PM.

The main thing however, is the usage of the format function to convert the hours to a xx:xx:xx format.
The rest is simple, we just need to concatenate the hours, minutes and seconds with the new hours and seconds.
'''