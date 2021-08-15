from contactbook import ContactBook

contacts = ContactBook()
print("Welcome to Contactbook.")

while True:
    pref = input("What operation would you like to perform? (index, add, remove) ")

    if pref == "index":
        for number, row in enumerate(contacts.index()):
            print(f"{number} - ID{row[0]}. {row[1]}: {row[2]}")

    elif pref == "add":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")

        contacts.add(name, str(phone))
        print("Contact added")

    elif pref == "remove":
        id_ = input("Enter ID: ")
        contacts.remove(id_)
        print("Contact deleted")

    elif pref == "update":
        id_ = input("Enter ID: ")
        print(contacts.find(id_))
        
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        
        contacts.update(id_, name, phone)

        print("Contact updated")

    else:
        print(
            "There are no other features available at this time. Thank you for your patience"
        )
        exit()
