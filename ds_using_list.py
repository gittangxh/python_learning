#This is my shopping list.

shoplist = ['apple', 'mango', 'carrot','banana']

print('I have', len(shoplist), 'items to buy.')

print('These items are: ', end='')
for i in shoplist:
    print(i,end=' ')

print('\nI also have to buy rice.')

shoplist.append('rice')
print('My shoplist is now:',shoplist)

print('I will sort my list now')
shoplist.sort()
print('The sorted list is now:', shoplist)

print('The first item I will buy is:', shoplist[0])
olditem = shoplist[0]

shoplist.pop(0)
print('I have bought:', olditem)

print('The shoplist is now:', shoplist)
