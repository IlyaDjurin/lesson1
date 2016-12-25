import json
import requests

def get_children(url):  ##Создаем функцию
	result = requests.get(url) ## Передаем переменнгой знасение url API
	if result.status_code ==200: ## Делаем проверку что возвращает реквестс
		
		return result.json()	 ## Возвращаем значение в формате json
	else:
		print("Чёт не то")	
	


if __name__ == "__main__":	
	data=get_children("http://api.data.mos.ru/v1/datasets/2009/rows") ## Юрл-апи сайта с данными
	print(data)
