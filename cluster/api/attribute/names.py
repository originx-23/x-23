class Names(object):
    def __init__(self):
        self.name = dict()

    def add_name(self, new_name, new_platform):
        self.name[new_platform] = new_name

    def name_in(self):
        new_name = input('请输入姓名:')
        new_platform = input('请输入平台:')
        self.add_name(new_name, new_platform)
