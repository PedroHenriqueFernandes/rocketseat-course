from pydantic import BaseModel
from typing import List

class Contact(BaseModel):
    name: str
    phone: str
    email: str
    is_favorite: bool = False

class Contacts:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact: Contact):
        self.contacts.append(contact)

    def edit_contact(self, contact: Contact, new_contact: Contact):
        index = self.contacts.index(contact)
        self.contacts[index] = new_contact

    def mark_as_favorite(self, contact: Contact):
        index = self.contacts.index(contact)
        self.contacts[index].is_favorite = True

    def unmark_as_favorite(self, contact: Contact):
        index = self.contacts.index(contact)
        self.contacts[index].is_favorite = False

    def get_favorite_contacts(self) -> List[Contact]:
        return [contact for contact in self.contacts if contact.is_favorite]

    def delete_contact(self, contact: Contact):
        self.contacts.remove(contact)

    def get_contacts(self) -> List[Contact]:
        return self.contacts

contacts = Contacts()
while True:
    print("1. Add contact")
    print("2. Edit contact")
    print("3. Mark as favorite")
    print("4. Unmark as favorite")
    print("5. List favorite contacts")
    print("6. Delete contact")
    print("7. List contacts")
    print("8. Exit")

    option = input("Choose an option: ")

    if option == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        is_favorite = input("Is favorite? (y/n): ")
        contact = Contact(name=name, phone=phone, email=email, is_favorite=is_favorite == "y")
        contacts.add_contact(contact)
    elif option == "2":
        name = input("Enter name of contact to edit: ")
        contact = next((c for c in contacts.get_contacts() if c.name == name), None)
        if contact:
            new_name = input("Enter new name: ")
            new_phone = input("Enter new phone: ")
            new_email = input("Enter new email: ")
            new_contact = Contact(name=new_name, phone=new_phone, email=new_email, is_favorite=contact.is_favorite)
            contacts.edit_contact(contact, new_contact)
        else:
            print("Contact not found")
    elif option == "3":
        name = input("Enter name of contact to mark as favorite: ")
        contact = next((c for c in contacts.get_contacts() if c.name == name), None)
        if contact:
            contacts.mark_as_favorite(contact)
        else:
            print("Contact not found")
    elif option == "4":
        name = input("Enter name of contact to unmark as favorite: ")
        contact = next((c for c in contacts.get_contacts() if c.name == name), None)
        if contact:
            contacts.unmark_as_favorite(contact)
        else:
            print("Contact not found")
    elif option == "5":
        favorite_contacts = contacts.get_favorite_contacts()
        for contact in favorite_contacts:
            print(contact)
    elif option == "6":
        name = input("Enter name of contact to delete: ")
        contact = next((c for c in contacts.get_contacts() if c.name == name), None)
        if contact:
            contacts.delete_contact(contact)
        else:
            print("Contact not found")
    elif option == "7":
        all_contacts = contacts.get_contacts()
        for contact in all_contacts:
            print(contact)
    elif option == "8":
        break
    else:
        print("Invalid option")
