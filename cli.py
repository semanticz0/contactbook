from contactbook import ContactBook

book = ContactBook()
print("Welcome to Contactbook.")

while True:
    pref = input("What operation would you like to perform? (index, add, remove) ")

    if pref == "index":
        for number, row in enumerate(book.index()):
            print(f"{number} - ID{row[0]}. {row[1]}: {row[2]}")

    elif pref == "add":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")

        book.add(name, str(phone))
        print("Contact added")

    elif pref == "remove":
        id_ = input("Enter ID: ")
        book.remove(id_)
        print("Contact deleted")

    else:
        print(
            "There are no other features available at this time. Thank you for your patience"
        )
        exit()
