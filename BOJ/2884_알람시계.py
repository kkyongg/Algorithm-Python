# 0시 0분 ~ 23시 59분까지
hour, minute = map(int, input().split())

if (minute < 45):
    if (hour == 0):
        print(23, 60-(45-minute))
    else:
        print(hour-1, 60-(45-minute))
else:
    print(hour, minute-45)