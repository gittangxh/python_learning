#我会推荐你总是使用括号
#来指明元组的开始与结束
#尽管括号是一个可选选项

zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))

new_zoo = ('monkey', 'camel', zoo)

print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals bought from old zoo are', new_zoo[2])
print('Last animal bought from old zoo is', new_zoo[2][2])
#
print('Number of animals in the new zoo is', len(new_zoo)-1+len(zoo))
