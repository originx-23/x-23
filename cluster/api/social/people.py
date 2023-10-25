import time

class Social(object):
    def __init__(self):
        with open('name_list', 'rb+', encoding='GBK') as f:
            self.name_list = f.read().splitlines()
            self.day_s = time.localtime()[-2]
            self.day_n = self.day_s
            # todo 创建每个人的分别的好感度

    def consume(self):
        self.day_n = time.localtime()[-2]
        self.dat_n - self.day_s
        # todo 设置好感度按照时间衰减，

    def repair(self):
        pass
        # todo 通过行为来提升

    def alarm(self):
        pass
        # todo 对好感度过低的做出提醒，或者更改分级
