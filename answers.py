a = {"привет": "и тебе привет!","как дела": "Лучше всех" , "пока": "Увидимся"}
b = str(input())

c=b.lower()

def get_answer():
	return print (a[c])

get_answer()	
