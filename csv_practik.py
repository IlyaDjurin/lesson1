from answers import answers, get_answer, ask_user, zap
import csv
a=[]
a.append(answers)
print(a)

with open('export.csv', 'w', encoding='utf-8') as f:
    fields = ['привет', 'как дела', 'пока']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for user in a:
    	writer.writerow(user)