print('simple assignment')

shoplist=['apple', 'mango', 'carrot', 'banana']

#mylist is only another name refer to shoplist
mylist= shoplist

del shoplist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)


shoplist=['apple', 'mango', 'carrot', 'banana']
print('copy by making a full slice')
mylist=shoplist[:]
del shoplist[0]
print('shoplist is', shoplist)
print('mylist is', mylist)
