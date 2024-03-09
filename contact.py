class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"{self.name} - {self.phone_number} - {self.email}"


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number, email):
        new_contact = Contact(name, phone_number, email)
        self.contacts.append(new_contact)
        print(f"Contact added: {new_contact}")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for contact in self.contacts:
                print(contact)

    def search_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone_number]
        if not found_contacts:
            print("No contacts found.")
        else:
            for contact in found_contacts:
                print(contact)

    def update_contact(self, name, new_phone_number=None, new_email=None):
        contact_to_update = None
        for contact in self.contacts:
            if contact.name == name:
                contact_to_update = contact
                break
        if contact_to_update:
            if new_phone_number:
                contact_to_update.phone_number = new_phone_number
            if new_email:
                contact_to_update.email = new_email
            print(f"Contact updated: {contact_to_update}")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        contact_to_delete = None
        for contact in self.contacts:
            if contact.name == name:
                contact_to_delete = contact
                break
        if contact_to_delete:
            self.contacts.remove(contact_to_delete)
            print(f"Contact deleted: {contact_to_delete}")
        else:
            print("Contact not found.")


contact_manager = ContactManager()

while True:
    print("\nContact Manager")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        contact_manager.add_contact(name, phone_number, email)
    elif choice == 2:
        contact_manager.view_contacts()
    elif choice == 3:
        search_term = input("Enter search term: ")
        contact_manager.search_contact(search_term)
    elif choice == 4:
        name = input("Enter name: ")
        new_phone_number = input("Enter new phone number (leave blank to keep the same): ")
        new_email = input("Enter new email (leave blank to keep the same): ")
        contact_manager.update_contact(name, new_phone_number, new_email)
    elif choice == 5:
        name = input("Enter name: ")
        contact_manager.delete_contact(name)
    elif choice == 6:
        break
    else:
        print("Invalid input. Please enter a number between 1 and 6.")