# Parse user input
def parse_input(user_input):
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, args
    except ValueError:
        return "", []

# Add a contact 
def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command. Expected input: add [name] [phone]"
    
    name, phone = args
    contacts[name] = phone
    return "Contact added."

#Update a contact
def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command. Expected input: add [name] [phone]"
    
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Name not found."

# Get a contact
def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid command. Expected input: phone [name]"
        
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Name not found."

# List contacts
def show_all(contacts):
    if not contacts:
        return "No contacts saved."
        
    result = "All contacts:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()

# Start bot
def main():
    contacts = {} 
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()