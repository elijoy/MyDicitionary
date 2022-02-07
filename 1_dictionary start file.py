phonebook = {'Chris':'555−1111', 
             'Katie':'555−2222',
             'Joanne':'555−3333'}
'''
print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)
print(type(phonebook))

phone = phonebook['Chris']

print(phone)

print(len(phonebook)) #tells how many elements we have in our phone book

mydictionary = dict(m=8,n=9) #key and value

print(mydictionary)




print()
print('*****  end section 1 ********')
print()







print()
print('*****  start section 2 - search dictionary ********')
print()

name = 'Chris'

if name in phonebook:
    print(phonebook[name])
else:
    print(name, "is not in the phonebook.")







print()
print('*****  end section 2 ********')
print()







print()
print('*****  start section 3 - edit/append dictionary ********')
print()

print(phonebook)

phonebook['chris'] = '555-0123' #Keys are immutable, the value gets updated

phonebook['Chris'] = '555-4444'

print(phonebook)

print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

del phonebook["Chris"]

print(phonebook)




print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys ********')
print() #will use a for loop

for key in phonebook: #key can be called whatever you want so you can write: for k in phonebook, just remember to be consistent
    print(key)
    print(phonebook[key])




print()
print('*****  end section 5 ********')
print()






print()
print('*****  start section 6 - iterate through values  ********')
print()
for value in phonebook.values():
    print(value)



print()
print('*****  end section 6 ********')
print()








print()
print('*****  start section 7 - iterate through both key and value pair********')
print()

for phonebook_tuple in phonebook.items():
    print(phonebook_tuple)

for key,value in phonebook.items():
    print(key)
    print(value)

print()
print('*****  end section 7 ********')
print()


print()
print('*****  start section 8 - using get and clear********')
print()


phone = phonebook.get('Chris','key not found') #get allows you to avoid
print(phone)

phonebook.clear()
print(phonebook) #have an empty dictionary

print()
print('*****  end section 8 ********')
print()



print()
print('*****  start section 9 - using pop method ********')
print()

remove = phonebook.pop('Chris', 'not found')
print(remove)

print(phonebook)


print()
print('*****  end section 9 ********')
print()




print()
print('*****  start section 10 - using popitem ********')
print()
#random part does not work
a = phonebook.popitem()

print(a)
print(phonebook)


print()
print('*****  end section 10 ********')
print()
'''


import random

print()
print('*****  start section 11 - using random and converting to list ********')
print()


#list_of_keys = list(phonebook)
#random_key = random.choice(list_of_keys) #remember to import random at the top
#phone = phonebook[random_key]

#print(phone)

#how to do it in 1 line

phone = phonebook[random.choice(list(phonebook))]
print(phone)

print()
print('*****  end section 11 ********')
print()



