class Skills(object):
    def __init__(self):
        self.skill = {}

    def add_skill(self, skill_n, skill_d, skill_s):
        self.skill[skill_n] = [skill_d, skill_s]
        # skill_s 技能属性：动，静，琴棋书画？或者是根据技能等级来区分需要的练习时间

    def skill_time(self):
        pass
        #   todo   主要是传参数给mission 并要复习旧有的技能
