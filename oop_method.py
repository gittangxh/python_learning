class Person:
    def __init__(self, name):
        self.name = 'tangxh'
        self.name2= name


    def say_hi(self):
        print('hello world:', self.name, self.name2)

p = Person('wanyw')
p.say_hi()
