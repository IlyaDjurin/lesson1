from datetime import datetime
from datetime import date
from vincenty import vincenty
import csv
import locale
dt_now = datetime.now()
##Создаем словарь с остановками и их геоданными
dct1 = {}
dct = {}  ##Создаем словарь,куда записывается cтанция и и её геоданные
##Открываем архив и приводим его к нужному виду
with open('/home/ilya/Документы/projekts/data-397-2016-11-24.csv', 'r', encoding='utf-8') as f:    
    fields = ["ID","Name","Longitude_WGS84","Latitude_WGS84","NameOfStation",\
    "Line","ModeOnEvenDays","ModeOnOddDays","FullFeaturedBPAAmount",\
    "LittleFunctionalBPAAmount","BPAAmount","RepairOfEscalators",\
    "system_object_id","global_id,geoData"]
    reader = csv.DictReader(f, fields)
    for row in reader:   ##Добалляем станции в список и делаем в словаре соответствие {Станция:[координаты]}
        dct[row["NameOfStation"]]=[row["Longitude_WGS84"],row["Latitude_WGS84"]]
with open('/home/ilya/Документы/projekts/data-398-2016-11-07.csv', 'r', encoding='1251') as f:   
    fields = ["system_object_id","global_id","Name","Longitude_WGS84",\
    "Latitude_WGS84","Street","AdmArea","District","RouteNumbers",\
    "OperatingOrgName","EntryState","Pavilion","Direction","ID","StationName","geoData"]
    reader = csv.DictReader(f, fields, delimiter=';')
    for row in reader:   ####Добалляем станции в список и делаем в словаре соответствие {Улица(остановка):[координаты]}
        dct1[row['Street']]=[row["Longitude_WGS84"],row["Latitude_WGS84"]]
## Удаляем из словарей не нудные значеия
del dct1['Street'] 
del dct["NameOfStation"]        
## Довавляем в список с координатоми значение ноль(для счетчика начальное значение)
for y in list(dct.keys()):
    dct[y].append(float(0))
##Вычисляем разницу между координатами станции и остановками, если расстояние меньше 500 м -прибавляем
## в счетчик 1цу
for y in list(dct.keys()):
    for z in list(dct1.keys()):
        dct[y][0]=float(dct[y][0])        
        dct[y][1]=float(dct[y][1])
        dct1[z][0]=float(dct1[z][0])
        dct1[z][1]=float(dct1[z][1])
        a=(dct[y][0],dct[y][1])
        b=(dct1[z][0],dct1[z][1])
        if float(vincenty(a,b)) <=0.5: ##Специальная функция вычисляет расстояние по координатам
            dct[y][2]= dct[y][2] + 1
b=[]  ## Создаем список максимального числа станций в радиусе 500м и выбираем максимальный элемент
for y in list(dct.keys()):
    b.append(dct[y][2])
b= float(max(b))
print(b)

def get_key(dct, value): ##Создаем функци. которая ищет ключ по значению и выводим ответ на экран
    for k, v in dct.items():
        if v[2] == value:
            return  print("Больше всего остановок в радиусе 500 м возле станции метро ",k,", их аж целых ",value)
get_key(dct,b)          
     