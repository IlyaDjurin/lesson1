import requests

def get_weather(url):
	result = requests.get(url)
	if result.status_code ==200:
		return result.json()
	else:
		print("Чёт не то")	
	


if __name__ == "__main__":	
	data=get_weather("http://api.openweathermap.org/data/2.5/weather?id=709717&APPID=3b6ec58c341debf3510765f70980935d&units=metric")
	print(data)
