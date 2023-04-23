#
# Каждый третий четверг каждого месяца билеты в Эрмитаж бесплатны. Напечатайте список дат в 2023 году, когда вход бесплатен.
import calendar

a = [str(calendar.monthcalendar(2023, j)[3][3]) + "." + str(j) + ".2023" if calendar.monthcalendar(2023, j)[0][3] == 0 else str(calendar.monthcalendar(2023, j)[2][3]) + "." + str(j) + ".2023" for j in range(1, 13)]

print(a)
