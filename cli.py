from contactbook import Contact, ContactBook

book = ContactBook()
print("Welcome to Contactbook.")

while True: 
    pref = input("What operation would you like to perform? (index, add, view, delete) ")

    if pref == 'index':
        for row in book.index():
            print(f"{row[0]}. {row[1]}: {row[2]}")

    elif pref == "add":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")

        book.add(name, str(phone))
        print("Contact added")

    else:
        print("There are no other features available at this time. Thank you for your patience")
        exit()
