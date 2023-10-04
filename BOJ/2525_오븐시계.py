hour, minute = map(int, input().split())
needTime = int(input())

minute = minute + needTime

#60분 이상이면 minute-60, hour+1
if minute >= 60 :
    while minute >= 60 :
        minute -= 60
        hour += 1

#24시 이상이면 hour-24 (0시 0분 ~ 23시 59분)
if hour >= 24 :
    hour -= 24

print(hour, minute)
