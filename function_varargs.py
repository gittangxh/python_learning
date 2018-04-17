def total(a=5, *numbers, **phonebook):
    print('a is', a)
    for single_item in numbers:
        print(single_item)
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)
    pass



print(total(5,1,2,3,tangxh=15996354628,wanyw=15950556971))
