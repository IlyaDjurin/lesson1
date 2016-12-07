answers = {
"привет": "и тебе привет!",
"как дела": "Лучше всех" , 
"пока": "Увидимся"}



def get_answer(questions,answers):
	return answers.get(questions)

def ask_user(answer):
	while True:
		user_input = input("СКажи ченибудь: ")
		answer = get_answer(user_input,answers)
		print(answer)

		if	user_input == "пока":
			break
def zap():

	try:			
		 return ask_user(answers)
	except KeyboardInterrupt:
		return print("ну все значит")	
zap()				