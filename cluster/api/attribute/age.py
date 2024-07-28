import time


class Age(object):
    def __init__(self):
        self.age = 0
        self.hp = 0
        self.birthdate = ''
        self.dayage = 0

    def age_in(self):
        self.birthdate = input('请输入出生日期')
        self.age = time.localtime()[0] - int(self.birthdate[:4])
        self.dayage = self.dayagecal()

    def dayagecal(self):
        mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        n = int(self.birthdate[:4])
        s = 0
        for i in range(1, self.age):
            if (n + i) % 400 == 0 or ((n + i) % 4 == 0 and (n + i) % 100 != 0):
                mon[1] = 29
            else:
                mon[1] = 28
            for j in mon:
                s += j
        for i in range(0, int(self.birthdate[-4:-2])):
            s += mon[i]
            s += int(self.birthdate[-2:])
        return s

    def hp_out(self):
        self.hp = (80 - self.age)*1000


age = Age()
age.age_in()
age.dayagecal()
print(age.dayage)
