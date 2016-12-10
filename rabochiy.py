class Information:
    def __init__(self, info):
        self.info = info

    def extract(self, i):
        self.current = self.info[i]
        return "%s" % self.current

class Teacher:
    def into(self, phrase):
        self.phrase = phrase

    def out(self):
        return "%s" % self.phrase

class Pupil:
    def __init__(self):
        self.know = []

    def take(self, i):
        self.know.append(i)

def test_fink():

    ### запхал все это дело в функцию что бы свернуть и работать с другими операциями

    inform = Information(["> (больше)","< (меньше)","== (равно)", "!= (не равно)"])
    t = Teacher()
    p1 = Pupil()
    p2 = Pupil()

    t.into(inform.extract(2))
    p1.take(t.out())
    print("1-ый ученик пока еще знает только ", p1.know)

    t.into(inform.extract(0))
    p1.take(t.out())
    p2.take(t.out())
    print("1-ый ученик знает, что ", p1.know)
    print("2-ой ученик знает, что ", p2.know)

    i=Information(["матюки","слова","выражения"])
    p3=Pupil()
    p4=Pupil()

    t.into(i.extract(0))
    p3.take(t.out())
    print("3й ученик негодяй и знает только",p3.know)

    t.into(i.extract(1))
    p3.take(t.out())
    p4.take(t.out())
    print("3-ый ученик знает, уже ", p3.know)
    print("4-ой ученик знает, уже ", p4.know)

    p5=Pupil()
    p5.take(i.info)
    for i in p5.know[0]:
        print(i)

a = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
def find_person():
    for i in a:
        print(i)
        if i == "Валера":
            print("Валера нашелся")
            break

def ask():
    while True:
        i=input("как дела?")
        if i != "Хорошо":
            print(i)
        else:
            print("Хорошо")
            break

answers = {
"привет": "И тебе привет!",
"как дела": "Лучше всех" ,
"пока": "Увидимся"}


def get_answer(questions,answers):
	return answers.get(questions,"не знаю ответ на это сообщение")

def ask_user(answer):
	while True:
		user_input = input("СКажи ченибудь: ")
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

def wordcount_user(bot, update):
    b = update.message.text
    b=b.strip()
    print(b)
    b=b.split('"')
    print(b)
    c=b.pop(0)
    c= b.pop(-1)
    print(b)
    e = b[0].split(" ")
    print(e)
    r = len(e)
    print(r)
    if len(b[0])== 0:
        bot.sendMessage(update.message.chat_id,  text=" нет слов ")

    else:
        bot.sendMessage(update.message.chat_id,  text= str(r) + " слова")


