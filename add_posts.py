import csv
import datetime
from bd import User , db_session, Post

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
for k in posts_list:
	post = Post(k['title'],k['image'],k['published'],k['content'],k['user_id'])
	db_session.add(post)

db_session.commit()
print(posts_list)		


		