import csv
import datetime
from bd import User

posts_list = []
u = User

with open ('blog.csv','r', encoding = 'utf-8') as f:
	fields = ['title','image','published','content','email','first_name','last_name']
	reader = csv.DictReader(f, fields, delimiter=';')
	for row in reader:
		row['published'] = datetime.datetime.strptime(row['published'], '%d.%m.%y %H:%M')
		author = u.query.filter(User.email == row['email']).first()
		row['user_id'] = author.id
		
		posts_list.append(row)
print(posts_list)		


		