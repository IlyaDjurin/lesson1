import csv

with open('data-398-2016-11-07.csv', 'r', encoding='utf-8') as f:
    fields = ['Name', 'Street']
    reader = csv.DictReader(f, fields, delimiter=';')
    for row in reader:
        for i in lst:
        if i in dct:
            dct[i] += 1
        else:
            dct[i] = 1  