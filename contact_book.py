import os
# File to store contacts
FILE_NAME = 'contacts.txt'
def load_contacts():
    """Load contacts from the file."""
    contacts = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            lines = file.readlines()
            for line in lines:
                name, phone, category = line.strip().split(',')
                contacts[name] = (phone, category)
    return contacts
def save_contacts(contacts):
    """Save contacts to the file."""
    with open(FILE_NAME, 'w') as file:
        for name, (phone, category) in contacts.items():
            file.write(f"{name},{phone},{category}\n")
def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter contact name: ").strip()
    phone = input("Enter contact phone: ").strip()
    category = input("Enter contact category (e.g., Personal, Work): ").strip()
    contacts[name] = (phone, category)
    print("Contact added successfully!")
def view_contacts(contacts):
    """View all contacts."""
    if not contacts:
        print("No contacts available.")
        return
    for name, (phone, category) in contacts.items():
        print(f"Name: {name}, Phone: {phone}, Category: {category}")
def update_contact(contacts):
    """Update an existing contact."""
    name = input("Enter contact name to update: ").strip()
    if name in contacts:
        phone = input("Enter new phone number: ").strip()
        category = input("Enter new contact category (e.g., Personal, Work): ").strip()
        contacts[name] = (phone, category)
        print("Contact updated successfully!")
    else:
        print("Contact not found.")
def delete_contact(contacts):
    """Delete a contact."""
    name = input("Enter contact name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")
def main():
    """Main function to run the contact book application."""
    contacts = load_contacts()
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            save_contacts(contacts)
            print("Saved!!!!!!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
if __name__ == "__main__":
    main()
