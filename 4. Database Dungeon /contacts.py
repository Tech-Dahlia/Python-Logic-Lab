"""
Project: Phone Book
Author:  Dahlia Mphalo
Description:  A command-line contact book that stores contacts as a list of dictionaries. 
              Users can add, search, delete, and view contacts through a while-loop menu. 
              Demonstrates lists, dictionaries, functions, loops, and the difference between mutable and immutable data types.
"""

#  ===============
#   DATA STRUCTURE CHEAT SHEET
#   Lists        = [ ]       ordered, changeable (mutable)
#   Dictionaries = { }       key-value pairs, changeable (mutable)
#   Tuples       = ( , )     ordered, unchangeable (immutable).   and The comma is what creates a tuple, not the brackets. edd x(1, 2, 3 )
#  ===============

contacts = [
    {"name": "Alice",   "phone": "123-456-7890", "email": "alice@example.com"},
    {"name": "Bob",     "phone": "987-654-3210", "email": "bob@example.com"},
    {"name": "Charlie", "phone": "555-555-5555", "email": "charlie@example.com"},
]


# A list of dictionaries. Each dictionary is one contact.
# Every contact has exactly three keys: name, phone, email.
contacts = [
    {"name": "Alice",   "phone": "123-456-7890", "email": "alice@example.com"},
    {"name": "Bob",     "phone": "987-654-3210", "email": "bob@example.com"},
    {"name": "Charlie", "phone": "555-555-5555", "email": "charlie@example.com"},
]

# ---------- FUNCTION 1: Add a contact ----------
def add_contact():
    """Ask the user for details, build a dict, append/add it to contacts."""
    name  = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    # Package the three pieces into a single dictionary
    new_contact = {"name": name, "phone": phone, "email": email}

    # .append() adds the dictionary to the END of the list
    contacts.append(new_contact)

    print(f" {name} has been added.")


# ---------- FUNCTION 2: Search a contact by name ----------
def search_contact(name):
    """
    Loop through contacts.
    If a contact's name matches (case-insensitive), return that dict.
    If nothing matches, return None.
    """
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    return None


# ---------- FUNCTION 3: Delete a contact by name ----------
def delete_contact(name):
    """
    Loop through contacts and remove the first match by name.
    We return immediately after removing so we don't modify the
    list while still iterating over it (that causes bugs).
    """
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print(f"  {name} has been deleted.")
            return
    print(f" No contact named {name} was found.")


# ---------- FUNCTION 4: View all contacts ----------
def view_all():
    """Print every contact in a formatted, numbered layout."""
    if not contacts:
        print(" Your contact book is empty.")
        return

    print("\n===== ALL CONTACTS =====")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name:  {contact['name']}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Email: {contact['email']}")
        print("-" * 25)
    print()


# ---------- MAIN MENU LOOP ----------
while True:
    print("===== CONTACT BOOK =====")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. View all contacts")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        name = input("Enter the name to search: ")
        result = search_contact(name)
        if result:
            print(f" Found: {result}")
        else:
            print(f" No contact named {name} was found.")

    elif choice == "3":
        name = input("Enter the name to delete: ")
        delete_contact(name)

    elif choice == "4":
        view_all()

    elif choice == "5":
        print(" Goodbye!")
        break

    else:
        print("1  Invalid option. Please pick 1-5.")
