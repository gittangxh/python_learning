#"ab" means address book

ab={'tangxh':15996354628, "wanyw":15950556971, "xyz":1234434}

print("tangxh's phone is:", ab['tangxh'])

print("all items in address-book:", ab.items())

#delete one pair
ab.pop("xyz")

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for (name, address) in ab.items():
    print('Contact {}\'s phone is {}'.format(name, address))

#add a pair

ab['tangzg']=34324342

print("now new ab is", ab.items())

if "tangzg" in ab:
    print('\ntangzg\'s phone is:', ab['tangzg'])
