from mymodule import say_hi, __version__

say_hi()


print(__version__)

print(say_hi.__doc__)

print(dir(say_hi))

a=5
print(dir())
del a
print(dir())
