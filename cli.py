from contactbook import Contact, ContactBook

book = ContactBook()
print("Welcome to Contactbook.")

pref = input("What operation would you like to perform? (index, create, view, delete) ")

if pref == 'index':
    for row in book.index():
        print(f"{row[0]}. {row[1]}: {row[2]}")
else:
    print("There are no other features available at this time. Thank you for your patience")
