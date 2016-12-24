a=[]
with open('referat.txt', 'r', encoding='utf-8') as f:
   for line in f:
 		
        a.append(line)
        ## если тут написать print(line) будет ошибка кодировки 
        ##это бан Винды,на Убунте все работает
c= a[0].split(" ")
d= a[1].split(" ")
e= a[2].split(" ")
g= a[3].split(" ")
h= a[5].split(" ")
i= a[6].split(" ")

z=len(c)+len(d)+len(e)+len(g)+len(h)+len(i)
print(len(d))	

print("В тексте: ",z," слов")    	