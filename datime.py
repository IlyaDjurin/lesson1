from datetime import datetime
from datetime import date, timedelta
import locale
locale._setlocale(locale.LC_ALL, "rus_rus")
dt_now = datetime.now()
a=dt_now.strftime('%d.%m.%Y %H:%m')
print(a)
a= dt_now.strftime('%A %d %B %Y')
print(a)
a=dt_now.strftime('%Y-%m-%d')
print("Сегодня: ", a)
delta = timedelta(days=1)
a = dt_now - delta
print("Вчера :",a)
delta = timedelta(days=30)
a = dt_now - delta
print("Месяц назад :",a)
date_string = '01/01/17 12:10:03.234567'
date_dt = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')
print("Преобразовали строку в дату: ",date_dt)

b=[]
k=dt_now.strftime('%Y.%m.%d')
for i in range(6):
	delta = timedelta(days=1)
	c = k - delta
	b.append(c)
print(b)	

