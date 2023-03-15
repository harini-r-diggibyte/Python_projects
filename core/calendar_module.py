import calendar_module
#user input :date as mm/dd/yyyy
n1, n2, n3 = map(int, input().split())

print((calendar.day_name[calendar.weekday(n3, n1, n2)]).upper())
