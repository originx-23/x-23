class Property(object):
    def __init__(self):
        self.property = {}

    def add_str(self, property_n, property_d):
        if property_d < 10:
            self.property[property_n] = [property_d, '温饱不愁']
            # TODO 金钱评价体系

    def account(self):
        pass
        # todo 记账体系