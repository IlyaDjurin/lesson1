import csv
##Создаем список с улицами
lst = []
dct = {}  ##Создаем словарь,куда записывается сколько раз упоминается улица в таблице

with open('data-398-2016-11-07.csv', 'r', encoding='1251') as f:    ##Открываем архиви приводим его к нужному виду
    fields = ["system_object_id","global_id","Name","Longitude_WGS84",\
    "Latitude_WGS84","Street","AdmArea","District","RouteNumbers",\
    "OperatingOrgName","EntryState","Pavilion","Direction","ID","StationName","geoData"]
    reader = csv.DictReader(f, fields, delimiter=';')
    for row in reader:   ##Добалляем улицы в список и присваиваем кадому упоминанию об улице в словаре единицу
    	lst.append(row['Street'])
    	dct[row['Street']]=1

    for i in lst: ##Проверяем кол-во вхождений улиц в списке и если их больше 1го-увеличиваем значение в словаре на 1
    	if i in lst:
    		dct[i]+=1

##Приводим значения словаря к списку
a=dct.values()
a= list(a)
a.remove(max(a)) ##Убираем первый максимальный элемент потому что в данном случае это "остсутствие улицы"
b=max(a) 
def get_key(dct, value): ##Создаем функци. которая ищет ключ по значению и выводим ответ на экран
    for k, v in dct.items():
        if v == value:
            return  print("Больше всего остановок на :",k)
get_key(dct,b)          
    
        