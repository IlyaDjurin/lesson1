def fu():
	i = input("введите выражение (символы через пробел) и напишите в конце знак = :")
	i= i.strip()
	if "=" in i: 
		if " " in i:
			i= i.split(" ")
			print(i)
			
			
			i.pop()
			print(i)
			a=float(i[0])
			b=float(i[2])
			t= i.pop(1)
			if t == "+":
				print(a+b)
			elif t == "-":
				print(a-b)
			elif t == "/":
				print(a/b)
			elif t == "*":
				print(a*b)
			else:
				print("этот знак в разработке")	
		else:
			print("возможно вы что то не правильно ввели, забыли пробел между символами или ещё что-то")	
	else:
		print("вы забыли знак = ")

def kalk():
	try:
		return fu()
	except (ZeroDivisionError , ValueError, TypeError, IndexError):
		return print("вы забыли ввести значение или поделили на 0 !")	

if __name__ == "__main__":
	kalk()

