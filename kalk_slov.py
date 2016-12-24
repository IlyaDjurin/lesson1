i = input("Водите словами:")
i= i.split(" ")
print(i)
q={'один': "1", 'два': "2", 'три': "3" ,'четыре':"4" , 'пять': "5",\
   'шесть':"6", 'семь': "7", 'восемь': "8", 'девять': "9" , 'ноль': "0",\
   'плюс': "+", 'минус': "-", 'умножить': "*", 'разделить' : "/",\
   'и':"."}
w= []
try:
	if i[0] in q:
		w.append(q[i[0]])

	if i[1] in q:
		w.append(q[i[1]])

	if i[2] in q:
		w.append(q[i[2]])

	if i[3] in q:
		w.append(q[i[3]])

	if i[4] in q:
		w.append(q[i[4]])

	if i[5] in q:
		w.append(q[i[5]])

	if i[6] in q:
		w.append(q[i[6]])

	if i[7] in q:
		w.append(q[i[7]])
except IndexError:		
	print('продолжаем')
print(w)	

if "+" in  w:
    a=w.index("+")
    b=w[0:a]
    s=''
    b=s.join(b)
    z=w[(a+1):]
    z = s.join(z)
    b=float(b)
    z=float(z)
    print(b+z)
    w.clear()        
elif "-" in w:
    a=w.index("-")
    b=w[0:a]
    s=''
    b=s.join(b)
    z=w[(a+1):]
    z = s.join(z)
    b=float(b)
    z=float(z)
    print(b-z)
    w.clear()
elif "*" in w: 
    a=w.index("*")
    b=w[0:a]
    s=''
    b=s.join(b)

    z=w[(a+1):]
    z = s.join(z)
    b=float(b)
    z=float(z)
    print(b*z)
    w.clear()
elif "/" in w:     
    a=w.index("/")
    b=w[0:a]
    s=''
    b=s.join(b)
    z=w[(a+1):]
    z = s.join(z)
    b=float(b)
    z=float(z)
    print(b/z)
    w.clear()
w.clear()            	
print(w)