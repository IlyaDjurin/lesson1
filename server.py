from flask import Flask , abort , request
from req import get_weather
from datetime import datetime
from news_list import all_news
from children_csv_json import get_children

city_id = 709717
apikey = '3b6ec58c341debf3510765f70980935d'

app= Flask(__name__)

@app.route("/")
def index():
	url = "http://api.openweathermap.org/data/2.5/weather?id=%s&APPID=%s&units=metric" % (city_id,apikey)
	weather = get_weather(url)
	date_now=datetime.now().strftime('%d.%m.%Y')
	result = "<p><b>Температура: <b>%s<p>" %weather['main']['temp']
	result += "<p><b>Город: <b>%s<p>" % weather['name']
	result += "<p><b>Дата: <b>%s<p>" % date_now
	return result

@app.route("/news/<int:news_id>")
def news_one(news_id):
	news_to_show = [news for news in all_news if news['id']==news_id]
	if len(news_to_show) == 1:
		result = "<h1>%(title)s<h1><p><i>%(date)s</i></p><p>%(text)s</p>"
		result = result % news_to_show[0]
		return result
	else:
		abort(404)	

@app.route("/news")
def all_the_news():
	for item  in request.args:
		print(item)
		limit = request.args.get('limit','all')
		color = request.args.get('color','black')
	return '<h1 style="color: %s">News: <small>%s</small></h1>' % (color , limit)


@app.route("/name")
def children_in_year():
	url = "http://api.data.mos.ru/v1/datasets/2009/rows"
	children = get_children(url)
	for i in range((len(children))):
		res = "<table>"
		res +=	'<tr>'
		res +=		        '<th> Год </th>'
		res +=		        '<th> Месяц </th>'
		res +=		        '<th> Имя </th>'
		res +=		    '</tr>'
		res +=		    '<tr>'
		res +=		        '<td> %s </td>' % children[i]["Cells"]["Year"]
		res +=		        '<td> %s </td>' % children[i]["Cells"]["Month"]
		res +=		        '<td> %s </td>' % children[i]["Cells"]["Name"]
		res +=		    '</tr>'
		res +=		'</table>'
		return res		

if 	__name__ == "__main__":
	app.run()
