# https://www.codingame.com/ide/puzzle/how-time-flies
from datetime import datetime
from dateutil import relativedelta

begin = datetime.strptime(input(), '%d.%m.%Y')
end = datetime.strptime(input(), '%d.%m.%Y')
duration = end - begin
r = relativedelta.relativedelta(end, begin)

res = ""

if r.years == 1:
    res += str(r.years) + " year, "
elif r.years > 1:
    res += str(r.years) + " years, "

if r.months == 1:
    res += str(r.months) + " month, "
elif r.months > 1:
    res += str(r.months) + " months, "

res += "total " + str(duration.days) + " days"

print(res)
