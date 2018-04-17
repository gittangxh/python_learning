import pickle

class contact_person:
    number_of_contact = 0
    def __init__(self, name):
        self.name = name
        self.email = 'null@null.com'
        self.phone = 0
        contact_person.number_of_contact += 1

    def add_email(self, email):
        self.email = email
    def add_phone(self, phone_num):
        self.phone = phone_num
    def print_all(self):
        print(self.name, self.phone, self.email)


addressbook={'tangxh':contact_person('tangxh')}

addressfile = 'add_book'

def save():
    f = open(addressfile,'wb')
    pickle.dump(addressbook, f)
    f.close()

def read():
    f = open(addressfile,'rb')
    global addressbook
    addressbook = pickle.load(f)

addressbook['tangxh'].add_email('tangxhmail@gmail.com')
addressbook['tangxh'].add_phone(15999993333)

print(addressbook['tangxh'].name, addressbook['tangxh'].email, addressbook['tangxh'].phone)

print(addressbook['tangxh'].print_all())

print(contact_person.number_of_contact)

addressbook.update(wanyw=contact_person('wanyw'))
addressbook['wanyw'].add_phone(1333443)
addressbook['wanyw'].add_email('dkjk@ls.com')
print(addressbook['wanyw'].print_all())

print(contact_person.number_of_contact)

print('address book before save:',addressbook)
print(addressbook['wanyw'].print_all())
print(addressbook['tangxh'].print_all())
save()
addressbook.clear()

print('address book after clear:', addressbook)

read()
print('address book after re-load:', addressbook)
print(addressbook['wanyw'].print_all())
print(addressbook['tangxh'].print_all())
print('add tangzg')
addressbook.update(tangzg=contact_person('tangzg'))
print('address book after add tzg:', addressbook)

print('saving to hd...')
save()
addressbook.clear()
print('clearing ram')
print('re-load from hd...')
read()
print(addressbook['tangzg'].print_all())
save()


