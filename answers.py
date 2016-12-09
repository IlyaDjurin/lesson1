answers = {
"привет": "И тебе привет!",
"как дела": "Лучше всех" , 
"пока": "Увидимся"}



def get_answer(questions,answers):
	return answers.get(questions,"не знаю ответ на это сообщение")

def ask_user(answer):
	while True:
		user_input = input("Скажи ченибудь: ")
		user_input=user_input.lower()
		answer = get_answer(user_input,answers)
		print(answer)

		if	user_input == "пока":
			break


def zap():

	try:			
		 return ask_user(answers)
	except KeyboardInterrupt:
		return print("ну все значит")	

if __name__== " __main__":
	zap()

