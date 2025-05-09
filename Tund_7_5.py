from tkinter import *
from tkinter import messagebox, simpledialog
from class1 import *


archieve = load_archieve("archieve.txt")


box = Tk()
box.title("Contact Archieve")
box.geometry("800x1000")
box.configure(bg="lightgrey")
box.resizable(width=True, height=True)
box.iconbitmap("mask.ico")

display_frame = Frame(box, bg="lightgrey")


entering=Entry(box, width=50, font=("Arial", 14), bg="lightgrey")
entering.insert(0, "Enter name, number or email to search")
entering.pack(pady=10, padx=10)



button_row =tk =Frame(box, bg="lightgrey")
button_row.pack(pady=5)

tk.Button(button_row, text="Add Contact", command=lambda: add_contact(archieve)).pack(side=LEFT, padx=5)
tk.Button(button_row, text="Change Contact", command=lambda: change_contact(archieve)).pack(side=LEFT, padx=5)
tk.Button(button_row, text="Search Contact", command=lambda: search_contact(archieve)).pack(side=LEFT, padx=5)
tk.Button(button_row, text="Delete Contact", command=lambda: delete_contact(archieve)).pack(side=LEFT, padx=5)
tk.Button(button_row, text="Show Archieve", command=lambda: show_archieve(archieve)).pack(side=LEFT, padx=5)
tk.Button(button_row, text="Sort Archieve", command=lambda: sort_archieve(archieve)).pack(side=LEFT, padx=5)
tk.Button(button_row, text="Send Email", command=lambda: send_email()).pack(side=LEFT, padx=5)
tk.Button(button_row, text="Save Changes", command=lambda: save_archieve(archieve, "archieve.txt")).pack(side=LEFT, padx=5)
tk.Button(button_row, text="Exit", command=box.quit).pack(side=LEFT, padx=5)

# Create a frame for the display box
display_frame = Frame(box, bg="lightgrey")
display_frame.pack(pady=20, padx=20, fill=BOTH, expand=True)



box.mainloop()

# print("Welcome to phones numbers and emails archive")

# archieve= load_archieve("archieve.txt")
#archieve=[[],[],[]]
# start = input ("Please type '1' to start the program or '0' to exit: ")
# if start == "1":
#     while True:
#             print("_"*20)
#             print("Options:")
#             print("1. Add new contact")
#             print("2. Change contact")
#             print("3. Search contact")
#             print("4. Delete contact")
#             print("5. Show archieve")
#             print("6. Sort archieve by name")
#             print("7. Send Email")
#             print("8. SAVE CHANGES")
#             print("9. EXIT")

#             try:
#                 choice= int(input("Select option: "))
#                 print("_"*20)
#             except ValueError:
#                 print("input Error")
#                 continue
#             if choice == 1:
#                 name = input("Enter new contact name: ")
#                 number = input("Enter new contact number: ")
#                 email = input("Enter new contact email: ")
#                 print(add_contact(archieve, name, number, email))
#             elif choice == 2:
#                 name = input("Enter contact name to change: ")
#                 new_name = input("Enter new contact name: ")
#                 new_number = input("Enter new contact number: ")
#                 new_email = input("Enter new contact email: ")
#                 print(change_contact(archieve, name, new_name, new_number, new_email))
#             elif choice == 3:
#                 contact = input("Enter contact name, number or email to search: ")
#                 print(search_contact(archieve, contact))
#             elif choice == 4:
#                 name = input("Enter contact name to delete: ")
#                 print(delete_contact(archieve, name))
#             elif choice == 5:
#                 show_archieve(archieve)
#             elif choice == 6:
#                 sort_archieve(archieve)
#                 print("Archieve sorted by name")
#             elif choice == 7:
#                 send_email()
#             elif choice == 8:
#                 save_archieve(archieve, "archieve.txt")
#                 print("Changes saved")
#             elif choice == 9:
#                 print("Exiting program...")
#                 break
# elif start == "0":
#             print("Exiting program...")
# else:
#      print("Invalid choice. Please try again.")
