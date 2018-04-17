#coding=UTF-8


class Robot:
    ''' a robot with name'''
    #one class variable, used to counter the robots quantity
    poputation = 0
    def __init__(self, name):
        '''initialize an object'''
        Robot.poputation += 1
        self.name = name
        print('(initializing {})'.format(self.name))

    def die(self):
        '''kill one robot'''
        print('{} is being destroyed'.format(self.name))
        Robot.poputation -=1
        if Robot.poputation == 0:
            print('{} is the last robot!'.format(self.name))
        else:
            print('There are still {} robots working'.format(Robot.poputation))
        del self

    def say_hi(self):
        print('This is {}'.format(self.name))
    @classmethod
    def how_many(cls):
        print('There are totally {} robots'.format(Robot.poputation))

Robot.how_many()

droid1 = Robot('droid1')
droid2 = Robot('droid2')

droid1.say_hi()
droid2.say_hi()
Robot.how_many()

droid1.die()
Robot.how_many()

print(Robot.__doc__)
print(Robot.die.__doc__)

