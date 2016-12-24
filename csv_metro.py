from datetime import datetime
from datetime import date, timedelta
import csv
import locale
dt_now = datetime.now()
##Создаем список с улицами
lst = []
dct = {}  ##Создаем словарь,куда записывается cтанция и ремонт эска
##Открываем архив и приводим его к нужному виду
with open('/home/ilya/Документы/projekts/data-397-2016-11-24.csv', 'r', encoding='utf-8') as f:    
    fields = ["ID","Name","Longitude_WGS84","Latitude_WGS84","NameOfStation",\
    "Line","ModeOnEvenDays","ModeOnOddDays","FullFeaturedBPAAmount",\
    "LittleFunctionalBPAAmount","BPAAmount","RepairOfEscalators",\
    "system_object_id","global_id,geoData"]
    reader = csv.DictReader(f, fields)
    for row in reader:   ##Добалляем ремонт в список и делаем в словаре соответствие {Станция:ремонт}
        lst.append(row["RepairOfEscalators"])
        dct[row["NameOfStation"]]=row["RepairOfEscalators"]

    for k in list(dct.keys()):  ##Станции где идет ремонт(убираем лишние станции где ремонта нет)
        dct[k]=dct[k].split()
        if len(dct[k]) == 0:
            del dct[k]
    for k in list(dct.keys()):   ##{Станция:[числа когда идут работы]}
        dct[k]=dct[k][4:5]

    for k in list(dct.keys()):  ##  Разбиваем дату на 2 элемента списка
        dct[k]="".join(dct[k])
        dct[k]=dct[k].split("-")

del dct["NameOfStation"] ## Удаляем стандартную станцию без ремонта



for k in list(dct.keys()):
    d1 = datetime.strptime(dct[k][0], '%d.%m.%Y')   ##преобразую строку в дату
    d1=datetime.date(d1) ##Убираем из строки время,отавляем только дату
    dct[k][0]=d1   ##Записываем новое значение в словарь 
    d2 = datetime.strptime(dct[k][1], '%d.%m.%Y')
    d2 = datetime.date(d2)
    dct[k][1]=d2


i= datetime.now()  ##Присваиваем переменно сеодняшнюю
i=datetime.date(i)   ## Удаляем из неё время 
for k in list(dct.keys()): ## Делаем проверку по дате где сейчас идёт ремонт эскалатора
    if dct[k][0] <= i <= dct[k][1]:
        print("Сейчас идет ремонт на станции: ",k)



                 
    
        