from tkinter import *
from class1 import *
# "vknn ongl tfdt vuct"

archieve = load_archieve("archieve.txt")

box = Tk()
box.title("Contact Archive")
box.geometry("1000x600")
box.configure(bg="lightgrey")
box.resizable(True, True)
box.iconbitmap("mask.ico")

print_to_output("Welcome to phones numbers and emails archive")
print_to_output("_" * 40)
current_action = {"type": None, "data": []}

main_frame = Frame(box, bg="lightgrey")
main_frame.pack(fill=BOTH, expand=True)

left_frame = Frame(main_frame, bg="lightgrey")
left_frame.pack(side=LEFT, fill=Y, padx=10, pady=10)

right_frame = Frame(main_frame, bg="lightgrey")
right_frame.pack(side=RIGHT, fill=BOTH, expand=True, padx=10, pady=10)

output_box = Text(right_frame, height=25, font=("Courier", 12), wrap=WORD, bg="white")
output_box.pack(pady=10, fill=BOTH, expand=True)



def print_to_output(text):
    output_box.insert(END, text + "\n")
    output_box.see(END)

set_output_widget(output_box)

entering = Entry(right_frame, width=50, font=("Courier", 14), bg="white")
entering.pack(side=BOTTOM, pady=10)

def send_email():
    """Starts the email sending process"""
    print_to_output("Enter recipient email:")
    current_action["type"] = "send_email"
    current_action["data"] = []
    current_action["stage"] = "recipient"

def share_email():
    """Handles the share contact email logic"""
    print_to_output("Enter recipient email:")
    current_action["type"] = "share_email"
    current_action["data"] = []
    current_action["stage"] = "recipient"

def handle_input(event=None):
    text = entering.get().strip()
    entering.delete(0, END)
    if not text:
        return
    action = current_action["type"]
    data = current_action["data"]

    if action == "add":
        data.append(text)
        prompts = ["Enter number:", "Enter email:"]
        if len(data) < 3:
            print_to_output(prompts[len(data) - 1])
        if len(data) == 3:
            result = add_contact(archieve, *data)
            print_to_output(result)
            current_action["type"] = None
            current_action["data"] = []
    elif action == "search":
        result = search_contact(archieve, text)
        print_to_output(result)
        current_action["type"] = None
    elif action == "delete":
        result = delete_contact(archieve, text)
        print_to_output(result)
        current_action["type"] = None
    elif action == "change":
        data.append(text)
        prompts = ["Enter new name:", "Enter new number:", "Enter new email:"]
        if len(data) < 4:
            print_to_output(prompts[len(data) - 1])
        if len(data) == 4:
            result = change_contact(archieve, *data)
            print_to_output(result)
            current_action["type"] = None
            current_action["data"] = []
    elif action == "send_email":
        data.append(text)
        if len(data) == 1:
            print_to_output("Enter your email password:")
        elif len(data) == 2:
            result = handle_email_sending(archieve, data[0], data[1])
            print_to_output(result)
            current_action["type"] = None
            current_action["data"] = []
    elif action == "share_email":
        data.append(text)
        if len(data) == 1:
            print_to_output("Enter your email password:")
        elif len(data) == 2:
            result = share_contact_by_email(archieve, data[0], data[1])
            print_to_output(result)
            current_action["type"] = None
            current_action["data"] = []

    else:
        print_to_output("Error")

entering.bind("<Return>", handle_input)

Button(left_frame, text="Add Contact", command=lambda: start_action("add", "Enter name:")).pack(fill=X, pady=2)
Button(left_frame, text="Change Contact", command=lambda: start_action("change", "Enter existing name to change:")).pack(fill=X, pady=2)
Button(left_frame, text="Search Contact", command=lambda: start_action("search", "Enter name, number or email:")).pack(fill=X, pady=2)
Button(left_frame, text="Delete Contact", command=lambda: start_action("delete", "Enter name to delete:")).pack(fill=X, pady=2)
Button(left_frame, text="Show Archive", command=lambda: show_archieve(archieve)).pack(fill=X, pady=2)
Button(left_frame, text="Sort Archive", command=lambda: sort_archieve(archieve)).pack(fill=X, pady=2)
Button(left_frame, text="Send Email", command=send_email).pack(fill=X, pady=2)
Button(left_frame, text="Share Contact", command=share_email).pack(fill=X, pady=2)
Button(left_frame, text="Backup Archive", command=backup_archieve).pack(fill=X, pady=2)
Button(left_frame, text="Delete Archive", command=delete_archieve_file).pack(fill=X, pady=2)
Button(left_frame, text="Save Changes", command=lambda: save_archieve(archieve, "archieve.txt")).pack(fill=X, pady=2)
Button(left_frame, text="Clear Screen", command=lambda: output_box.delete(1.0, END)).pack(fill=X, pady=2)
Button(left_frame, text="Exit", command=box.quit).pack(fill=X, pady=2)

def start_action(action_type, prompt):
    current_action["type"] = action_type
    current_action["data"] = []
    print_to_output(prompt)

box.mainloop()



# while True:
#     print("_" * 20)
#     print("Options:")
#     print("1. Add new contact")
#     print("2. Change contact")
#     print("3. Search contact")
#     print("4. Delete contact")
#     print("5. Show archieve")
#     print("6. Show archieve by name")
#     print("7. Send Email")
#     print("8. SAVE CHANGES")
#     print("9. EXIT")
#     print("10. Share contact by email")
#     print("11. Backup archive")
#     print("12. Delete archive file")

#     try:
#         choice = int(input("Select option: "))
#     except ValueError:
#         print("Input Error")
#         continue

#     if choice == 1:
#         print(add_contact_input(archieve))
#     elif choice == 2:
#         print(change_contact_input(archieve))
#     elif choice == 3:
#         print(search_contact_input(archieve))
#     elif choice == 4:
#         print(delete_contact_input(archieve))
#     elif choice == 5:
#         show_archieve(archieve)
#     elif choice == 6:
#         sort_archieve(archieve)
#         print("Archieve sorted by name")
#     elif choice == 7:
#         send_email()
#     elif choice == 8:
#         save_archieve(archieve, "archieve.txt")
#         print("Changes saved")
#     elif choice == 9:
#         print("Exiting program...")
#         break
#     elif choice == 10:
#         share_contact_by_email(archieve)
#     elif choice == 11:
#         backup_archieve()
#     elif choice == 12:
#         delete_archieve_file()

