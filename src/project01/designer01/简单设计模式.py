
"""
简单工厂模式

"""

class Operation(object):

    @property
    def numer_a(self):
        return self.__number_a

    @numer_a.setter
    def number_a(self, value):
        self.__number_a = value

    @property
    def number_b(self):
        return self.__number_b

    @number_b.setter
    def number_b(self, value):
        self.__number_b = value


class OperationAdd(Operation):
    def get_result(self):
        return self.number_a + self.number_b


class OperationSub(Operation):
    def get_result(self):
        return self.number_a - self.number_b


class OperationFactory(object):
    @staticmethod
    def create_operation(operate):
        if operate == "+":
            return OperationAdd()
        elif operate == "-":
            return OperationSub()


if __name__ == '__main__':
    op = OperationFactory.create_operation('-')
    op.number_a = 10
    op.number_b = 5

    print(op.get_result())
