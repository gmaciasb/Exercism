import random
import string

class Robot:
    names = []
    def __init__(self):

        name_list = [random.choice(string.ascii_letters).upper() for i in range(2)] + [str(random.randint(0,9)) for i in range(3)]
        self.name = ''.join(name_list)
        Robot.names.append(self.name)

    def reset(self):
        self.__init__()
        if Robot.names.count(self.name) > 1:
            self.__init__()

        return self.name
