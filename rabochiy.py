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


a = 30
e= 31
b= "мне сегодня %s лет"%a
с = "мне сегодня  {} лет, а в следуюхем году {}".format(a,e)
print(с)
k = "мне сегодня  30 лет, а в следуюхем году 31"
sorted(k)
print(k)