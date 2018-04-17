class ShortInputException(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('enter something-->')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except EOFError:
    print('why did you do an EOF on me?')
except ShortInputException as ex:
    print('ShortInputException: The input was {} long, expect at least{}'.format(ex.length,ex.atleast))
else:
    print('you entered:{}'.format(text))
